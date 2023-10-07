import numpy as np
import pandas as pd


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


def save_to_numpy(array):
    np.save("Video_colors", array, allow_pickle=True)
    test = np.load("Video_colors.npy")
    return