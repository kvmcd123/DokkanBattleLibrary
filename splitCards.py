import cv2
import numpy as np
import matplotlib.pyplot as plt
from os import listdir, makedirs
from os.path import isfile, join

# Path to folder containing images of card list
mypath='app_images/'

# Create saving directory if it does not exist
makedirs('my_images/', exist_ok=True)

# Grabs the file name for every image in the folder
all_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

# Iterator for file naming
i=0
# Loop through pictures of dokkan card list
for file in all_files:

    # Define the path to image
    path =mypath+file

    # Reading an image in default mode
    image = cv2.imread(path)

    # Crop the image (iPhone 15 Pro Max)
    image=image[560:2065,:]

    # Define an empty list to store images in
    cells = []
    
    # Define the starting pixel for each row
    start_row_coords = [30, 330, 635, 935, 1235]
    
    # Define the starting pixel for each column
    start_col_coords = [35, 295, 555, 815, 1075]

    # Define height of card
    row_height = 180
    
    # Define width of card
    col_width = 181

    # Loop through each row
    for start_row in start_row_coords:
        # Loop through each column
        for start_col in start_col_coords:
            # Create a new image of a single card by cropping to cards dimensions
            new_image = image[start_row:start_row + row_height, start_col:start_col + col_width]
            # Append the card to list of cards in row
            cells.append(new_image)
    
    # Loop through all cards
    for cell in cells:
        # Define a file name for the card
        fName = './my_images/'+str(i)+'.png'
        # Log the name for a progress update
        print(fName)
        # Save the image
        cv2.imwrite(fName, cell)
        # Update the iterator
        i=i+1