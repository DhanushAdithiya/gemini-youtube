import os
import logging
import argparse

from src.utils.video_offloader import offload_video
from src.utils.transcribe_video import transcribe_audio
from src.utils.cache import clear_cache

from src.models.text_processing import text_processing
from src.models.summarizer import summarize_content


def main():
    parser = argparse.ArgumentParser(description="Youtube Video Summarization")
    parser.add_argument("--video_url", type=str, required=True, help="Pass the youtube video link here")
    parser.add_argument("--cache",type=bool ,required=False, help="This is used to clear the transcription cache")
    args = parser.parse_args()

    directories = ["video", "transcription"]
    for d in directories:
        if not os.path.exists(f"src/data/{d}"):
            os.makedirs(f"src/data/{d}")


    file_name = offload_video(args.video_url)
    transcribe_audio(f"./src/data/video/{file_name}.mp3", file_name)
    summarize_content(f"./src/data/transcription/{file_name}.txt", filename=file_name)
    clear_cache(file_name, args.cache)

if __name__ == "__main__":
    main()
    