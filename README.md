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

1. **Set the directory variable in `video.py` to the path where your videos are located.**

2. **Run the script:**
   ```bash
   python video.py
   ```

3. **Follow the script prompts:**
   - Enter the directory path containing your video files.
   - Provide a sample file name to help the script detect the numbering pattern.

The script will generate a `result.txt` file with the YouTube chapters based on the video files in the specified directory.

## Requirements

- Python 3.x
- moviepy
- FFmpeg

For any issues related to FFmpeg installation or usage, refer to the [official FFmpeg documentation](https://ffmpeg.org/documentation.html).
