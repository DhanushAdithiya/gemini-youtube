import os
import logging

from src.utils.video_offloader import offload_video
from src.utils.transcribe_video import transcribe_audio
from src.utils.cache import clear_cache

from src.models.text_processing import text_processing
from src.models.summarizer import summarize_content




if __name__ == "__main__":
    directories = ["video", "transcription"]
    for d in directories:
        if not os.path.exists(f"src/data/{d}"):
            os.makedirs(f"src/data/{d}")


    title = offload_video("https://www.youtube.com/watch?v=Bw_12zRkUkY&list=WL&index=100")
    transcribe_audio(f"./src/data/video/{title}.mp3", title)
    summarize_content(f"./src/data/transcription/{title}.txt", filename=title)
    clear_cache(directories, title)