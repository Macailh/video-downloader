from pytube import YouTube


def download_video(url, resolution='720p', path='./'):

    filename = "video.mp4"

    video = YouTube(url)
    stream = video.streams.filter(res=resolution).first()
    stream.download(filename=filename, output_path=path)


if __name__ == "__main__":
    url = input("Ingresa la URL del video de YouTube que deseas descargar: ")
    resolution = input(
        "Ingresa la resolución deseada (ej. 720p, 1080p, etc.): ")

    download_video(url, resolution)
