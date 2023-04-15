# YouTube Downloader with Pytube
This is a Python script that allows you to download videos or playlists from YouTube using the pytube library.

# Requirements

Python 3.x

pytube (you can install it with `pip install pytube`)

# How to use
1. Clone this repository on your machine

- `git clone https://github.com/your_username/YouTube-Downloader.git`

2. Run the youtube_downloader.py script with Python.

- `python youtube_downloader.py`

3. Enter the link of the video or playlist you want to download

4. The download will start automatically
5. When the download is complete, you can choose whether you want to download more videos or exit the program.

# Functions
The script contains the following functions:

- _check_video_exist(title): checks if the video already exists in your download folder
- _progress_callback(stream, chunk, remaining_bytes): displays the download progress bar
- _download_video(stream, yt, path=''): downloads a specific video
- _download_playlist(playlist): downloads all videos in a playlist
- download(yt_link): downloads a video or entire playlist

# How to contribute
You can contribute to this project in various ways. Some suggestions include:

- Reporting errors and bugs
- Adding new features
- Improving documentation
- Translating documentation to other languages

# Author
This project was created by MallowHerman.
