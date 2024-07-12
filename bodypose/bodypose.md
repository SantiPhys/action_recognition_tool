# Bodypose estimation with MediaPipe Holistic Model

The script in this folder processes a video file using MediaPipe's Holistic model to detect and draw landmarks for the body, hands, and face. It saves the processed video with the drawn landmarks and exports the landmark data to a CSV file. The script can display the processed video during processing based on a command-line argument. You can specify the input video file through a command-line argument as well.

## Contents

- `estimate_bodypose.py`: The main script that processes the video.
- `README.md`: This readme file.

## Requirements

- Python 3.6 or higher
- OpenCV
- MediaPipe
- NumPy

You can install the required packages using `pip`:

```sh
pip install opencv-python mediapipe numpy
```

## Usage

Run the script with default settings:

```sh
python estimate_bodypose.py
```

This will process the video at `/home/groupwork/groupwork-tool/data/data_raw/videos/webcam/test_distance_webcam.avi` and save the processed video and landmark data in the specified output folder.

### Command-line Arguments

- `-input <input_video_path>`: Specify the input video file.
- `-display on`: Display the processed video during processing.

### Examples

1. **Default behavior:**

   ```sh
   python estimate_bodypose.py
   ```

   Processes the video at `/home/groupwork/groupwork-tool/data/data_raw/videos/webcam/test_distance_webcam.avi`.

2. **Specifying an input video:**

   ```sh
   python estimate_bodypose.py -input /path/to/your/video.mp4
   ```

   Processes the specified video and saves the results.

3. **Specifying input video and enabling display:**

   ```sh
   python estimate_bodypose.py -input /path/to/your/video.mp4 -display on
   ```

   Processes the specified video, displays the video during processing, and saves the results.

## Output

The script generates two output files in the specified output folder (`/home/groupwork/groupwork-tool/data/data_processed/videos/mediapipe`):
- A processed video file with landmarks drawn, named `<input_video_name>__bodypose.<extension>`.
- A CSV file containing the landmark data, named `<input_video_name>__bodypose.csv`.