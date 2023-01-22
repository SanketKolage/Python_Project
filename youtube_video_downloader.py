
from pytube import YouTube
user_input = input("Enter Link")
link = user_input
y1 = YouTube(link)

videos = y1.streams.all()

vid = list(enumerate(videos))

for i in vid:
    print(i)
print()

strm = int(input("Enter :"))

videos[strm].download()
print("Download Completed...")