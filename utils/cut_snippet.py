import cv2

# Control variables
duration_seconds = 20
crop = True
if crop:
    min_x, max_x = 550, 1300
    min_y, max_y = 400, 1000  # New variables for Y-axis cropping

# Open the original video file
input_video_path = '/home/groupwork/groupwork-tool/data/data_raw/videos/360/panorama_centered_1per.MP4'
output_video_path = '/home/groupwork/groupwork-tool/data/data_raw/videos/360/panorama_centered_cropped_1per.MP4'
cap = cv2.VideoCapture(input_video_path)

# Check if video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Get video properties
fps = cap.get(cv2.CAP_PROP_FPS)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Calculate the number of frames to extract
frames_to_extract = int(fps * duration_seconds)

# Ensure cropping bounds are within the frame dimensions
if crop:
    min_x = max(0, min_x)
    max_x = min(frame_width, max_x)
    min_y = max(0, min_y)  # Ensure min_y is within bounds
    max_y = min(frame_height, max_y)  # Ensure max_y is within bounds
    cropped_width = max_x - min_x
    cropped_height = max_y - min_y  # Calculate cropped height
else:
    cropped_width = frame_width
    cropped_height = frame_height
    min_x = 0
    max_x = frame_width
    min_y = 0
    max_y = frame_height

# Set up the video writer with new dimensions
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec
out = cv2.VideoWriter(output_video_path, fourcc, fps, (cropped_width, cropped_height))

# Read and write frames until the first minute
frame_count = 0
while frame_count < frames_to_extract:
    ret, frame = cap.read()
    if not ret:
        break
    # Crop frame according to both X and Y dimensions
    cropped_frame = frame[min_y:max_y, min_x:max_x, :]
    out.write(cropped_frame)
    frame_count += 1

# Release resources
cap.release()
out.release()
print(f"First {duration_seconds} seconds of video saved successfully in {output_video_path}.")