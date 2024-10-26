from nltk.parse.stanford import StanfordDependencyParser
import numpy as np
import cv2
import imageio
from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip
import nltk
import os
import sys
import argparse
from nltk.parse.stanford import StanfordParser
from nltk.tag.stanford import StanfordPOSTagger, StanfordNERTagger
from nltk.tokenize.stanford import StanfordTokenizer
from nltk.tree import *
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import warnings
import requests
from bs4 import BeautifulSoup
from pytube import YouTube
from urllib.error import HTTPError
import pyttsx3

# Define headers and paths
output_path = "D:\\Shreyas_Codez\\AIA_Proj"
headers = {
    'authority': 'indiansignlanguage.org',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Cookie': 'cf_clearance=Vt_PPbkPKyr6QVKpSjjs.LnhUrq.453SWtsnQ7RqFPg-1705825351-1-AfPAQ7SHFiGiAdLo8mtwG5/ttJ2WOr0T0U1+7H4qByBGdT9lECChhCXse/+cJXYsj7Uu2Jq2/pBj69+/m3EBHek=',
    'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# Download function with try-except for handling HTTPError
def download_youtube_video(embedded_url, output_path):
    try:
        yt = YouTube(embedded_url)
        video_stream = yt.streams.get_highest_resolution()
        video_stream.download(output_path)
        print("Video downloaded successfully!")
    except HTTPError as e:
        if e.code == 410:
            print("Error: Video is no longer available (HTTP Error 410: Gone)")
        else:
            print(f"HTTP Error: {e}")
    except Exception as e:
        print(f"Error downloading video: {e}")

# Add audio to video function
def add_audio_to_video(video_path, audio_path, output_path):
    try:
        video_clip = VideoFileClip(video_path)
        audio_clip = AudioFileClip(audio_path)
        video_clip = video_clip.set_audio(audio_clip)
        video_clip.write_videofile(output_path)
    except Exception as e:
        print(f"Error adding audio to video: {e}")

# Text-to-speech engine setup
engine = pyttsx3.init()
engine.setProperty('rate', engine.getProperty('rate') - 50)
engine.setProperty('volume', 0.9)
engine.setProperty('voice', engine.getProperty('voices')[1].id)

# Prepare input and setup Stanford Parser
inputString = input("Enter the String to convert to ISL: ")
try:
    parser = StanfordParser(model_path='D:\\stanford-parser-full-2018-02-27\\edu\\stanford\\nlp\\models\\lexparser\\englishPCFG.ser.gz')
    englishtree = [tree for tree in parser.parse(inputString.split())]
    parenttree = ParentedTree.convert(englishtree[0])
except Exception as e:
    print(f"Error initializing parser: {e}")

# ISL parsing and sentence construction
dict = {sub.treeposition(): 0 for sub in parenttree.subtrees()}
isltree = Tree('ROOT', [])
i = 0

# Construct ISL tree and parsed sentence
for sub in parenttree.subtrees():
    if sub.label() in {"NP", "VP", "PRP"} and dict[sub.treeposition()] == 0:
        dict[sub.treeposition()] = 1
        isltree.insert(i, sub)
        i += 1

parsed_sent = isltree.leaves()
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()
ps = PorterStemmer()
lemmatized_words = [lemmatizer.lemmatize(ps.stem(w)) for w in parsed_sent if w not in stop_words]
islsentence = " ".join(lemmatized_words)
print(islsentence)

# Remove temporary files with try-except
for filename in ["video.mp4", "Final.mp4"]:
    try:
        os.remove(filename)
    except FileNotFoundError:
        pass

# Data sourcing and video concatenation with try-except
for each_word in lemmatized_words:
    url = f'https://indiansignlanguage.org/{each_word}/'
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            iframe_tag = soup.find('iframe')
            if iframe_tag and (embedded_link := iframe_tag.get('src')):
                print(f'Embedded Link: {embedded_link}')
                download_youtube_video(embedded_link, output_path)
            else:
                print(f"No video found for {each_word}.")
        else:
            print(f"Request failed for {each_word} with status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error fetching video for {each_word}: {e}")

# Concatenate videos
arg_array = []
try:
    for word in lemmatized_words:
        clip = VideoFileClip(f"{output_path}\\{word}.mp4")
        arg_array.append(clip)
    final_clip = concatenate_videoclips(arg_array)
    final_clip.write_videofile("video.mp4")
except FileNotFoundError as e:
    print(f"Error in video file processing: {e}")

# Clean up downloaded files
for word in lemmatized_words:
    try:
        os.remove(f"{output_path}\\{word}.mp4")
    except FileNotFoundError:
        pass

# TTS conversion to audio and adding audio to video
try:
    engine.save_to_file(f"Translation for: {inputString}", "audio.mp3")
    engine.runAndWait()
    add_audio_to_video("video.mp4", "audio.mp3", "Final.mp4")
except Exception as e:
    print(f"Error in audio processing or adding to video: {e}")

# Clean up final temporary files
for filename in ["audio.mp3"]:
    try:
        os.remove(filename)
    except FileNotFoundError:
        pass
