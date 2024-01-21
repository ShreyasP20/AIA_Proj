# NLP Script for Indian Sign Language Translation

This script is designed to convert a given English sentence into Indian Sign Language (ISL). It utilizes various NLP (Natural Language Processing) tools and external libraries to achieve this goal. Let's break down the functionality and components of the script.

## Dependencies

The script relies on several Python libraries and external tools. Make sure you have them installed before running the script.

- `nltk`: Natural Language Toolkit for NLP tasks.
- `moviepy`: Library for video editing tasks.
- `imageio`, `pytube`: For working with video streams and downloads.
- `pyttsx3`: Text-to-speech library for audio synthesis.
- `requests`, `beautifulsoup4`: For web scraping to get YouTube embedded links.
- `Stanford NLP`: A suite of NLP tools including parsers, tokenizers, and taggers.

## Usage

1. **Clone the Repository**

    ```bash
    git clone https://github.com/ShreyasP20/AIA_Proj.git
    cd AIA_Proj
    ```

2. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Script**

    ```bash
    python NLP_WS_TTS.py 
    ```

    Follow the prompts and input the English sentence when prompted.

4. **Output**

    The script will generate an ISL video (`Final.mp4`) with audio synthesis of the translated sentence.

## Script Explanation

1. **Downloading YouTube Video**

    - The `download_youtube_video` function utilizes the `pytube` library to download YouTube videos given an embedded link.

2. **Audio-Video Processing**

    - The script uses `moviepy` to concatenate video clips for each word in the input sentence and adds synthesized audio using `pyttsx3`.

3. **NLP Processing**

    - The script utilizes the Stanford NLP tools for parsing the input English sentence, extracting noun phrases, and lemmatization.

4. **Web Scraping for ISL Translations**

    - It scrapes the Indian Sign Language website to find embedded YouTube links for each word in the input sentence.

5. **Speech Synthesis**

    - The script uses `pyttsx3` for text-to-speech synthesis, creating an audio file (`audio.mp3`) for the translated sentence.

6. **Final Output**

    - The final ISL video with audio is saved as `Final.mp4`.

## Note


- The script may require modifications based on changes in external libraries or website structures.
- Standford Parser is needed to be downloaded from there officical website. (stanford-parser-full-2018-02-27)

Feel free to explore and modify the script according to your requirements!
