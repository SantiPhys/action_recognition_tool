"""
This script compares headpose data from multiple CSV files by plotting the X, Y, and Z coordinates over time.
It allows for the visualization of headpose movements across different files to assess reliability and consistency.
The script supports input through command-line arguments, enabling the processing of specified files or a default set.
Plots are saved as a single image file, facilitating easy comparison.

Last edited by Santiago Poveda Gutierrez 2024/07/12
"""

import os
import argparse
import pandas as pd
import matplotlib.pyplot as plt

def load_and_filter_data(file_path):
    # Print the file being processed
    print(f"Loading and filtering data from {file_path}")
    # Load CSV file into DataFrame
    data = pd.read_csv(file_path)
    # Return only the columns of interest
    return data[['timestamp', 'pose_Tx', 'pose_Ty', 'pose_Tz']]

def plot_data(axs, row, col, data, label, title, color, y_limits):
    # Inform about the plotting process
    print(f"Plotting {label} data")
    # Plot the data with the specified configurations
    axs[row, col].plot(data['timestamp'], data[label], label=label, color=color)
    axs[row, col].set_xlabel('Timestamp')
    axs[row, col].set_ylabel(label.split('_')[1])
    axs[row, col].set_title(title)
    axs[row, col].set_ylim(*y_limits)
    axs[row, col].legend()
    axs[row, col].grid(True)

def main(input_files):
    # Start of the main function
    print("Starting main function")
    # Define the output folder path
    output_folder = "/home/groupwork/groupwork-tool/data/data_processed/videos/OpenFace"

    # Check if input files were provided
    if not input_files:
        # Default files to process if none are provided
        print("No input files provided, using default files")
        input_files = [
            "/home/groupwork/groupwork-tool/data/data_processed/videos/OpenFace/test_distance_webcam.csv",
            "/home/groupwork/groupwork-tool/data/data_processed/videos/OpenFace/test_distance_absolute_webcam.csv"
        ]

    # Determine the number of files to process
    num_files = len(input_files)
    # Setup the plot layout
    fig, axs = plt.subplots(3, num_files, figsize=(5 * num_files, 10))

    # Adjust layout for a single file
    if num_files == 1:
        axs = axs.reshape(3, 1)

    # Define colors for the plots
    colors = ['b', 'r', 'g', 'c', 'm', 'y', 'k']
    # Set y-axis limits for the plots
    y_limits = [(-500, 500), (-500, 500), (0, 1500)]
    # Labels for the data to plot
    labels = ['pose_Tx', 'pose_Ty', 'pose_Tz']

    # Loop through each file to process and plot
    for col, file_path in enumerate(input_files):
        # Load and filter data from the current file
        data = load_and_filter_data(file_path)
        # Extract the base name of the file for the title
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        # Titles for each subplot
        titles = [f"{base_name} - X Coordinate", f"{base_name} - Y Coordinate", f"{base_name} - Z Coordinate"]

        # Plot each data type in a separate subplot
        for row, (label, y_limit, title) in enumerate(zip(labels, y_limits, titles)):
            plot_data(axs, row, col, data, label, title, colors[col % len(colors)], y_limit)

    # Adjust layout to prevent overlap
    plt.tight_layout()

    # Generate the output file name based on the input files
    base_names = [os.path.splitext(os.path.basename(file))[0] for file in input_files]
    output_file_name = f"{'__vs__'.join(base_names)}__headpose.png"
    # Combine the output folder path and file name
    output_path = os.path.join(output_folder, output_file_name)
    # Save the plot to the specified path
    plt.savefig(output_path)
    # Inform the user where the plot was saved
    print(f"Plot saved to {output_path}")
    # Display the plot
    plt.show()

if __name__ == "__main__":
    # Script execution begins here
    print("Script execution started")
    # Setup command-line argument parsing
    parser = argparse.ArgumentParser(description="Compare headpose data from multiple CSV files.")
    parser.add_argument('-input', nargs='+', help="List of input CSV files to process.", default=None)
    # Parse arguments
    args = parser.parse_args()
    # Call the main function with the provided input files
    main(args.input)