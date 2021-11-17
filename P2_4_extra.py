import subprocess
video = input("Introduce the directory of the video you want to change the audio: \n ")
answer = int(input("Choose 1 mono audio \n 2 Encode in different audio codec: "))

if(answer == 1):
    subprocess.call(['ffmpeg', '-i', video, '-ac', '1', 'mono_video.mp4'])
elif (answer == 2):
    subprocess.call(
        ['ffmpeg', '-i', video, '-acodec', 'aac', '-vcodec', 'copy',
         'aac_video.mp4'])
else:
    print("Invalid command")