from typing import List

import numpy as np
import pandas as pd
from cv2 import imread


def averaged_pixels(photo: np.array) -> np.ndarray:
    """Takes a photo and returns an array of averaged pixels"""

    df_r = pd.DataFrame(photo[:, :, 0])
    df_g = pd.DataFrame(photo[:, :, 1])
    df_b = pd.DataFrame(photo[:, :, 2])

    # Get image resolution in x and y direction
    y = df_r.shape[0]
    x = df_r.shape[1]

    # Change this array to change the segmentation of the images
    segs = [5, 5]

    # define index ranges for rows
    rows = []
    x_subs = y / segs[0]
    for i in range(segs[0]):
        if i == 0:
            rows.append(list(range(int((x_subs * i) - i), int(x_subs - (i + 1)) + 1)))
        else:
            rows.append(
                list(range(int((x_subs * i) - i) + i, int((x_subs * (i + 1) - 1)) + 1))
            )

    # define index ranges for columns
    cols = []
    y_subs = x / segs[0]
    for i in range(segs[0]):
        if i == 0:
            cols.append(list(range(int((y_subs * i) - i), int(y_subs - (i + 1)) + 1)))
        else:
            cols.append(
                list(range(int((y_subs * i) - i) + i, int((y_subs * (i + 1) - 1)) + 1))
            )

    all_avgs = []
    for x in range(len(rows)):
        row_avgs = []
        for y in range(len(cols)):
            avgs = []
            avgs.append(
                int(
                    (df_r.iloc[rows[x], cols[y]].sum().sum())
                    / (len(rows[x]) * len(cols[y]))
                )
            )
            avgs.append(
                int(
                    (df_g.iloc[rows[x], cols[y]].sum().sum())
                    / (len(rows[x]) * len(cols[y]))
                )
            )
            avgs.append(
                int(
                    (df_b.iloc[rows[x], cols[y]].sum().sum())
                    / (len(rows[x]) * len(cols[y]))
                )
            )
            row_avgs.append(avgs)
        all_avgs.append(row_avgs)

    return np.array(all_avgs)


def save_to_numpy(array):
    np.save("Video_colors", array, allow_pickle=True)
    np.load("Video_colors.npy")


def average_files(files: List[str]) -> List[np.ndarray]:
    averaged_photos = []
    for i, file in enumerate(files):
        print(f"Processing {file}: {i} of {len(files)}")
        photo = imread(file)

        averaged_photo = averaged_pixels(photo)

        averaged_photos.append(averaged_photo)
    return averaged_photos


if __name__ == "__main__":
    test_image = np.random.randint(0, 10, (10, 10, 3), dtype=np.uint8)
    # Print the test image array
    print("Test Image:")
    for i in range(test_image.shape[0]):
        for j in range(test_image.shape[1]):
            print(test_image[i, j], end=' ')
        print()

    # Call the segment_data function
    segmented_data = average_files(test_image)

    # Print the segmented data
    print("Segmented Data:")
    for i in range(segmented_data.shape[0]):
        for j in range(segmented_data.shape[1]):
            print(segmented_data[i, j], end=' ')
        print()