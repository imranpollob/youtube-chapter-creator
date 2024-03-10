import moviepy.editor
import os
import re

# Ask user for directory input
directory = input("Please enter the directory path: ")


def convert(seconds):
    hours = seconds // 3600
    seconds %= 3600
    mins = seconds // 60
    seconds %= 60
    return f"{hours:02}:{mins:02}:{seconds:02}"


def video_duration(file_dir):
    video = moviepy.editor.VideoFileClip(file_dir)
    return int(video.duration)


def extract_number(file_name):
    # Match numbers at the beginning of the file name, handling various formats
    match = re.search(r"^(\d+)[\s.-]*", file_name)
    if match:
        return int(match.group(1))
    # Special handling for 'lesson' followed by numbers
    match = re.search(r"lesson(\d+)", file_name, re.IGNORECASE)
    if match:
        return int(match.group(1))
    return None  # Default case if no number is found


result = open("result.txt", "a")

for root, dirs, files in os.walk(directory):
    print(f"----------------{root}")
    result.write(f"{root}\n")
    video_list = [file for file in files if file.endswith(".mp4")]
    # Sort files based on extracted numbers, handling all the listed naming conventions
    video_list = sorted(
        video_list,
        key=lambda i: (
            extract_number(i) if extract_number(i) is not None else float("inf")
        ),
    )

    total_time = 0

    for video in video_list:
        if extract_number(video) is not None:  # Process only if a number is successfully extracted
            duration = video_duration(os.path.join(root, video))
            print(f"{convert(total_time)} {video}")
            result.write(f"{convert(total_time)} {video}\n")
            total_time += duration

result.close()
