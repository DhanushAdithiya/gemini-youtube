import os
import whisper
import logging
from src.utils.cache import check_cache


def transcribe_audio(file_path, filename):

    logging.info("Video Transcirption Started")

    if check_cache(folder="src/data/transcription", filename=filename):
        return 

    model = whisper.load_model("base.en")
    result = model.transcribe(file_path)
    directory = f"./src/data/transcription/{filename}.txt"
    with open(directory, "w+") as f:
        f.write(result["text"])
    
    logging.info("Video Sucessfully Transcribed ✅")