import os
from typing import List
import cv2

from Segment import *
from numpy_to_midi import *

photo_path = "./assets"


def list_files(dir: str) -> List[str]:
    return os.listdir(dir)


def process_photo(file_path: str) -> np.ndarray:
    return cv2.imread(file_path)


def main():
    sequence = []
    files = list_files(photo_path)
    for file in files[:10]:
        if file.endswith(".png"):
            photo = process_photo(os.path.join(photo_path, file))

            sequence.append(segment_data(photo))

    # save_to_numpy(full_array)

    for frame in range(len(sequence[:10])):
        data = sequence[frame].reshape(5, 5, 3)
        midi_generator(data, f"./midi/frame-{frame + 1}_midi.mid")


if __name__ == "__main__":
    main()