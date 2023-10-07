import os
from typing import List
from tempfile import TemporaryFile
import cv2
import numpy as np
import pandas as pd

photo_path = "C:/Users/tochi/OneDrive/Documents/NASA Space Apps Challenge/Videos/1/"


def list_files(dir: str) -> List[str]:
    return os.listdir(dir)


def process_photo(file_path: str) -> np.ndarray:
    return cv2.imread(file_path)


def segment_data(photo) -> np.ndarray:
    df1 = pd.DataFrame(photo[:, :, 0])
    df2 = pd.DataFrame(photo[:, :, 1])
    df3 = pd.DataFrame(photo[:, :, 2])

    # Get image resolution in x and y direction
    y = df1.shape[0]
    x = df1.shape[1]

    # Change this array to change the segmentation of the images
    segs = [5, 5]

    # define index ranges for rows
    rows = []
    x_subs = y / segs[0]
    for i in range(segs[0]):
        if i == 0:
            rows.append(list(range(int((x_subs * i) - i), int(x_subs - (i + 1)) + 1)))
        else:
            rows.append(list(range(int((x_subs * i) - i) + i, int((x_subs * (i + 1) - 1)) + 1)))

    # define index ranges for columns
    cols = []
    y_subs = x / segs[0]
    for i in range(segs[0]):
        if i == 0:
            cols.append(list(range(int((y_subs * i) - i), int(y_subs - (i + 1)) + 1)))
        else:
            cols.append(list(range(int((y_subs * i) - i) + i, int((y_subs * (i + 1) - 1)) + 1)))

    all_avgs = []
    for x in range(len(rows)):
        for y in range(len(cols)):
            avgs = []
            avgs.append(int((df1.iloc[rows[x], cols[y]].sum().sum()) / (len(rows[x]) * len(cols[y]))))
            avgs.append(int((df2.iloc[rows[x], cols[y]].sum().sum()) / (len(rows[x]) * len(cols[y]))))
            avgs.append(int((df3.iloc[rows[x], cols[y]].sum().sum()) / (len(rows[x]) * len(cols[y]))))
            all_avgs.append(avgs)

    return np.array(all_avgs)


def main():
    full_array = []
    files = list_files(photo_path)
    for file in files:
        photo = process_photo(os.path.join(photo_path, file))

        full_array.append(segment_data(photo))

    # Save output
    np.save("Video_colors", full_array, allow_pickle=True)
    test = np.load("Video_colors.npy")
    print(len(test))


if __name__ == "__main__":
    main()