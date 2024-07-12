# Headpose with OpenFace

This Python script is designed to compare headpose data from multiple CSV files obtained with OpenFace by plotting the X, Y, and Z coordinates over time. It enables the visualization of headpose movements across different files to assess their reliability and consistency. The script supports input through command-line arguments, allowing for the processing of specified files or a default set. Plots are saved as a single image file, facilitating easy comparison.

## Features

- Load headpose data from CSV files.
- Filter and retain relevant columns (`timestamp`, `pose_Tx`, `pose_Ty`, `pose_Tz`).
- Plot X, Y, and Z coordinates over time for each file.
- Support for multiple files comparison.
- Save plots as a single image file for easy comparison.

## Requirements

Before running the script, ensure you have the following installed:

- Python 3.x
- Pandas: `pip install pandas`
- Matplotlib: `pip install matplotlib`

## Usage

1. **Prepare Your Data**: Ensure your CSV files follow the OpenFace output format. They must at least contain the columns `timestamp`, `pose_Tx`, `pose_Ty`, and `pose_Tz`. 

2. **Run the Script**: Use the command line to navigate to the script's directory and run it with the following syntax:

```bash
python check_headpose_reliability.py -input [path_to_csv1] [path_to_csv2] ...