from pytube import YouTube
from sys import argv       #argv is a list in Python, which contains the command-line arguments passed to the script.

link = argv[1]              #link is the first argument passed to the script

yt = YouTube(link)         

print("Title: ", yt.title)

yd = yt.streams.get_by_resolution('720p') #this will get the video with 720p resolution(since there are multiple steams of video)

print("Downloading...")
yd.download("F:\Automated Video Downloader\Downloaded Video")
