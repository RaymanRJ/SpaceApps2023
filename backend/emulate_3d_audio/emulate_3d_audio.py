import os
import platform
from pathlib import Path
from pydub import AudioSegment

PLATFORM_NAME = platform.system()
CURRENT_PATH = Path(__file__).parent
INPUT_FOLDER = CURRENT_PATH / "Test Data"

def main():

    #Should create temporary environmental variable for any system
    if PLATFORM_NAME == 'Windows':
        os.environ["PATH"] += os.pathsep + str(Path(path_to_ffmpeg()).parent)
    else:
        os.environ["LD_LIBRARY_PATH"] += ":" + str(Path(path_to_ffmpeg()).parent)
    
    #Read in 5 audio tracks
    song1 = AudioSegment.from_file(INPUT_FOLDER / "la.mp3", format="mp3")
    song2 = AudioSegment.from_file(INPUT_FOLDER / "mi.mp3", format="mp3")
    song3 = AudioSegment.from_file(INPUT_FOLDER / "re.mp3", format="mp3")
    song4 = AudioSegment.from_file(INPUT_FOLDER / "si.mp3", format="mp3")
    song5 = AudioSegment.from_file(INPUT_FOLDER / "sol.mp3", format="mp3")

    #Introduce pan based on column the mp3 represents
    #1 - left, 2 - centre-left, 3 - centre, 4 - centre-right, 5 - right
    song1 = song1.pan(-1)
    song2 = song2.pan(-0.5)
    song4 = song4.pan(+0.5)
    song5 = song5.pan(+1)

    overlay = song1.overlay(
        song2, position=0).overlay(
        song3, position=0).overlay(
        song4, position=0).overlay(
        song5, position=0)

    #Overlay all mp3s into 1
    overlay.export(CURRENT_PATH.parent / "outputs/mashup.mp3", format="mp3")


def path_to_ffmpeg():
    #get path to ffmpeg
    SCRIPT_DIR = Path(__file__).parent 
    if PLATFORM_NAME == 'Windows':
        return str(Path(SCRIPT_DIR, "win", "ffmpeg", "ffmpeg.exe"))
    elif PLATFORM_NAME == 'Darwin':
        return str(Path(SCRIPT_DIR, "mac", "ffmpeg", "ffmpeg"))
    else:
        return str(Path(SCRIPT_DIR, "linux", "ffmpeg", "ffmpeg"))

main()
