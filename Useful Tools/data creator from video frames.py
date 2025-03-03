import os
import numpy as np
import cv2
from PIL import Image
import random

def process_video_to_images(video_path, label, train_folder, test_folder):
    """
    Extract frames from a video and save them as image files in a labeled folder structure.

    :param video_path: Path to the input .mp4 video
    :param label: Label associated with each frame (e.g., alphabet letter from file name)
    :param train_folder: Folder to save training frames
    :param test_folder: Folder to save testing frames (1 frame per label)
    """
    try:
        video_capture = cv2.VideoCapture(video_path)

        if not video_capture.isOpened():
            print(f"Error: Unable to open video {video_path}")
            return

        frame_count = 0
        frames = []

        # Read all frames from the video
        while True:
            ret, frame = video_capture.read()
            if not ret:
                break

            # Convert the frame to RGB and resize
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_image = Image.fromarray(frame_rgb).resize((64, 64))
            frames.append(frame_image)

        video_capture.release()

        if len(frames) == 0:
            print(f"No frames found in video {video_path}")
            return

        # Randomly select one frame for the test set
        test_frame_index = random.randint(0, len(frames) - 1)
        test_frame = frames[test_frame_index]

        # Save the test frame
        test_frame_name = f"{label}_test.png"
        test_frame.save(os.path.join(test_folder, test_frame_name))

        # Save the remaining frames in the train set
        train_label_folder = os.path.join(train_folder, label)
        os.makedirs(train_label_folder, exist_ok=True)
        for i, frame in enumerate(frames):
            if i != test_frame_index:
                train_frame_name = f"{label}_{i+1}.png"  # Rename frames as LETTER_number
                frame.save(os.path.join(train_label_folder, train_frame_name))

        print(f"Processed {len(frames)} frames for label {label}, 1 frame saved to test set as {test_frame_name}.")

    except Exception as e:
        print(f"An error occurred while processing the video: {e}")

if __name__ == "__main__":
    video_folder = "./videos"  # Replace with your folder containing videos
    train_output_folder = "./asl_alphabet_train"
    test_output_folder = "./asl_alphabet_test"

    # Create train and test folders
    os.makedirs(train_output_folder, exist_ok=True)
    os.makedirs(test_output_folder, exist_ok=True)

    # Gather all video files and their labels
    video_files = [f for f in os.listdir(video_folder) if f.endswith(".mp4")]
    video_paths = [os.path.join(video_folder, f) for f in video_files]
    labels = [f.split("_")[0] for f in video_files]  # Extract label from filename

    # Process each video
    for video_path, label in zip(video_paths, labels):
        process_video_to_images(video_path, label, train_output_folder, test_output_folder)

    print("Dataset created successfully with one test frame per label and correctly renamed frames.")
