# OpenFace Command Guide

This document provides a comprehensive guide to using OpenFace commands for headpose estimation within our project. OpenFace is a powerful tool for facial behavior analysis, including facial landmark detection, head pose estimation, and more. Follow the steps below to execute OpenFace commands effectively.

## Navigating to OpenFace Directory

First, navigate to the directory containing the OpenFace binaries:

```sh
cd ~/groupwork-tool/headpose/opencv-4.1.0/build/OpenFace/build
```

## Headpose Estimation Commands

### Single Person Estimation

To perform headpose estimation for videos featuring a single person, use the following command:
```sh
./bin/FeatureExtraction -f "/home/groupwork/groupwork-tool/data/data_raw/videos/360/panorama_centered_1per.MP4" -out_dir "/home/groupwork/groupwork-tool/data/data_processed/videos/OpenFace" -pose
```
This command extracts facial features and estimates the headpose, saving the results in the specified output directory.


### Multiple People Estimation
For videos featuring multiple people, use the `FaceLandmarkVidMulti` command as follows:

```sh
./bin/FaceLandmarkVidMulti -f "/home/groupwork/groupwork-tool/data/data_raw/videos/360/panorama_centered_3per.MP4" -out_dir "/home/groupwork/groupwork-tool/data/data_processed/videos/OpenFace"
```
This command is specifically designed to handle multiple faces within a video, providing detailed analysis for each detected individual.

## Default Behavior
To utilize the default OpenFace behavior without specifying an output directory, simply omit the `-out_dir` option:

```sh
./bin/FeatureExtraction -f "/path/to/your/video.MP4"
```

The results will be saved in the default processed folder within the OpenFace directory.

## Navigating to View Processed Results
To view the processed results, navigate to the `processed` folder:
```sh
cd /home/groupwork/groupwork-tool/headpose/opencv-4.1.0/build/OpenFace/build/processed
```

## Returning to Python Scripts Directory
After running the OpenFace commands, you can return to the directory containing your Python scripts with the following command:

```sh
cd /home/groupwork/groupwork-tool/headpose/openface
```