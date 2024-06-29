import cv2
import numpy as np
from os import listdir
from os.path import isfile, join
from concurrent.futures import ThreadPoolExecutor, as_completed

# Directory containing your cards
my_path = 'my_images/'

# Directory containing database of dokkan images
all_path = 'all_images/'

# List of files in the directory containing your cards
my_files = [f for f in listdir(my_path) if isfile(join(my_path, f))]

# List of files in the directory containing database of dokkan images
all_files = [f for f in listdir(all_path) if isfile(join(all_path, f))]

# ORB (Feature) Detector
orb = cv2.ORB_create()

# BFMatcher with default parameters
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Function to match each card in my_path to a card in all_path
def find_best_match(file):
    # Define the path to the main image
    main_image_path = join(my_path, file)
    # Read the main image in grayscale
    img_rgb = cv2.imread(main_image_path, 0)
    
    # Detect keypoints and descriptors in the main image
    kp1, des1 = orb.detectAndCompute(img_rgb, None)
    
    # Initialize variables to store the best match and best score
    best_match = None
    best_score = float('inf')

    # Iterate over all template images in the database
    for template in all_files:
        # Define the path to the template image
        template_image_path = join(all_path, template)
        # Extract the template number from the filename
        template_number = int(template.replace('.png', ''))
        # Read the template image in grayscale
        template_img = cv2.imread(template_image_path, 0)
        
        # Detect keypoints and descriptors in the template image
        kp2, des2 = orb.detectAndCompute(template_img, None)
        
        if des2 is not None:
            # Match descriptors between the main image and the template image
            matches = bf.match(des1, des2)
            # Sort matches by distance (best matches first)
            matches = sorted(matches, key=lambda x: x.distance)
            
            # Calculate a score based on the average distance of the matches
            if matches:
                score = np.mean([m.distance for m in matches])
                # Update the best match if the current score is lower than the best score
                if score < best_score:
                    best_score = score
                    best_match = template_number

    # Print and return the best match for the current file
    if best_match is not None:
        print(f"Best match for {file}: Template {best_match} with score {best_score}")
        return {file: best_match}
    else:
        print(f"No good match found for {file}")
        return {file: None}

# List to store the match results
MATCH = []

# Use ThreadPoolExecutor to parallelize processing
with ThreadPoolExecutor() as executor:
    # Submit a job for each file in my_files to the executor
    futures = [executor.submit(find_best_match, file) for file in my_files]
    # Collect the results as they are completed
    for future in as_completed(futures):
        MATCH.append(future.result())

# Write the match results to a text file
with open('matches.txt', 'w+') as f:
    for line in MATCH:
        f.write(f"{line}\n")
