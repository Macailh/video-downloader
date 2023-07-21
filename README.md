# Video downloader

This is a simple command-line application that allows you to download YouTube videos using Python. It utilizes the `pytube` library to fetch and download the videos.

## Installation

Before running the application, make sure you have Python installed on your system.

1. Clone the repository or download the `youtube_downloader.py` file.
2. Install the required dependencies using pip. You can do this by running the following command in your terminal or command prompt:

`$pip install pytube typer`

## Use

To download a YouTube video, you need to run the `youtube_downloader.py` script from your terminal or command prompt with the appropriate arguments.

`code`

Replace `<URL>` with the URL of the YouTube video you want to download and `<resolution>` with the desired resolution (e.g., "720p", "480p", "360p", etc.). The downloaded video will be saved as an MP4 file in the same directory as the script.

## Troubleshooting

- If you encounter any issues during the download process, make sure you have a stable internet connection and the video is available for download on YouTube.
- If the provided video URL is incorrect or malformed, the application will display an error message.
- If the specified resolution is not available for the video, it will attempt to download the video in the best available resolution.
- If the video is not available for download, the application will notify you accordingly.
- For any other unexpected errors during the download process, an error message will be displayed with details about the issue.

## Disclaimer

This application is intended for personal use only and should comply with YouTube's terms of service. It is essential to respect copyright laws and the content creators' rights when downloading videos. Always ensure that you have the necessary permissions to download and use the videos responsibly.
