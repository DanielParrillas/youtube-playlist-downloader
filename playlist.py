from pytube import Playlist, YouTube, exceptions
import pytube

# playlist_link = 'https://www.youtue.com/playeefd/3st=PL3817D41C7D841E23'
playlist_link = 'https://www.youtube.com/playlist?list=PL3817D41C7D841E23'



playlist = Playlist(playlist_link)
youtube_list = []
try:
    cantidad = len(playlist)
    for link in playlist:
        try:
            youtube_list.append(YouTube(link))
        except Exception as e:
                print(e)
except Exception as e:
    print(e)
    print("Error en el recorrido")
else:
    for youtube in youtube_list:
        print(youtube)
        video = youtube.streams.filter(mime_type="video/mp4", progressive="True")
        for stream in video:
            print('\t' + str(stream))
        # video.download('cache/')