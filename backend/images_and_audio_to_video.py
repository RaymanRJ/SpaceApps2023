"""
Convert a set of image files and an audio file into a video file.

Usage:
    python images_and_audio_to_video.py input_image_folder input_audio_file output_video_name [--image_format image_format] [--fps fps] [--audio_format audio_format]

Arguments:
    input_image_folder (str): Path to the folder containing the image files.
    input_audio_file (str): Path to the input audio file.
    output_video_name (str): Name of the output video file.

Optional Arguments:
    --image_format (str): File format of the input images. Default is png.
    --fps (int): Frame rate of the output video. Default is 24 fps.
    --audio_format (str): File format of the input audio. Default is mp3.

Example:
    python images_and_audio_to_video.py assets input_audio.mp3 output_video.mp4 --fps 30
"""


import argparse
from glob import glob

import moviepy.editor as mp


def images_and_audio_to_video(
    input_image_folder,
    output_video_name,
    input_audio_file,
    image_format,
    fps,
    audio_format,
):
    images = sorted(glob(f"{input_image_folder}/*.{image_format}"))

    video = mp.ImageSequenceClip(images, fps=fps)

    video.to_videofile(
        output_video_name,
        fps=fps,
        audio=input_audio_file,
        temp_audiofile=input_audio_file.replace(f".{audio_format}", ".m4a"),
        remove_temp=True,
        codec="libx264",
        audio_codec="aac",
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert a set of PNG image files and an audio file into a video file."
    )
    parser.add_argument(
        "input_image_folder",
        type=str,
        help="Path to the folder containing the PNG image files.",
    )
    parser.add_argument(
        "input_audio_file", type=str, help="Path to the input audio file."
    )
    parser.add_argument(
        "output_video_name", type=str, help="Name of the output video file."
    )
    parser.add_argument(
        "--image_format",
        type=str,
        default="png",
        help="File format of the input images. Default is png.",
    )
    parser.add_argument(
        "--fps",
        type=int,
        default=24,
        help="Frame rate of the output video. Default is 24 fps.",
    )
    parser.add_argument(
        "--audio_format",
        type=str,
        default="mp3",
        help="File format of the input audio. Default is mp3.",
    )
    args = parser.parse_args()

    images_and_audio_to_video(
        args.input_image_folder,
        args.output_video_name,
        args.input_audio_file,
        args.image_format,
        args.fps,
        args.audio_format,
    )
