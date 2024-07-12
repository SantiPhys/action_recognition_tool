# Head Pose Estimation using OpenCV and dlib

This script performs head pose estimation using a webcam or video file. It uses the OpenCV library and dlib to detect faces, extract facial landmarks, and estimate head pose. The head pose is estimated by solving the Perspective-n-Point (PnP) problem, which involves finding the rotation and translation vectors of the head in 3D space. The script draws a 3D annotation box on the face to visualize the head pose and displays the angles of head rotation in degrees, printing messages indicating the direction of head movement (up, down, left, right). It has been adapted and modified from the 
[Proctoring-AI project on GitHub](https://github.com/vardanagarwal/Proctoring-AI.git)

## Folder Structure

```
.
├── __pycache__
├── detect_face.py
├── draw_face_landmarks.py
├── face_detector.py
├── face_landmarks.py
├── head_pose_estimation.py
├── head_pose_estimation_old.py
└── models
```

### Description

- `__pycache__`: Contains cached bytecode of the Python files.
- `detect_face.py`: Module for face detection.
- `draw_face_landmarks.py`: Module for drawing face landmarks.
- `face_detector.py`: Module for getting the face detector model and finding faces.
- `face_landmarks.py`: Module for getting the facial landmark model and detecting landmarks.
- `head_pose_estimation.py`: The main script for head pose estimation.
- `models`: Directory containing pre-trained models for face detection and landmark detection.

## Usage

### Arguments

- `-i` or `--input`: Path to the input video file. If not provided, the webcam is used.
- `-v` or `--verbose`: Verbosity level. Choices are:
  - `cam`: Print head position messages.
  - `war`: Print TensorFlow warnings.
  - `all`: Print both head position messages and TensorFlow warnings.

### Example Commands

1. **Using Webcam without Verbosity:**
   ```sh
   python3 head_pose_estimation.py
   ```

2. **Using Webcam with Head Position Messages:**
   ```sh
   python3 head_pose_estimation.py -v cam
   ```

3. **Using Webcam with TensorFlow Warnings:**
   ```sh
   python3 head_pose_estimation.py -v war
   ```

4. **Using Webcam with All Messages:**
   ```sh
   python3 head_pose_estimation.py -v all
   ```

5. **Using a Video File without Verbosity:**
   ```sh
   python3 head_pose_estimation.py -i "../../data/data_raw/videos/test_1min_1p.avi"
   ```

6. **Using a Video File with Head Position Messages:**
   ```sh
   python3 head_pose_estimation.py -i "../../data/data_raw/videos/test_1min_1p.avi" -v cam
   ```

7. **Using a Video File with TensorFlow Warnings:**
   ```sh
   python3 head_pose_estimation.py -i "../../data/data_raw/videos/test_1min_1p.avi" -v war
   ```

8. **Using a Video File with All Messages:**
   ```sh
   python3 head_pose_estimation.py -i "../../data/data_raw/videos/test_1min_1p.avi" -v all
   ```

### Output

The processed video is saved in the `../../data/data_processed/videos` folder. The output video filename is based on the input source:

- For video file input: `<input_filename>_headpose<extension>`.
- For webcam input: `webcam_headpose.avi`.

The script prints the path of the processed output video to the terminal.
