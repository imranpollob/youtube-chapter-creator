import moviepy.editor
import os
import re


def convert(seconds):
    hours = seconds // 3600
    seconds %= 3600
    mins = seconds // 60
    seconds %= 60
    return f"{hours:02}:{mins:02}:{seconds:02}"


def video_duration(file_dir):
    video = moviepy.editor.VideoFileClip(file_dir)
    return video.duration


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


def is_video_file(file_name):
    video_formats = [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm", ".3gp", ".3g2"]
    return any(file_name.endswith(format) for format in video_formats)


def get_video_list(directory):
    video_list = []
    for root, dirs, files in os.walk(directory):
        print(f"Directory: {root}")
        video_list = [file for file in files if is_video_file(file)]
        # Sort files based on extracted numbers, handling all the listed naming conventions
        video_list = sorted(
            video_list,
            key=lambda i: (
                extract_number(i) if extract_number(i) is not None else float("inf")
            ),
        )
    return video_list


if __name__ == "__main__":
    directory = input("Please enter the directory path: ")
    video_list = get_video_list(directory)

    with open("result.txt", "w") as result:
        total_time = 0
        for video in video_list:
            if extract_number(video) is not None:
                duration = video_duration(os.path.join(directory, video))
                ceiled_total_time = int(total_time)
                print(f"{convert(ceiled_total_time)} {video}")
                result.write(f"{convert(ceiled_total_time)} {video}\n")
                total_time += duration
