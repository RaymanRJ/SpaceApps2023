from moviepy.editor import VideoFileClip, AudioFileClip
import matplotlib.pyplot as plt
from scipy.io import wavfile
from moviepy.video.io.bindings import mplfig_to_npimage


def overlay(video_file: str, audio_file: str, final_video_file: str) -> str:

    # Load the video and audio files
    video = VideoFileClip(video_file)
    audio = AudioFileClip(audio_file)

    # Convert audio to WAV format for easier processing
    audio.write_audiofile("temp_audio.wav")

    # Read WAV file to get audio data
    sample_rate, audio_data = wavfile.read("temp_audio.wav")

    # Create a function to draw waveform
    def draw_waveform(t):
        fig, ax = plt.subplots()
        duration = int(sample_rate * t)
        ax.plot(audio_data[:duration])
        ax.set_title("Waveform")
        ax.set_xlabel("Sample")
        ax.set_ylabel("Amplitude")
        plt.close(fig)
        return mplfig_to_npimage(fig)

    # Generate video with waveform overlay
    waveform_video = VideoFileClip(duration=video.duration)
    waveform_video = waveform_video.fl(lambda gf, t: draw_waveform(t))

    # Combine original video and waveform video
    final_video = VideoFileClip(video_file).set_audio(audio)
    final_video = final_video.fx(lambda gf, t: gf(t) + waveform_video.get_frame(t))

    # Write the final video
    final_video.write_videofile(final_video_file)

    return final_video
