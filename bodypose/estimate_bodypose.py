"""
This script processes a video file using MediaPipe's Holistic model to detect and draw landmarks for the body, hands, and face.
It saves the processed video with the drawn landmarks and exports the landmark data to a CSV file.
The script can display the processed video during processing based on a command-line argument.
You can specify the input video file through a command-line argument as well.

Usage:
    python omni_holi01.py [-input <input_video_path>] [-display on]

Last edited by Santiago Poveda Gutierrez 2024/07/12

"""
 
import os
import cv2
import mediapipe as mp
import numpy as np
import sys

# Control variables
resize = True
scale_percent = 45  # percentage of original size
default_input_video = '/home/groupwork/groupwork-tool/data/data_raw/videos/webcam/test_distance_webcam.avi'
output_folder = '/home/groupwork/groupwork-tool/data/data_processed/videos/mediapipe/'
display_video = False

# Check command-line arguments for input video and display option
input_video = default_input_video
if len(sys.argv) > 1:
    for i in range(1, len(sys.argv), 2):
        if sys.argv[i] == '-input' and i + 1 < len(sys.argv):
            input_video = sys.argv[i + 1]
            print(f"Using input video: {input_video}")
        elif sys.argv[i] == '-display' and i + 1 < len(sys.argv) and sys.argv[i + 1] == 'on':
            display_video = True

# Initialize MediaPipe and related objects
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic
data_land = np.zeros((0, 99))
data_land2 = None

# Load mp4 file
cap = cv2.VideoCapture(input_video)  # load video file

# Get the number of frames, FPS, width, and height of the video
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
idx = 0

# Prepare video writer for saving the processed video
video_name, video_ext = os.path.basename(input_video).split('.')
output_video_path = os.path.join(output_folder, video_name + "__bodypose." + video_ext)
output_csv_path = os.path.join(output_folder, video_name + "__bodypose.csv")
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

# Holistic Model and Frame Processing Loop
with mp_holistic.Holistic(
        min_detection_confidence=0.9,
        min_tracking_confidence=0.9) as holistic:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print(f'skipped: {idx=}')
            # If the final frame, exit. Otherwise, treat as a detection failure (assign None)
            if idx < frame_count:
                idx += 1
                if data_land2 is None:
                    data_land = np.vstack((data_land, np.zeros(99)))
                else:
                    data_land = np.vstack((data_land, data_land2))
                continue
            else:
                print('End of Files.')
                break

        # Image Preprocessing and Landmark Detection
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = holistic.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Draw landmarks on the images
        mp_drawing.draw_landmarks(
            image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
        mp_drawing.draw_landmarks(
            image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
        mp_drawing.draw_landmarks(
            image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)

        # Get coordinates
        if results.pose_landmarks is None:
            if data_land2 is None:
                data_land = np.vstack((data_land, np.zeros(99)))
            else:
                data_land = np.vstack((data_land, data_land2))
        else:
            data_land2 = np.zeros((1, 3))
            for x in range(0, 33):
                data1 = results.pose_landmarks.landmark[x].x
                data2 = results.pose_landmarks.landmark[x].y
                data3 = results.pose_landmarks.landmark[x].z
                keydata = np.hstack((data1, data2, data3)).reshape(1, -1)
                data_land2 = np.hstack((data_land2, keydata))
            data_land2 = data_land2[:, 3:]
            data_land = np.vstack((data_land, data_land2))

        # Increment the frame number
        idx += 1

        if resize:
            # Resize image before displaying
            display_width = int(image.shape[1] * scale_percent / 100)
            display_height = int(image.shape[0] * scale_percent / 100)
            dim = (display_width, display_height)
            display_image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
        else:
            display_image = image

        # Write the frame to the output video
        out.write(image)

        if display_video:
            # Display image until "esc" key is pressed
            cv2.imshow('MediaPipe Holistic', display_image)
            if cv2.waitKey(5) & 0xFF == 27:
                break

# Save data_land to the new CSV file
np.savetxt(output_csv_path, data_land, delimiter=',')
print(f"Saved bodypose data to {output_csv_path}")

cap.release()
out.release()
print(f"Saved processed video to {output_video_path}")

if display_video:
    cv2.destroyAllWindows()

print("Video processing completed.")
