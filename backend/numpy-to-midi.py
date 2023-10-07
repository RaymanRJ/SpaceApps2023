import numpy as np
from mido import MidiFile, MidiTrack, Message


pretend_picture = np.random.randint(0, 256, (5, 5, 3), dtype=np.uint8)
# print(np.array2string(pretend_picture, formatter={'all': lambda x: f'{x: >5}'}))

# def play_midi(file_path: str):

def handler(picture: np.ndarray, file_path: str) -> str:
    # Create a new MIDI file with one track
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

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

            print(r_note, g_note, b_note)

            # Add a note-on message
            track.append(Message('note_on', note=r_note, velocity=64, time=0))
            track.append(Message('note_on', note=g_note, velocity=64, time=0))
            track.append(Message('note_on', note=b_note, velocity=64, time=0))

            # Add a note-off message (here, after 500 ticks)
            track.append(Message('note_off', note=r_note, velocity=64, time=500))
            track.append(Message('note_off', note=g_note, velocity=64, time=500))
            track.append(Message('note_off', note=b_note, velocity=64, time=500))

    mid.save(file_path)
    return file_path



midi_path = "midi.mid"
handler(pretend_picture, midi_path)

print(pretend_picture.shape)