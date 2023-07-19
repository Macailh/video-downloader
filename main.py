from pytube import YouTube
from pytube.exceptions import VideoUnavailable, RegexMatchError


def download_video(url, resolution='720p'):
    try:
        # Get video information
        video = YouTube(url)

        # Get video title
        filename = f"{video.title}.mp4"

        # Define output path
        output_path = './'

        # Filter by resolution
        stream = video.streams.filter(res=resolution).first()

        if not stream:
            print(
                f"Resolution '{resolution}'not found. Downloading in the best resolution.")
            stream = video.streams.get_highest_resolution()

        print(
            f"Downloading '{video.title}' in resolution '{stream.resolution}'...")
        # Download the video
        stream.download(filename=filename, output_path=output_path)

        print("¡Download finished!")

    except VideoUnavailable:
        print("The video is not available for download")
    except RegexMatchError:
        print("Video URL format error")
    except Exception as e:
        print(f"An error occurred during download: {str(e)}")


if __name__ == "__main__":
    url = input("Ingresa la URL del video de YouTube que deseas descargar: ")
    resolution = input(
        "Ingresa la resolución deseada (ej. 720p, 1080p, etc.): ")

    download_video(url, resolution)
