import os
import random
import shutil

def select_and_copy_images(source_folder, destination_folder, num_images):
    # Create destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Get a list of all image files in the source folder
    image_files = [f for f in os.listdir(source_folder) if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

    # Select random images
    selected_images = random.sample(image_files, min(num_images, len(image_files)))

    # Copy selected images to the destination folder
    for image in selected_images:
        src_path = os.path.join(source_folder, image)
        dst_path = os.path.join(destination_folder, image)
        shutil.copy(src_path, dst_path)

    print(f"{num_images} images copied to '{destination_folder}'.")

if __name__ == "__main__":
    source_folder = input("Enter the source folder path: ").strip()
    destination_folder = os.path.join(source_folder, "selected_images")
    num_images = 1234  # Change this number to select a different number of images

    select_and_copy_images(source_folder, destination_folder, num_images)
