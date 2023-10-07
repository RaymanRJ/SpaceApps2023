import os
from typing import List

import cv2
import numpy as np

photo_path = "./assets/"


def list_files(dir: str) -> List[str]:
    return os.listdir(dir)


def process_photo(file_path: str) -> np.ndarray:
    return cv2.imread(file_path)


def main():
    files = list_files(photo_path)
    print(files)
    for file in files:
        photo = process_photo(os.path.join(photo_path, file))


if __name__ == "__main__":
    main()