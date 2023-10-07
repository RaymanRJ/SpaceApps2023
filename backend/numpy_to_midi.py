from typing import Tuple

import numpy as np
from mido import MidiFile, MidiTrack, Message


# Create a 5x5 RGB image (uint8 datatype by default)
# pretend_picture = np.random.randint(0, 256, (5, 5, 3), dtype=np.uint8)
# pretend_picture = np.full((5, 5, 3), [128, 64, 32], dtype=np.uint8)
NUM_TRACKS = 10
picture_tests = [
    np.random.randint(0, 256, (5, 5, 3), dtype=np.uint8) for _ in range(NUM_TRACKS)
]


midi_path = "midi.mid"


def rms_algorithm(picture: np.ndarray) -> Tuple[int, int, int]:
    rows, cols, colors = picture.shape
    r_note = 0
    g_note = 0
    b_note = 0

    for row in range(rows):
        for col in range(cols):
            r, g, b = picture[row, col]

            r_note += r ** 2
            g_note += g ** 2
            b_note += b ** 2

    r_note = np.sqrt(r_note / (rows * cols))
    g_note = np.sqrt(g_note / (rows * cols))
    b_note = np.sqrt(b_note / (rows * cols))

    return int(r_note * 127 / 255), int(g_note * 127 / 255), int(b_note * 127 / 255)


def average_algorithm(picture: np.ndarray) -> Tuple[int, int, int]:
    rows, cols, colors = picture.shape
    r_note = 0
    g_note = 0
    b_note = 0
    for row in range(rows):
        for col in range(cols):
            r, g, b = picture[row, col]

            r_note += int(r * 127 / 255)  # Map 0-255 to 0-127
            g_note += int(g * 127 / 255)  # Map 0-255 to 0-127
            b_note += int(b * 127 / 255)  # Map 0-255 to 0-127

    r_note /= (rows * cols)
    g_note /= (rows * cols)
    b_note /= (rows * cols)

    r_note = int(r_note)
    g_note = int(g_note)
    b_note = int(b_note)

    return r_note, g_note, b_note


def handler(picture: np.ndarray, file_path: str) -> str:
    # Create a new MIDI file with one track
    mid = MidiFile(type=1)

    r_track = MidiTrack()
    g_track = MidiTrack()
    b_track = MidiTrack()

    r_track.name = "Red"
    g_track.name = "Green"
    b_track.name = "Blue"
    
    mid.tracks = [r_track, g_track, b_track]

    r_note, g_note, b_note = average_algorithm(picture)

    print(r_note, g_note, b_note)

    # r_note, g_note, b_note = rms_algorithm(picture)
    print(r_note, g_note, b_note)

    # Add note-on messages
    r_track.append(Message('note_on', note=r_note, velocity=64, time=0))
    g_track.append(Message('note_on', note=g_note, velocity=64, time=0))
    b_track.append(Message('note_on', note=b_note, velocity=64, time=0))

    # Add note-off messages immediately (time=0)
    r_track.append(Message('note_off', note=r_note, velocity=64, time=500))
    g_track.append(Message('note_off', note=g_note, velocity=64, time=500))
    b_track.append(Message('note_off', note=b_note, velocity=64, time=500))

    # Add a delay message to separate this set of notes from the next
    # track.append(Message('control_change', control=0, value=0, time=500))

    mid.save(file_path)
    return file_path


if __name__ == "__main__":
    for i, pretend_picture in enumerate(picture_tests):
        path = f"midi_{i}.mid"
        handler(pretend_picture, path)