from PIL import Image
import numpy as np
import os

def split_image_to_blocks(image_path, block_size):
    img = Image.open(image_path)
    img_width, img_height = img.size
    
    # Calculate the number of blocks horizontally and vertically
    x_blocks = img_width // block_size     # num of blocks in row
    y_blocks = img_height // block_size    # num of blocks in column 
    
    # Create a list to store the blocks
    blocks = []
    
    # Iterate over each block position
    for y in range(y_blocks):
        for x in range(x_blocks):
            # Define the coordinates of the current block
            left = x * block_size
            upper = y * block_size
            right = left + block_size
            lower = upper + block_size
            
            # Crop the block from the image
            block = img.crop((left, upper, right, lower))
            
            # Convert the block to a NumPy array and append to the list
            block_array = np.array(block)
            blocks.append(block_array)
    
    # Convert the list of blocks to a NumPy array
    blocks_array = np.array(blocks)
    
    return blocks_array

# Set paths and block size
image_dir = 'reconstructed/frames_qp22'
block_size = 24

# Initialize a list to store all blocks from all images
all_blocks = []

# Process each image in the directory
for filename in os.listdir(image_dir):
   # if filename.endswith('.png'):  # Assuming the images are PNG
        image_path = os.path.join(image_dir, filename)
        blocks_array = split_image_to_blocks(image_path, block_size)
        all_blocks.append(blocks_array)
        print(f'Processed {filename}, resulting array shape: {blocks_array.shape}')

# Optionally, convert the list of all blocks to a NumPy array
all_blocks_array = np.array(all_blocks)
print(f'Total number of images processed: {len(all_blocks)}')
print(f'Final array shape: {all_blocks_array.shape}')