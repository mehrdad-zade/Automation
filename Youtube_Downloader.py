'''
This program, downloads YouTube videos in the desired format

Install Pre-Requisits:

sudo pip3 install youtube_dl
brew install ffmpeg
'''
#from __future__ import unicode_literals
import youtube_dl

def downloader(vid):
	ydl_opts = {
	    'format': 'bestaudio/best',
	    'postprocessors': [{
	        'key': 'FFmpegExtractAudio',
	        'preferredcodec': 'mp3',
	        'preferredquality': '192',
	    }],
	}

	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download([vid])


#2 sample videos for download, 
#you can keep the single quotes and add your youtube url instead
list_of_youtube_vids = [
'https://www.youtube.com/watch?v=qaAkN3gcg_0',
'https://www.youtube.com/watch?v=XqZsoesa55w'
]

for vid in list_of_youtube_vids:
	downloader(vid)

