import typer
from pytube import YouTube
from pytube.exceptions import VideoUnavailable, RegexMatchError

app = typer.Typer()


@app.command()
def download_video(url: str, resolution: str):
    """
    Download a video from YouTube in the specified resolution.

    Parameters:
        url (str): The URL of the YouTube video to download.
        resolution (str): The desired resolution of the video. This should be a string representing the
                          resolution, e.g., '720p', '1080p', '480p', etc.

    Raises:
        VideoUnavailable: If the video is not available for download.
        RegexMatchError: If there is an error in the video URL format.
        Exception: For any other unexpected errors during the download process.

    Note:
        - The downloaded video will be saved in the same directory as this script with the filename
          being the title of the video appended with the '.mp4' extension.
        - If the specified resolution is not available, the video will be downloaded in the best
          available resolution.

    Example:
        To download a video with the URL 'https://www.youtube.com/watch?v=abcdef' in 720p resolution:
        ```
        download_video(url='https://www.youtube.com/watch?v=abcdef', resolution='720p')
        ```

        If the specified resolution is not available, it will automatically download the best
        available resolution:
        ```
        download_video(url='https://www.youtube.com/watch?v=abcdef', resolution='480p')
        ```
    """
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
            typer.echo(
                f"Resolution '{resolution}' not found. Downloading in the best resolution.")
            stream = video.streams.get_highest_resolution()

        typer.echo(
            f"Downloading '{video.title}' in resolution '{stream.resolution}'...")
        # Download the video
        stream.download(filename=filename, output_path=output_path)

        typer.echo("¡Download finished!")

    except VideoUnavailable:
        typer.echo("The video is not available for download")
    except RegexMatchError:
        typer.echo("Video URL format error")
    except Exception as e:
        typer.echo(f"An error occurred during download: {str(e)}")


if __name__ == "__main__":
    app()
