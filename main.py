from pytube import YouTube


def download_video(url, resolution='720p'):
    # Get video information
    video = YouTube(url)

    # Get video title
    filename = f"{video.title}.mp4"

    # Define output path
    output_path = './'

    # Filter by resolution
    stream = video.streams.filter(res=resolution).first()

    print(
        f"Downloading '{video.title}' in resolution '{stream.resolution}'...")
    # Download the video
    stream.download(filename=filename, output_path=output_path)

    print("¡Download finished!")


if __name__ == "__main__":
    url = input("Ingresa la URL del video de YouTube que deseas descargar: ")
    resolution = input(
        "Ingresa la resolución deseada (ej. 720p, 1080p, etc.): ")

    download_video(url, resolution)
