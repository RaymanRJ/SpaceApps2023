import os
from typing import List

import cv2
import numpy as np
import pandas as pd

photo_path = "./assets/"


def list_files(dir: str) -> List[str]:
    return os.listdir(dir)


def process_photo(file_path: str) -> np.ndarray:
    return cv2.imread(file_path)


def main():
    files = list_files(photo_path)
    for file in files[:1]:
        photo = process_photo(os.path.join(photo_path, file))


        df = pd.DataFrame(photo[:, :, 0])

        # df = pd.DataFrame({('R', i, j): photo[i, j, 2] for i in range(photo.shape[0]) for j in range(photo.shape[1])})
        # df['G'] = pd.DataFrame({(i, j): photo[i, j, 1] for i in range(photo.shape[0]) for j in range(photo.shape[1])})
        # df['B'] = pd.DataFrame({(i, j): photo[i, j, 0] for i in range(photo.shape[0]) for j in range(photo.shape[1])})


        print(df)
        df.to_csv("image1.csv")


if __name__ == "__main__":
    main()