import os
import logging
import argparse
from datetime import datetime
import yaml

from src.utils.video_offloader import offload_video
from src.utils.transcribe_video import transcribe_audio
from src.utils.cache import clear_cache

from src.models.text_processing import text_processing
from src.models.summarizer import summarize_content
from src.models.summarizer import conversation


def main():
    logfile_name = datetime.now()
    logging.basicConfig(filename=f"src/logs/{logfile_name}.log", level=logging.INFO)
    
    parser = argparse.ArgumentParser(description="Youtube Video Summarization")
    parser.add_argument("--video_url", type=str, required=True, help="Pass the youtube video link here")
    parser.add_argument("--cache",type=bool ,required=False, help="This is used to clear the transcription cache")
    args = parser.parse_args()
    
    directories = ["video", "transcription"]
    for d in directories:
        if not os.path.exists(f"src/data/{d}"):
            os.makedirs(f"src/data/{d}")
    logging.info("Started")
    file_name = offload_video(args.video_url)
    transcribe_audio(f"./src/data/video/{file_name}.mp3", file_name)
    content = summarize_content(f"./src/data/transcription/{file_name}.txt", filename=file_name)
    clear_cache(file_name, args.cache)

    try:
        while True:
            user_input = input("Any Questions? \n")
            conversation(content, user_input)
    except KeyboardInterrupt:
        print("\n Thank you for using the application")

    with open("config.yaml" ,"r") as f:
        config = yaml.safe_load(f);

   
    loc = config["Obsidian"]["vault_location"]
    home_dir = os.path.expanduser("~")
    target = os.path.join(home_dir, loc)
    with  open(f"{target}/{file_name}.md", "w+") as f:
        f.write(content)


    logging.info("Finished")

if __name__ == "__main__":
    main()
    