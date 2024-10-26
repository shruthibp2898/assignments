import cv2
import numpy as np
import os
import concurrent.futures

# Function to create a binary mask and count pixels
def process_image(file_path):
    # Read the image
    image = cv2.imread(file_path)

    if image is None:
        print(f"Failed to read image: {file_path}")
        return 0  # If the image could not be read, return 0

    # Create a binary mask where all 3 channels are above 200
    mask = np.all(image > 200, axis=-1).astype(np.uint8) * 255

    # Write the mask image as a PNG (lossless)
    mask_file_path = os.path.splitext(file_path)[0] + '_mask.png'
    cv2.imwrite(mask_file_path, mask)

    # Count the number of pixels where the mask is max (255)
    count_max_pixels = np.sum(mask > 0)
    
    return count_max_pixels

def main(image_folder):
    total_count = 0
    image_files = []
    results=[]
    # Walk through the directory and its subdirectories
    for root, _, files in os.walk(image_folder):
        for file in files:
            if file.endswith('.jpg'):
                image_files.append(os.path.join(root, file))
    # import pdb;pdb.set_trace()

    for image in image_files:
        out=process_image(image)
        results.append(out)


    # Sum the counts from all processed images
    total_count = sum(results)

    # Log the total count of pixels where the mask is max
    print(f"Total number of pixels where the mask is max: {total_count}")

if __name__ == "__main__":
    image_folder = r"C:\Users\Shruthi\Downloads\Online-test"  # Specify the folder containing jpg images
    main(image_folder)
