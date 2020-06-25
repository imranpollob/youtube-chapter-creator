import moviepy.editor
import os


def convert(seconds):
    hours = seconds // 3600
    seconds %= 3600
    mins = seconds // 60
    seconds %= 60

    return f'{hours:02}:{mins:02}:{seconds:02}'


def video_duration(file_dir):
    video = moviepy.editor.VideoFileClip(file_dir)
    return int(video.duration)


# d = '/Users/imran/Documents/Tutorials/Complete Python Developer in 2020 Zero to Mastery/6. Advanced Python Object Oriented Programming'
d = '/Users/imran/Documents/Tutorials/Complete Python Developer in 2020 Zero to Mastery'
result = open('result.txt', 'a')


for root, dirs, files in os.walk(d):
    print(f'----------------{root}')
    # print(f'----------------{dirs}')
    # print(f'----------------{files}')
    result.write(f'{root}\n')
    video_list = [file for file in files if file.endswith(".mp4")]  # .sort(key=lambda i: int(i.split('.')[0]))
    video_list = sorted(video_list, key=lambda i: int(i.split('.')[0]))

    total_time = 0

    for video in video_list:
        duration = video_duration(os.path.join(root, video))
        total_time += duration
        print(f'{convert(total_time)} {video}')
        result.write(f'{convert(total_time)} {video}\n')