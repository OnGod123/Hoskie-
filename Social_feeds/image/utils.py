# utils.py

import os
import ffmpeg

def save_image_with_quality(input_file_path, output_file_path):
    """
    Save the image with its quality preserved using ffmpeg.
    
    Args:
    input_file_path (str): Path to the input image file.
    output_file_path (str): Path to the output image file.
    """
    try:
        ffmpeg.input(input_file_path).output(output_file_path).run(overwrite_output=True)
        print(f"Image saved successfully at {output_file_path}")
    except ffmpeg.Error as e:
        print(f"An error occurred: {e.stderr.decode()}")
        raise

