import subprocess
subprocess.call(["ffmpeg", "-i", "cut_video.mp4", "-vf",
                 "split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay",
                 "output_yuv.mp4"])