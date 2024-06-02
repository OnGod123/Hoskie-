

import os
import ffmpeg

def save_video_with_quality(input_file_path, output_file_path):
    """
    Save the video with its quality preserved using ffmpeg.
    
    Args:
    input_file_path (str): Path to the input video file.
    output_file_path (str): Path to the output video file.
    """
    try:
        ffmpeg.input(input_file_path).output(output_file_path).run(overwrite_output=True)
        print(f"Video saved successfully at {output_file_path}")
    except ffmpeg.Error as e:
        print(f"An error occurred: {e.stderr.decode()}")
        raise

