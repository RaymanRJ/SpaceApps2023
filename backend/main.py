import os
from typing import List
import cv2

import numpy as np
from Segment import segment_data
from numpy_to_midi import midi_generator
from midi_to_audio import stitch_midis, midi_to_mp3

photo_path = "./assets"
# photo_path = "./STScI-01EVS1PYMMJ7HR4N6VFSCK6EXH"


def list_files(dir: str) -> List[str]:
    return os.listdir(dir)


def process_photo(file_path: str) -> np.ndarray:
    return cv2.imread(file_path)


def main():
    sequence = []
    files = list_files(photo_path)
    for file in files:
        if file.endswith(".png"):
            print(f"Processing {file}")
            photo = process_photo(os.path.join(photo_path, file))

            sequence.append(segment_data(photo))

    # save_to_numpy(full_array)

    midi_files = []
    for frame in range(len(sequence)):
        data = sequence[frame].reshape(5, 5, 3)
        midi_file_path = f"./midi/frame-{frame + 1}_midi.mid"
        midi_generator(data, midi_file_path)
        midi_files.append(midi_file_path)

    midi = stitch_midis(midi_files, "stitch_test.mid")
    mp3 = midi_to_mp3(midi, "stitch_test.mp3")


if __name__ == "__main__":
    main()