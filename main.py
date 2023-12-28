from pytube import YouTube
from sys import argv       #argv is a list in Python, which contains the command-line arguments passed to the script.

link = argv[1]              #link is the first argument passed to the script

yt = YouTube(link)         

print("Title: ", yt.title)
