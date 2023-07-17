from pytube import YouTube


url = input("Enter video url: ")
resolution = "720p"

path = "./"
filename = "video.mp4"

video = YouTube(url)
stream = video.streams.filter(res=resolution).first()
stream.download(filename=filename)
