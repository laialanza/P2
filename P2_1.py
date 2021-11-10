from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

video = input("Introduce the directory of the video ypu want to cut: \n ")
start_time = int(input("Introduce at which second you want to start the cut: \n "))
end_time = int(input("Introduce at which second you want to end the cut: \n "))

ffmpeg_extract_subclip(video, start_time, end_time, targetname="cut_video.mp4")