from pydub import AudioSegment

from pydub.playback import play


def clean_mp3(mp3_file: str, output_mp3_file: str) -> str:

    # Load audio file
    sound = AudioSegment.from_mp3(mp3_file)


    # normalized_audio = sound.apply_gain(-10 - sound.dBFS)
    # normalized_audio.export(output_mp3_file, format="mp3")
    # return output_mp3_file

    # Set audio levels below -50 dB to silence
    threshold = -10 # in dB
    filtered_sound = sound._spawn(sound.raw_data, overrides={
        "frame_rate": sound.frame_rate
    }).set_frame_rate(44100)

    # Apply gating to remove noise
    sound = filtered_sound._spawn(filtered_sound.raw_data, overrides={
        "frame_rate": filtered_sound.frame_rate
    }).set_frame_rate(44100)

    # Export the cleaned audio
    sound.export(output_mp3_file, format="mp3")


if __name__ == "__main__":
    # play(AudioSegment.from_mp3("outputs/wav_to_mp3.mp3"))
    clean_mp3("outputs/wav_to_mp3.mp3", "outputs/cleaned_audio.mp3")
    play(AudioSegment.from_mp3("outputs/cleaned_audio.mp3"))