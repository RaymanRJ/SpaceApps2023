import cv2
import numpy as np
import simpleaudio as sa

video_path = "../videos/Flight Through the Orion Nebula in Visible and Infrared Light [Ultra HD].mp4"

# Function to generate sound based on frame
def generate_sound(frame):
    # Calculate the average brightness of the frame
    avg_brightness = frame.mean()
    # Map the brightness to a frequency range (e.g., 200 to 800 Hz)
    frequency = np.interp(avg_brightness, [0, 255], [200, 800])

    fs = 44100  # 44100 samples per second
    seconds = 1  # Note duration of 1 second
    t = np.linspace(0, seconds, seconds * fs, False)  # Generate array with seconds*fs steps
    note = 0.5 * np.sin(frequency * 2 * np.pi * t)  # Generate sine wave of given frequency
    audio = note * (2 ** 15 - 1) / np.max(np.abs(note))  # Normalize to 16-bit range
    audio = audio.astype(np.int16)  # Convert to 16-bit PCM format
    return audio

def main(video_path):
    # Load the video
    cap = cv2.VideoCapture(video_path)

    # Check if video opened successfully
    if not cap.isOpened():
        print("Error: Could not open video.")
        exit()

    # Loop through video frame by frame
    while cap.isOpened():
        ret, frame = cap.read()  # Read the next frame
        if not ret:
            break  # Break the loop if we reach the end of the video

        audio = generate_sound(frame)  # Generate sound for the current frame
        play_obj = sa.play_buffer(audio, 1, 2, 44100)  # Play the generated sound
        play_obj.wait_done()  # Block until sound is finished playing

    # Release the video capture object
    cap.release()

# Call the main function with your video file path
main(video_path)
