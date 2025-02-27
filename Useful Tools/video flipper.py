# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 13:32:32 2025

@author: claud
"""

import cv2
import os

# Set the directory path
desktop_path = 'C:/Users/claud/OneDrive/Desktop'
os.chdir(desktop_path)

# Full paths for the videos
input_video_path = 'C:/Users/claud/OneDrive/Desktop/X_1.mp4'  # Full path of the input video
output_video_path = 'C:/Users/claud/OneDrive/Desktop/X_1.mp4'  # Full path of the output video

# Open the input video
cap = cv2.VideoCapture(input_video_path)

# Get video information (width, height, FPS)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Set the codec for the output video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use 'XVID' for .avi format
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Mirror the frame horizontally
    mirrored_frame = cv2.flip(frame, 1)

    # Write the mirrored frame to the output video
    out.write(mirrored_frame)

    # Display the frame (optional)
    cv2.imshow('Mirrored Video', mirrored_frame)
    
    # Stop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the objects and close the windows
cap.release()
out.release()
cv2.destroyAllWindows()


