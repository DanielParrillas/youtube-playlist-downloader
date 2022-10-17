from pytube import Playlist, YouTube
from termcolor import colored, cprint
from colorama import Fore, Back, Style

cprint(" ► ", 'green', 'on_red', end=' ')
cprint("YOUTUBE PLAYLIST DOWNLOADER\n", attrs=['bold'])
playlist_url = input("Pege el link de la playlist: " + Fore.BLUE)
print(Style.RESET_ALL)

playlist = Playlist(playlist_url)

try:
    cantidad = len(playlist)
    nombre_lista = str(playlist.title)
    cprint(Fore.BLACK + Back.WHITE + "Playlist " + nombre_lista, attrs=['bold'])
    print(Style.RESET_ALL)
    # print(str(playlist.title) + '\n')
except Exception as e:
    cprint("\n\tError!",'red',attrs=['bold'], end=' ')
    cprint("No se pudo obtener la lista " + str(e))
else:
    for video_url in playlist:
        try:
            video = YouTube(video_url)
        except Exception as e:
            cprint("Error!",'red',attrs=['bold'], end=' ')
            print("No se pudo obtener video: " + link)
            print(str(e))
        else:
            print("\n\t" + Fore.BLACK + Back.WHITE + video.title)
            print(Style.RESET_ALL)
            try:
                #obtener stream de mejor calidad
                stream = video.streams.filter(mime_type="video/mp4", progressive="True")[-1]
            except Exception as e:
                cprint("Error!",'red',attrs=['bold'], end=' ')
                print("\tNo se pudo acceder al stream del video" + str(e))
            else:
                cprint("descargando...", 'green')
                print(str(stream))
                stream.download('downloads/')
                cprint("...completado!", 'blue')