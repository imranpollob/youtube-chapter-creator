import os
from video import get_video_list

if __name__ == "__main__":
    directory = input("Please enter the directory path: ")
    file_dir = input("Please enter the file directory path: ")

    correct_names = []
    video_list = get_video_list(directory)

    with open(file_dir, "r") as file:
        correct_names = file.readlines()
        correct_names = [x.strip() for x in correct_names]

    for i in range(len(video_list)):
        file_name, file_extension = os.path.splitext(video_list[i])
        os.rename(os.path.join(directory, video_list[i]), os.path.join(directory, correct_names[i] + file_extension))
        print(f"Renamed {video_list[i]} to {correct_names[i] + file_extension}")
        