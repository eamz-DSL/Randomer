# Random Image Selector

## Overview
This Python script is designed to randomly select a specified number of images from a given folder and copy them to another folder. It provides a simple solution for users who need to quickly select a subset of images for various purposes.

## Requirements
- Python 3.x
- `os` module
- `random` module
- `shutil` module

## Usage
1. Ensure you have Python installed on your system.
2. Download the script (`random_image_selector.py`) to your desired location.
3. Open a terminal or command prompt.
4. Navigate to the directory where the script is saved.
5. Run the script by executing the command: `python random_image_selector.py`
6. You will be prompted to input the source folder path in the console.
7. After entering the source folder path, the script will select a specified number of random images from the folder.
8. The selected images will be copied to a new folder named "selected_images" within the provided source folder path.

## Customization
- You can change the default number of images to be selected by modifying the `num_images` variable in the script.

## Example
```
$ python random_image_selector.py
Enter the source folder path: /path/to/source_folder
2222 images copied to '/path/to/source_folder/selected_images'.
```

## Note
- This script currently supports image files with extensions `.jpg`, `.jpeg`, `.png`, and `.gif`.
- If the source folder contains fewer images than the specified number, it will select all available images.

Enjoy randomizing your image collection effortlessly with this script! 📷🔀
