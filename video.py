from pytube import YouTube

link = 'https://youtu.be/laZusNy8QiY?list=PL3817D41C7D841E23'
# link = 'https://youtu.be/laZusNy8QiY?li=PL3817D41C7D841E23'

try:
    yt = YouTube(link)
except Exception as e:
    print(e)
else:
    print("Video seleccionado:\t" + yt.title)
    videos = yt.streams.filter(file_extension='mp4')
    for video in videos:
        print(video)
    print(len(videos))
    # video.download('cache/')

# (file_extension='mp4')
# (only_audio=True)
# (only_audio=True, abr='160kbps')
# (only_audio=True, abr='160kbps')[0]
# (only_audio=True, file_extension='mp4')