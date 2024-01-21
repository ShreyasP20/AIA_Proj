from pytube import YouTube
from urllib.error import HTTPError

def download_youtube_video(embedded_url, output_path):
    try:
        # Create a YouTube object
        yt = YouTube(embedded_url)

        # Get the highest resolution stream
        video_stream = yt.streams.get_highest_resolution()

        # Set the output path for the downloaded video
        video_stream.download(output_path)

        print("Video downloaded successfully!")

    except HTTPError as e:
        if e.code == 410:
            print("Error: Video is no longer available (HTTP Error 410: Gone)")
        else:
            print(f"HTTP Error: {e}")

# Replace 'YOUR_EMBEDDED_URL' with the actual embedded URL of the YouTube video
embedded_url = "https://www.youtube.com/embed/nbGetUh9P74"

# Replace 'YOUR_OUTPUT_PATH' with the desired output path for the downloaded video
output_path = "D:\\Shreyas_Codez\\AIA_Proj"

download_youtube_video(embedded_url, output_path)