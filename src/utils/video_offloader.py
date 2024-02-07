import logging 
import os
import ffmpeg
from pytube import YouTube
import string
from src.utils.cache import check_cache


def offload_video(url):
    yt = YouTube(url)
    title = (yt.title).translate(str.maketrans("", "", string.punctuation)).lower()

    if check_cache(folder="src/data/video/", filename=title):
        return title

    video_url = yt.streams.all()[0].url
    audio, err = (
        ffmpeg
        .input(video_url)
        .output("pipe:", format="wav",acodec="pcm_s16le")
        .run(capture_stdout=True)
    )
    with open(f"src/data/video/{title}.mp3", "wb+") as f:
        f.write(audio)


    logging.info("Video Sucessfully Downloaded ✅")
    return title
