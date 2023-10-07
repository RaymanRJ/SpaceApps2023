import subprocess
from pydub import AudioSegment
from typing import List
from mido import MidiFile, MidiTrack, Message

from backend.numpy_to_midi import NUM_TRACKS


def stitch_midis(midi_files: List[str], midi_file_path: str) -> str:
    """Stitch together a list of midi files into one midi file."""

    stitched_midi = MidiFile(midi_files[0])
    tracks = {track.name for track in stitched_midi.tracks}
    track_length = sum(msg.time for msg in stitched_midi.tracks[0])   # Expectation: Every track has the same length
    track_offset = track_length
    for midi in midi_files[1:]:
        current_midi = MidiFile(midi)

        for track in current_midi.tracks:
            new_track = MidiTrack()
            new_track.name = track.name
            for msg in track:
                if not msg.is_meta:
                    msg.time += track_offset
                new_track.append(msg)
            stitched_midi.tracks.append(new_track)

        track_offset += track_length
    stitched_midi.save(midi_file_path)

    return midi_file_path


def midi_to_mp3(midi_file: str, mp3_file: str) -> str:

    soundfont = "PC-98_Soundfont.sf2"
    # Step 1: Convert MIDI to WAV using FluidSynth
    # Replace 'soundfont.sf2' with the path to your specific SoundFont file
    subprocess.run(['fluidsynth', '-ni', soundfont, midi_file, '-F', 'output.wav', '-r', '44100'])

    # Step 2: Convert WAV to MP3 using pydub
    audio = AudioSegment.from_wav("output.wav")
    audio.export(mp3_file, format="mp3")

    return mp3_file


if __name__ == "__main__":
    midi_files = []
    for _ in range(NUM_TRACKS):
        midi_files = [f"midi_{i}.mid" for i in range(NUM_TRACKS)]

    midi = stitch_midis(midi_files, "stitch_test.mid")
    mp3 = midi_to_mp3(midi, "stitch_test.mp3")



