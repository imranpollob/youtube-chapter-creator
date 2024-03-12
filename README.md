# YouTube Chapter Creator

Easily create YouTube chapters for combined videos. This tool automatically generates chapters for merged video files, enhancing navigation for viewers and content structure for creators.

## Features

- Automatically detects video duration and creates chapter marks.
- Supports a variety of file naming conventions.
- Outputs chapter marks in a YouTube-ready format.

## Installation

1. **Clone the repository or download the source code.**

2. **Install Python dependencies:**

   Navigate to the project directory and run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install FFmpeg:**

   `moviepy` requires FFmpeg to process video files. Follow the instructions below based on your operating system:

   - **Windows:**
     1. Download FFmpeg from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html).
     2. Extract the downloaded archive.
     3. Add the path to the `bin` folder inside the extracted folder to your system's PATH environment variable.

   - **macOS:**
     Use Homebrew to install FFmpeg:
     ```bash
     brew install ffmpeg
     ```

   - **Linux:**
     Use your distribution's package manager. For example, on Ubuntu/Debian:
     ```bash
     sudo apt-get update
     sudo apt-get install ffmpeg
     ```

   Ensure FFmpeg is installed correctly by running `ffmpeg -version` in your command line or terminal.

## Usage

1. **Run the script:**
   ```bash
   python video.py
   ```

3. **Follow the script prompts:**
   - Enter the directory path containing your video files.


The script will generate a `result.txt` file with the YouTube chapters based on the video files in the specified directory.

## Requirements

- Python 3.x
- moviepy
- FFmpeg

For any issues related to FFmpeg installation or usage, refer to the [official FFmpeg documentation](https://ffmpeg.org/documentation.html).


## Useful softwares
- To merge videos free and fast use https://github.com/mifi/lossless-cut


## Renaming file names

Let's say you have files like the below naming convention.
```
lesson1.mp4
lesson2.mp4
lesson3.mp4
```

And you have a text file containing the correct name for each lessons. 
For example `course-contents.txt` may have the following content.

```
01 - Intro to JavaScript
02 - Variable declaration
03 - Loop
```

Now, if you want to rename original file names with correct file names defined in the `.txt` file then run the `rename.py` file.


1. **Run the script:**
   ```bash
   python rename.py
   ```

2. **Follow the script prompts:**
   - Enter the directory path containing your video files.
   - Enter the fie directory of the `.txt` file containing correct file names.