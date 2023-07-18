from pytube import YouTube


def download_video(url, resolution='720p'):
    video = YouTube(url)
    filename = f"{video.title}.mp4"
    output_path = './'

    stream = video.streams.filter(res=resolution).first()
    stream.download(filename=filename, output_path=output_path)


if __name__ == "__main__":
    url = input("Ingresa la URL del video de YouTube que deseas descargar: ")
    resolution = input(
        "Ingresa la resolución deseada (ej. 720p, 1080p, etc.): ")

    download_video(url, resolution)
