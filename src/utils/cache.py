import os


def clear_cache(folders, file_name):
    for folder in folders:
        for file in os.listdir(f"src/data/{folder}"):
            if file[:-4] == file_name:
                os.remove(f"src/data/{folder}/{file}")


def check_cache(folder, filename):
    for file in os.listdir(folder):
        if file[:-4] == filename:
            return True

    return False
