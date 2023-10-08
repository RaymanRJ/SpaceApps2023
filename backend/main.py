import os
from glob import glob
from typing import List

import cv2
import numpy as np

from images_and_audio_to_video import images_and_audio_to_video
from midi_to_audio import midi_to_mp3, stitch_midis
from numpy_to_midi import midi_generator
from Segment import segment_data

photo_path = "assets"
# photo_path = "./STScI-01EVS1PYMMJ7HR4N6VFSCK6EXH"
# photo_path = "./temp_150"


def process_photo(file_path: str) -> np.ndarray:
    return cv2.imread(file_path)


def main():
    sequence = []
    files = sorted(glob(f"{photo_path}/*.png"))
    print(files)
    for file in files:
        print(f"Processing {file}")
        photo = process_photo(file)

        segmented_data = segment_data(photo)
        print(segmented_data.shape)
        sequence.append(segmented_data)

    # save_to_numpy(full_array)

    midi_files = []
    for frame in range(len(sequence)):
        data = sequence[frame].reshape(5, 5, 3)
        midi_file_path = f"midi/frame-{frame + 1}_midi.mid"
        midi_generator(data, midi_file_path)
        midi_files.append(midi_file_path)

    midis = stitch_midis(midi_files, "outputs/stitch_midis.mid")
    mp3 = midi_to_mp3(midis, "outputs/midis_to_wav.wav", "outputs/wav_to_mp3.mp3")

    images_and_audio_to_video(
        photo_path,
        "outputs/output_video.mp4",
        "outputs/wav_to_mp3.mp3",
        "png",
        30,
        "mp3",
    )


if __name__ == "__main__":
    main()
