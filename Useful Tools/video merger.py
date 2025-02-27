# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 13:49:59 2025

@author: claud
"""

import cv2
import os

# Set the desktop path
desktop_path = 'C:/Users/claud/OneDrive/Desktop'
os.chdir(desktop_path)

# Paths to the input videos
input_video_path_1 = 'C:/Users/claud/OneDrive/Desktop/X_3.mp4'  # First video
input_video_path_2 = 'C:/Users/claud/OneDrive/Desktop/X_4.mp4'  # Second video

# Output video path
output_video_path = 'C:/Users/claud/OneDrive/Desktop/X_1.mp4'

# Open the first video
cap1 = cv2.VideoCapture(input_video_path_1)

# Get the video information (width, height, FPS)
frame_width1 = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height1 = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps1 = cap1.get(cv2.CAP_PROP_FPS)

# Open the second video
cap2 = cv2.VideoCapture(input_video_path_2)

# Get the video information (width, height, FPS)
frame_width2 = int(cap2.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height2 = int(cap2.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps2 = cap2.get(cv2.CAP_PROP_FPS)

# Set the codec for the output video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# Create the VideoWriter for the output (set the width and height)
output_width = max(frame_width1, frame_width2)  # Use the wider width
output_height = max(frame_height1, frame_height2)  # Use the taller height
out = cv2.VideoWriter(output_video_path, fourcc, min(fps1, fps2), (output_width, output_height))

# Write the frames of the first video to the output
while cap1.isOpened():
    ret1, frame1 = cap1.read()
    if not ret1:
        break

    # Resize frame1 if necessary (in case of different heights/widths)
    if frame_height1 != output_height or frame_width1 != output_width:
        frame1 = cv2.resize(frame1, (output_width, output_height))

    # Write the frame of the first video
    out.write(frame1)

    # Show the frame (optional)
    cv2.imshow('Merged Video', frame1)
    
    # Press 'q' to exit the preview
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Now write the frames of the second video to the output
while cap2.isOpened():
    ret2, frame2 = cap2.read()
    if not ret2:
        break

    # Resize frame2 if necessary (in case of different heights/widths)
    if frame_height2 != output_height or frame_width2 != output_width:
        frame2 = cv2.resize(frame2, (output_width, output_height))

    # Write the frame of the second video
    out.write(frame2)

    # Show the frame (optional)
    cv2.imshow('Merged Video', frame2)
    
    # Press 'q' to exit the preview
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the objects and close the windows
cap1.release()
cap2.release()
out.release()
cv2.destroyAllWindows()

