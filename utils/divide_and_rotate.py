import numpy as np

# Define the angle theta
theta = np.pi / 4  # TODO: change this to the

def rotate_y(theta):

    # Rotation matrix about the y-axis
    rot_y = np.array([
        [np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])

    return rot_y

theta = -np.pi / 4  # TODO: change this to the angle given by the arc between reference and other coordinate system
rot_y = rotate_y(theta)
print(rot_y)
