# Seperating files into their respective folders 

import os
import shutil

# Set the path to the folder containing the files
path = '/workspace/Player_Performance_Prediction/Data'

# Create two destination folders
os.makedirs(path + '/csv_files')
os.makedirs(path + '/info_files')

# Loop through the files in the folder
for filename in os.listdir(path):
  # Check if the file ends in ".csv"
  if filename.endswith(".csv"):
    # Check if the file name contains "_info"
    if "_info" in filename:
      # If it does, move the file to the "info_files" folder
      shutil.move(path + '/' + filename, path + '/info_files')
    else:
      # If it doesn't, move the file to the "csv_files" folder
      shutil.move(path + '/' + filename, path + '/csv_files')