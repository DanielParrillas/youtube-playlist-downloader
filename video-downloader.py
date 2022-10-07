from pytube import YouTube

yt = YouTube('https://youtu.be/laZusNy8QiY?list=PL3817D41C7D841E23')

print("Video seleccionado:\t" + yt.title)
# videos = yt.streams
# videos = yt.streams.filter(file_extension='mp4')
# videos = yt.streams.filter(only_audio=True)
# video = yt.streams.filter(only_audio=True, abr='160kbps')
# video = yt.streams.filter(only_audio=True, abr='160kbps')[0]
# videos = yt.streams.filter(only_audio=True, file_extension='mp4')
videos = yt.streams.filter(file_extension='mp4', abr='128kbps')
print(videos)

# video.download('cache/')

# print(len(videos))

