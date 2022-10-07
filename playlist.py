from pytube import Playlist, YouTube

playlist = Playlist('https://www.youtube.com/playlist?list=PL3817D41C7D841E23')
# print(playlist)
youtube_list = []

for link in playlist:
    youtube_list.append(YouTube(link))

for youtube in youtube_list:
    # print(youtube)
    # video = youtube.streams.filter(only_audio=True, abr='160kbps')[0]
    video = youtube.streams.filter(file_extension='mp4', abr='128kbps')[0]
    video.download('cache/')Marn2022