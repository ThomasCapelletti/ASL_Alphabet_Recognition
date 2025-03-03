# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 14:18:04 2025

@author: claud
"""

import os
import numpy as np
from PIL import Image

# Path to the folder containing images
folder_path = './Olddata'

# Lists to store images and labels
images = []
labels = []

# Define the classes
classes = ['D', 'H', 'K', 'S', 'X']

# Sort subfolders in alphabetical order
subfolders = sorted(os.listdir(folder_path))

# Iterate through subfolders (each subfolder corresponds to a letter)
for label in subfolders:
    subfolder_path = os.path.join(folder_path, label)
    
    # Check if it's a directory
    if os.path.isdir(subfolder_path):
        print(f"Analyzing folder: {label}")
        
        # Iterate through files inside the subfolder
        for img_name in sorted(os.listdir(subfolder_path)):
            img_path = os.path.join(subfolder_path, img_name)
            
            # Load the image if it's a valid image file
            if os.path.isfile(img_path) and img_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                # Open the image with PIL
                img = Image.open(img_path)
                
                # Resize the image to 64x64
                img_resized = img.resize((64, 64))
                
                # Convert the image into a NumPy array (formatted as RGB)
                img_array = np.array(img_resized)
                
                # If the image does not have 3 channels (e.g., grayscale), convert it
                if img_array.ndim == 2:  # If it's grayscale
                    img_array = np.stack([img_array] * 3, axis=-1)
                
                # Normalize pixel values to [0, 1]
                img_array = img_array.astype('float32') / 255.0
                
                # Add the image to the list
                images.append(img_array)
                
                # Add the numerical label corresponding to the letter
                labels.append(classes.index(label))
    
    else:
        print(f"{label} is not a valid directory.")

# Convert lists into NumPy arrays
images_array = np.array(images)
labels_array = np.array(labels)

# Save the NumPy arrays as .npy files
np.save('olddata.npy', images_array)
np.save('labels.npy', labels_array)

print("Images and labels have been saved in 'olddata.npy' and 'labels.npy'.")

