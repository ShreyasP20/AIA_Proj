from nltk.parse.stanford import StanfordDependencyParser
import numpy as np
import cv2
import imageio
imageio.plugins.ffmpeg.download()
from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.editor import VideoFileClip, concatenate_videoclips
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
os.environ['CLASSPATH']='D:\\stanford-parser-full-2018-02-27'
inputString = " "
java_path = "C:\\Program Files\\Java\\jdk-9.0.4\\bin\\java.exe"
os.environ['JAVAHOME'] = java_path
warnings.filterwarnings("ignore", category=DeprecationWarning)

for each in range(1,len(sys.argv)):
    inputString += sys.argv[each]
    inputString += " "

inputString = input("Enter the String to convert to ISL: ")
parser=StanfordParser(model_path='D:\\stanford-parser-full-2018-02-27\\edu\\stanford\\nlp\\models\\lexparser\\englishPCFG.ser.gz')
s = inputString
o=parser.parse(s.split())
englishtree=[tree for tree in parser.parse(inputString.split())]
parsetree=englishtree[0]
dict={}
# "***********subtrees**********"
parenttree= ParentedTree.convert(parsetree)
for sub in parenttree.subtrees():
    dict[sub.treeposition()]=0

#"----------------------------------------------"
isltree=Tree('ROOT',[])
i=0
for sub in parenttree.subtrees():
    if(sub.label()=="NP" and dict[sub.treeposition()]==0 and dict[sub.parent().treeposition()]==0):
        dict[sub.treeposition()]=1
        isltree.insert(i,sub)
        i=i+1
        
    if(sub.label()=="VP" or sub.label()=="PRP"):
        for sub2 in sub.subtrees():
            if((sub2.label()=="NP" or sub2.label()=='PRP')and dict[sub2.treeposition()]==0 and  dict[sub2.parent().treeposition()]==0):
                dict[sub2.treeposition()]=1
                isltree.insert(i,sub2)
                i=i+1
                
for sub in parenttree.subtrees():
    for sub2 in sub.subtrees():
        if(len(sub2.leaves())==1 and dict[sub2.treeposition()]==0 and dict[sub2.parent().treeposition()]==0):
            dict[sub2.treeposition()]=1
            isltree.insert(i,sub2)
            i=i+1
            
parsed_sent=isltree.leaves()
words=parsed_sent
stop_words=set(stopwords.words("english"))


lemmatizer = WordNetLemmatizer()
ps = PorterStemmer()
lemmatized_words=[]

for w in parsed_sent:
    w=ps.stem(w)
    lemmatized_words.append(lemmatizer.lemmatize(w))
    
islsentence = ""
for w in lemmatized_words:
    if w not in stop_words:
        islsentence+=w
        islsentence+=" "
        
print(islsentence)


try:
    os.remove("my_concatenation.mp4")
except:
    pass
print(sys.path)
name=islsentence

for each in range(1,len(sys.argv)):
    name+=sys.argv[each]
    name+=" "
    
input_text=name
text = nltk.word_tokenize(input_text)
result=nltk.pos_tag(text)
for each in result:
    print(each[0])
    url = f'https://indiansignlanguage.org/{each[0]}/'  
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        iframe_tag = soup.find('iframe')
        
        if iframe_tag:
            embedded_link = iframe_tag.get('src')

            if embedded_link:
                print(f'Embedded Link: {embedded_link}')
                download_youtube_video(embedded_link,output_path)
                
            else:
                print('No src attribute found in the <iframe> tag.')
        else:
            print('No <iframe> tag found on the page.')
    else:
        print(f'Request failed with status code: {response.status_code}')
        if response.status_code == 403:
            print('Replace the Cookie header with new Cookie')



dict={}
dict["NN"]="noun"
arg_array=[]
#for text in result:
    # arg_array.append(VideoFileClip(text[0]+".mp4"))
    # print(text[0]+".mp4")

# print(arg_array[0])

# final_clip = concatenate_videoclips(arg_array)
# final_clip.write_videofile("my_concatenation.mp4")



