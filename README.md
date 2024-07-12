# Action Recognition Project Overview

This project is structured to facilitate the estimation of body and head poses using various tools and libraries, including OpenCV, dlib, and OpenFace. It is divided into several key directories, each serving a specific purpose in the workflow of pose estimation from video and image data. Below is a bird's eye view of the folder structure and a brief description of each component.

## Directory Structure

- `bodypose/`: Contains scripts and documentation for estimating body poses using MediaPipe
  - `bodypose.md`: Documentation on how to use the body pose estimation script.
  - `estimate_bodypose.py`: Script for estimating body poses from video data.
- `data/`: Holds raw and processed data, including images and videos.
  - `data_processed/`: Contains processed data ready for analysis.
    - `images/`: Processed images.
    - `videos/`: Processed videos, including those processed by MediaPipe, OpenFace, and the custom method
  - `data_raw/`: Stores the raw data collected or used for processing.
    - `images/`: Raw images.
    - `videos/`: Raw videos.
- `headpose/`: Dedicated to head pose estimation using OpenCV, dlib, and custom methods.
  - `opencv_dlib_custom/`: Contains scripts for head pose estimation using only OpenCV and dlib.
  - `opencv-4.1.0/`: Contains the OpenCV library, OpenFace, and documentation for building and using both of them.
  - `openface/`: Includes scripts and documentation for analyzing results obtained with OpenFace.
- `install_instructions/`: Provides detailed instructions for installing OpenFace and setting up the environment.
- `utils/`: Utility scripts that assist in data processing and manipulation.

## Key Features

- **Body Pose Estimation**: Utilizes MediaPipe for estimating body poses from video data, generating both visual outputs and CSV files containing landmark data.
- **Head Pose Estimation**: Employs OpenCV, dlib, and OpenFace for accurate head pose estimation from video and image data.
- **Installation and Setup**: Detailed instructions are provided for setting up OpenFace with Linux

This project structure is designed to be modular and extensible, allowing for easy integration of additional tools or data for pose estimation tasks.