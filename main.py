import typer
from pytube import YouTube
from pytube.exceptions import VideoUnavailable, RegexMatchError

app = typer.Typer()


@app.command()
def download_video(url: str, resolution: str):
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
