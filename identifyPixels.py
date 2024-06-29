import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# Load the image
image_path = 'app_images/1.png'  # Replace with your image path
img = mpimg.imread(image_path)

# Crop the image 
# top_pixel = 560
# bottom_pixel = 2065
# img = img[top_pixel:bottom_pixel,:]

# Create a plot to display the image
fig, ax = plt.subplots(figsize=(12, 8),constrained_layout=True)
ax.imshow(img)

# Function to print the pixel coordinates
def on_move(event):
    if event.inaxes:
        x, y = int(event.xdata), int(event.ydata)
        if 0 <= x < img.shape[1] and 0 <= y < img.shape[0]:
            print(f'Pixel number: ({x}, {y})')

# Connect the motion_notify_event to the function
fig.canvas.mpl_connect('motion_notify_event', on_move)

plt.show()
