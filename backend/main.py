from glob import glob

from images_and_audio_to_video import images_and_audio_to_video
from midi_to_audio import midi_to_mp3, stitch_midis
from numpy_to_midi import sequence_to_midis
from segment import average_files

photo_path = "assets"


def main():
    files = sorted(glob(f"{photo_path}/*.png"))
    print(files)

    averaged_photos = average_files(files)
    print(f"Averaged photos length: {len(averaged_photos)}")

    midi_files = sequence_to_midis(averaged_photos)
    print(f"MIDI files length: {len(midi_files)}")

    midis = stitch_midis(midi_files, "outputs/stitch_midis.mid")
    print(f"Stitched MIDI length: {len(midis)}")

    audio = midi_to_mp3(midis, "outputs/midis_to_wav.wav", "outputs/wav_to_mp3.mp3")
    print(f"Final MP3: {audio}")

    video = images_and_audio_to_video(
        photo_path,
        "outputs/output_video.mp4",
        audio,
        "png",
        30,
        "mp3",
    )
    print(f"Final video: {video}")


if __name__ == "__main__":
    main()
