import subprocess
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import moviepy.editor as mp

answer=True
while answer:
    print("""
        1.Create a script which can cut N seconds the BBB video. 
        2.Create a script which will extract the YUV histogram from the previous 
        BBB video you’ve done and create a new video with both images at the
         same time.
        3.Create a script which can resize the BBB video into 4 differents video
         outputs 
            a) 720p
            b) 480p
            c) 360x240
            d) 160x120
        4.Create a script which can change the audio into mono output and in a
         different audio codec
            a)Change to mono audio
            b)Change to mp3
        5.Exit
        """)
    answer = int(input("What would you like to do? \n"))
    #Ex 1
    if answer == 1:
        video = input(
            "Introduce the directory of the video you want to cut: \n ")
        start_time = int(
            input("Introduce at which second you want to start the cut: \n "))
        end_time = int(
            input("Introduce at which second you want to end the cut: \n "))
        print("The video will be save as cut_video.mp4")
        ffmpeg_extract_subclip(video, start_time, end_time,
                               targetname="cut_video.mp4")
    #Ex 2
    elif answer == 2:
        video = input(
            "Introduce the directory of the video you want to cut: \n ")
        subprocess.call(["ffmpeg", "-i", video, "-vf",
                         "split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay",
                         "output_yuv.mp4"])
    #Ex 3
    elif answer == 3:
        video = input(
            "Introduce the directory of the video you want to cut: \n ")
        size = int(
            input("INTRODUCE: \n 1 if you want 720p \n 2 if you want 480p\n 3 if you want "
                  "360x240 \n or anything else if you want 160x120: \n "))

        clip = mp.VideoFileClip(video)
        if size == 1:
            clip_resized = clip.resize(newsize=(1280, 720))
            clip_resized.write_videofile("resized_video_720p.mp4")
        elif size == 2:
            clip_resized = clip.resize(newsize=(852, 480))
            clip_resized.write_videofile("resized_video_480p.mp4")
        elif size == 3:
            clip_resized = clip.resize(newsize=(360, 240))
            clip_resized.write_videofile("resized_video_360x240.mp4")
        elif size == 4:
            clip_resized = clip.resize(newsize=(160, 120))
            clip_resized.write_videofile("resized_video_160x120.mp4")

    #Ex 4
    elif answer == 4:
        video = input(
            "Introduce the directory of the video you want to change the audio: \n ")
        option = int(input(
            "Choose 1 mono auido \n 2 Encode in different audio codec: "))

        if (option == 1):
            subprocess.call(
                ['ffmpeg', '-i', video, '-ac', '1', 'mono_video.mp4'])
        elif (option == 2):
            subprocess.call(
                ['ffmpeg', '-i', video, '-acodec', 'aac', '-vcodec', 'copy',
                 'aac_video.mp4'])
        else:
            print("Invalid command")
    #To exit
    elif answer == 5:
        answer = False
    #Wrong command
    else:
        print("Write a valid command")