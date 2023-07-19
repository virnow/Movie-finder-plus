import requests
import random

def download_with_progress(url):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    file_name = url.split('/')[-1]
    file_size = int(response.headers.get('content-length', 0))
    chunk_size = 8192
    downloaded_size = 0
    print("\033[1;34;40m","Downloading: " + file_name,"\033[0m")
    print("\033[1;32;40m","Size: " + str(file_size // 1024 // 1024) + " MB","\033[0m")
    with open(file_name, "wb") as file:
        for chunk in response.iter_content(chunk_size=chunk_size):
            if chunk:
                file.write(chunk)
                downloaded_size += len(chunk)
                progress = int(downloaded_size / file_size * 100)
                print("\033[1;"+str(random.randint(31,37))+";40m",f"Download progress: {progress}%","\033[0m", end="\r")
    return file_name
