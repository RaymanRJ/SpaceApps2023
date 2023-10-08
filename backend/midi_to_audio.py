import subprocess
from typing import List

from mido import MidiFile, MidiTrack
from pydub import AudioSegment

from numpy_to_midi import NUM_TRACKS

import fluidsynth


def get_track_pixel_name(track_name: str) -> str:
    # Track names are: color_photo_pixel (color_photo_row_column)
    # Remove the photo portion

    base_track_name = track_name.split("_")

    return "_".join(base_track_name[0:2] + base_track_name[3:])

    print(track_name)
    return "_".join(track_name.split("_")[0:2])


def stitch_midis(midi_files: List[str], midi_file_path: str) -> str:
    # At this point, each midi_file contains all data for each photo
    # All track names are: color_photo_pixel (color_photo_row_column)
    # We need to stitch the tracks together by pixel (row, column)


    stitched_midi = MidiFile(midi_files[0])
    for track in stitched_midi.tracks:
        track.name = get_track_pixel_name(track.name)
    track_dict = {track.name: track for track in stitched_midi.tracks}
    track_length = sum(msg.time for msg in stitched_midi.tracks[0])
    track_offset = track_length

    for midi in midi_files[1:]:
        current_midi = MidiFile(midi)
        for track in current_midi.tracks:
            track_name = get_track_pixel_name(track.name)
            if track_name in track_dict:
                target_track = track_dict[track_name]
            else:
                target_track = MidiTrack()
                target_track.name = track_name
                stitched_midi.tracks.append(target_track)
                track_dict[track_name] = target_track

            for msg in track:
                # if not msg.is_meta:
                #     msg.time += track_offset
                target_track.append(msg)

        track_offset += track_length

    stitched_midi.save(midi_file_path)
    return midi_file_path


def midi_to_mp3(midi_file: str, wav_file: str, mp3_file: str) -> str:
    # soundfont = "./soundfonts/SuperMarioWorld.sf2"
    soundfont = "./soundfonts/PC-98_Soundfont.sf2"

    # Step 1: Convert MIDI to WAV using FluidSynth
    # Replace 'soundfont.sf2' with the path to your specific SoundFont file
    process = subprocess.run(
        ["fluidsynth", "-ni", soundfont, midi_file, "-F", wav_file, "-r", "44100"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    print(process)

    # Step 2: Convert WAV to MP3 using pydub
    sound = AudioSegment.from_wav(wav_file)

    normalized_sound = sound.normalize(headroom=0.1)
    normalized_sound.export("outputs/midis_to_wav_normalized.wav", format="wav")

    faded_sound = sound.fade_in(1).fade_out(1)
    faded_sound.export("outputs/midis_to_wav_faded.wav", format="wav")

    faded_sound.export(mp3_file, format="mp3")

    return mp3_file


if __name__ == "__main__":
    midi_files = []
    for _ in range(NUM_TRACKS):
        midi_files = [f"midi_{i}.mid" for i in range(NUM_TRACKS)]

    midi = stitch_midis(midi_files, "stitch_test.mid")
    mp3 = midi_to_mp3(midi, "stitch_test.mp3")


