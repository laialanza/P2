import subprocess
video = input("Introduce the directory of the video you want to cut: \n ")
subprocess.call(["ffmpeg", "-i", video, "-vf",
                 "split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay",
                 "output_yuv.mp4"])