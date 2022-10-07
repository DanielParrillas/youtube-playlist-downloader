from pytube import Playlist, YouTube

playlist_url = input("Pege el link de la playlist: ")

playlist = Playlist(playlist_url)

try:
    cantidad = len(playlist)
except Exception as e:
    print("No se pudo obtener la lista\n" + str(e))
else:
    print(playlist.title + '\n')
    for video_url in playlist:
        try:
            video = YouTube(video_url)
        except Exception as e:
            print("No se pudo obtener video: " + link)
            print(str(e))
        else:
            print("\t" + video.title)
            try:
                #obtener stream de mejor calidad
                stream = video.streams.filter(mime_type="video/mp4", progressive="True")[-1]
            except Exception as e:
                print("\tNo se pudo acceder al stream del video" + str(e))
            else:
                print("\t\tdescargando...\n\t\t" + str(stream))
                stream.download('downloads/')
                print("\t\t...completado!\n\t\t" + str(stream))