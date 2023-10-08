from glob import glob

import cv2
import numpy as np

from images_and_audio_to_video import images_and_audio_to_video
from midi_to_audio import midi_to_mp3, stitch_midis
from numpy_to_midi import sequence_to_midis
from segment import segment_files

photo_path = "assets"


def process_photo(file_path: str) -> np.ndarray:
    return cv2.imread(file_path)


def main():
    files = sorted(glob(f"{photo_path}/*.png"))
    print(files)

    sequence = segment_files(files)
    print(f"Sequence length: {len(sequence)}")

    midi_files = sequence_to_midis(sequence)
    print(f"MIDI files length: {len(midi_files)}")

    midis = stitch_midis(midi_files, "outputs/stitch_midis.mid")
    print(f"Stitched MIDI length: {len(midis)}")

    audio = midi_to_mp3(midis, "outputs/midis_to_wav.wav", "outputs/wav_to_mp3.mp3")
    print(f"Final MP3: {audio}")

    video = images_and_audio_to_video(
        photo_path,
        "outputs/output_video.mp4",
        audio,
        "png",
        30,
        "mp3",
    )
    print(f"Final video: {video}")


if __name__ == "__main__":
    main()
