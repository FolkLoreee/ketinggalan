import subprocess
from gtts import gTTS
import time
from playsound import playsound


def start_record():
    time.sleep(0.4)
    v = gTTS("Aku wis miwiti ngrekam", lang="jw")
    v.save("rekaman.mp3")
    playsound("/home/folkloreee/Documents/ketinggalan/rekaman.mp3")
    subprocess.call(
        "rm /home/folkloreee/Documents/ketinggalan/rekaman.mp3", shell=True)
    subprocess.call(
        "ffmpeg -i /dev/video4 -r 60 -t 2 -y video.mp4", shell=True)

    time.sleep(0.4)
    v = gTTS("録音を終了しました", lang="ja")
    v.save("rekaman.mp3")
    playsound("/home/folkloreee/Documents/ketinggalan/rekaman.mp3")
    subprocess.call(
        "rm /home/folkloreee/Documents/ketinggalan/rekaman.mp3", shell=True)

    subprocess.call(
        "vlc /home/folkloreee/Documents/ketinggalan/video.mp4", shell=True)


if __name__ == "__main__":
    start_record()
