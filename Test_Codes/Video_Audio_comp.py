from moviepy.editor import VideoFileClip, AudioFileClip

def add_audio_to_video(video_path, audio_path, output_path):
    video_clip = VideoFileClip(video_path)

    audio_clip = AudioFileClip(audio_path)

    video_clip = video_clip.set_audio(audio_clip)

    video_clip.write_videofile(output_path)

add_audio_to_video('D:\\Shreyas_Codez\\AIA_Proj\\Offline_Dataset\\banana.mp4', 'test.mp3', 'output.mp4')
