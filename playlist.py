from pytube import Playlist, YouTube

print("► YOUTUBE PLAYLIST DOWNLOADER\n")
playlist_url = input("Pege el link de la playlist: ")

playlist = Playlist(playlist_url)
no_descargados = []

try:
    cantidad = len(playlist)
    nombre_lista = str(playlist.title)
    print("Playlist " + nombre_lista)
except Exception as e:
    print("\n\tError!", end=' ')
    print("No se pudo obtener la lista " + str(e))
else:
    for video_url in playlist:
        try:
            video = YouTube(video_url)
        except Exception as e:
            print("Error!", 'red', end=' ')
            print("No se pudo obtener video: " + video_url)
            print(str(e))
        else:
            print("\n\t" + video.title)
            try:
                # obtener stream de mejor calidad
                stream = video.streams.filter(mime_type="video/mp4", progressive="True")[-1]
            except Exception as e:
                print("Error!", end=' ')
                print("\tNo se pudo acceder al stream del video" + str(e))
            else:
                print("descargando...")
                print(str(stream))
                try:
                    stream.download('downloads/')
                except Exception as e:
                    print("Fallo la descarga")
                    no_descargados.append(video.title)
                else:
                    print("...completado!")
