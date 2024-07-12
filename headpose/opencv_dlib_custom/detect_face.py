"""
This code uses OpenCV's DNN module to load a pre-trained model for face detection, 
preprocesses an input image, and applies the model to detect faces in the image. 
Detected faces are then highlighted with rectangles.

Taken from: https://towardsdatascience.com/real-time-head-pose-estimation-in-python-e52db1bc606a
"""

import cv2
import numpy as np
import os

# Load the model from the disk
modelFile = "models/res10_300x300_ssd_iter_140000.caffemodel"
configFile = "models/deploy.prototxt.txt"
input_folder = "../data/data_raw/images"
output_folder = "../data/data_processed/images"

# Read the model using cv2.dnn module
net = cv2.dnn.readNetFromCaffe(configFile, modelFile)

# Get the list of image files in the input folder
image_files = os.listdir(input_folder)

# Loop over each image file
for image_file in image_files:
    # Read the image file
    img_path = os.path.join(input_folder, image_file)
    img = cv2.imread(img_path)
    if img is None:
        continue  # skip if the image is not loaded properly

    # Get the height and width of the image
    h, w = img.shape[:2]

    # Preprocess the image: resize it to 300x300 pixels, scale the pixel values, and adjust the color channel ordering
    blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), 1.0, (300, 300), (104.0, 117.0, 123.0))

    # Set the blob as input to the network
    net.setInput(blob)

    # Perform a forward pass of the network to get the face detections
    faces = net.forward()

    # Loop over the face detections
    for i in range(faces.shape[2]):
        # Extract the confidence (i.e., probability) associated with the prediction
        confidence = faces[0, 0, i, 2]
        # Filter out weak detections by ensuring the confidence is greater than the minimum confidence
        if confidence > 0.5:
            # Compute the (x, y)-coordinates of the bounding box for the face
            box = faces[0, 0, i, 3:7] * np.array([w, h, w, h])
            (x, y, x1, y1) = box.astype("int")
            # Draw the bounding box of the face along with the associated probability
            cv2.rectangle(img, (x, y), (x1, y1), (0, 0, 255), 2)

    # Resize the image to fit comfortably on the left side of the display
    max_height = 800  # Adjust this value as needed
    scale_factor = max_height / h if h > max_height else 1
    resized_img = cv2.resize(img, (int(w * scale_factor), int(h * scale_factor)))

    # Display the output image with the bounding box
    cv2.imshow("Output", resized_img)

    # Save the image to disk
    output_path = os.path.join(output_folder, image_file.split(".")[0] + "_face_detected.jpg")
    cv2.imwrite(output_path, img)

    # Wait for a key press to move to the next image
    cv2.waitKey(0)

# Close all image windows
cv2.destroyAllWindows()
