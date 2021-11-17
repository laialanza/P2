import moviepy.editor as mp
from pydub import AudioSegment

video = input("Introduce the directory of the video you want to change the audio: \n ")
type_audio = int(input("Introduce 1 for a WAV mono or else for MP3 audio: \n")) #Doing it for different codecs
my_clip = mp.VideoFileClip(video) #Obtain the video
if(type_audio ==1):
    my_clip.audio.write_audiofile(r"my_result.wav") #Save the audio

    sound = AudioSegment.from_wav("my_result.wav") #Read the audio of the video
    sound = sound.set_channels(1) #Set audio to mono
    sound.export("mono_result.wav", format="wav") #Save the audio
    audioclip = mp.AudioFileClip("mono_result.wav")  # Read the audio
    new_audioclip = mp.CompositeAudioClip([audioclip])
    my_clip.audio = new_audioclip  # Change the audio of the video
    my_clip.write_videofile("mono_video.mp4")  # Save the new video

else:
    my_clip.audio.write_audiofile(r"output.mp3")
    audioclip = mp.AudioFileClip("output.mp3")  # Read the audio
    new_audioclip = mp.CompositeAudioClip([audioclip])
    my_clip.audio = new_audioclip  # Change the audio of the video
    my_clip.write_videofile("audio_mp3.mp4")  # Save the new video

