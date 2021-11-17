import moviepy.editor as mp
video = input(
            "Introduce the directory of the video you want to cut: \n ")
size = int(input("PUT 1 if you want 720p \n 2 if you want 480p\n 3 if you want "
                 "360x240 \n or anything else if you want 160x120: \n "))

clip = mp.VideoFileClip(video)
if size == 1:
    clip_resized = clip.resize(newsize=(1280, 720))
if size == 2:
    clip_resized = clip.resize(newsize=(852, 480))
if size==3:
    clip_resized = clip.resize(newsize=(360,240))
else:
    clip_resized = clip.resize(newsize=(160, 120))

clip_resized.write_videofile("resized_video.mp4")

