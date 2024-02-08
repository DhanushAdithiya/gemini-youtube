import os


def clear_cache(file_name, clear= False ):
    for file in os.listdir("src/data/video"):
        if file[:-4] == file_name:
            os.remove(f"src/data/video/{file}")
    
    if clear:
        for file in os.listdir("src/data/transcription"):
            if file[:-4] == file_name:
                os.remove(f"src/data/transcription/{file}")


def check_cache(folder, filename):
    for file in os.listdir(folder):
        if file[:-4] == filename:
            return True

    return False
