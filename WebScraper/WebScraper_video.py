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


embedded_url = "https://www.youtube.com/embed/nbGetUh9P74"

output_path = "D:\\Shreyas_Codez\\AIA_Proj"

download_youtube_video(embedded_url, output_path)