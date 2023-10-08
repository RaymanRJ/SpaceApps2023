from typing import List, Tuple

import numpy as np
from mido import Message, MidiFile, MidiTrack

# Create a 5x5 RGB image (uint8 datatype by default)
# pretend_picture = np.random.randint(0, 256, (5, 5, 3), dtype=np.uint8)
# pretend_picture = np.full((5, 5, 3), [128, 64, 32], dtype=np.uint8)
NUM_TRACKS = 10
picture_tests = [
    np.random.randint(0, 256, (5, 5, 3), dtype=np.uint8) for _ in range(NUM_TRACKS)
]


midi_path = "midi.mid"


def pixel_to_midi(picture: np.ndarray) -> Tuple[int, int, int]:
    r, g, b = picture

    r_note = int(r * 127 / 255)  # Map 0-255 to 0-127
    g_note = int(g * 127 / 255)  # Map 0-255 to 0-127
    b_note = int(b * 127 / 255)  # Map 0-255 to 0-127

    return r_note, g_note, b_note



def rms_algorithm(picture: np.ndarray) -> Tuple[int, int, int]:
    rows, cols, colors = picture.shape
    r_note = 0
    g_note = 0
    b_note = 0

    for row in range(rows):
        for col in range(cols):
            r, g, b = picture[row, col]

            r_note += r**2
            g_note += g**2
            b_note += b**2

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

    r_note /= rows * cols
    g_note /= rows * cols
    b_note /= rows * cols

    r_note = int(r_note)
    g_note = int(g_note)
    b_note = int(b_note)

    return r_note, g_note, b_note


def midi_generator(picture: List[np.ndarray], file_name: str, file_path: str) -> str:
    tracks = []
    mid = MidiFile(type=1)
    for i, row in enumerate(picture):
        for j, pixel in enumerate(row):

            track_name = f"{file_name}_{i}_{j}"

            r_track = MidiTrack()
            g_track = MidiTrack()
            b_track = MidiTrack()

            r_track.name = f"Red_{track_name}"
            g_track.name = f"Green_{track_name}"
            b_track.name = f"Blue_{track_name}"

            r_note, g_note, b_note = pixel_to_midi(pixel)

            # Add note-on messages
            r_track.append(Message("note_on", note=r_note, velocity=64, time=0))
            g_track.append(Message("note_on", note=g_note, velocity=64, time=0))
            b_track.append(Message("note_on", note=b_note, velocity=64, time=0))

            # Add note-off messages immediately (time=0)
            r_track.append(Message("note_off", note=r_note, velocity=64, time=int(1000 / 30)))
            g_track.append(Message("note_off", note=g_note, velocity=64, time=int(1000 / 30)))
            b_track.append(Message("note_off", note=b_note, velocity=64, time=int(1000 / 30)))

            mid.tracks.append(r_track)
            mid.tracks.append(g_track)
            mid.tracks.append(b_track)

        mid.save(file_path)
    return file_path


def sequence_to_midis(averaged_photos: List[np.ndarray]) -> List[str]:
    midi_files = []
    for i, averaged_photo in enumerate(averaged_photos):
        midi_file = f"midi_{i}"
        midi_file_path = f"midi/{midi_file}.mid"
        midi_files.append(midi_generator(averaged_photo, midi_file, midi_file_path))

    return midi_files

if __name__ == "__main__":
    for i, pretend_picture in enumerate(picture_tests):
        path = f"midi_{i}.mid"
        midi_generator(pretend_picture, path)
