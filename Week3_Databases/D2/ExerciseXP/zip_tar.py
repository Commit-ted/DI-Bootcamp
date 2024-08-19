import zipfile
import tarfile
import os

# Define file paths
zip_file_path = '/Users/manuel/Desktop/DI-Bootcamp/Week3_Databases/D2/ExerciseXP/dvdrental.zip'
extracted_folder = '/Users/manuel/Desktop/DI-Bootcamp/Week3_Databases/D2/ExerciseXP/dvdrental_extracted'
tar_file_path = '/Users/manuel/Desktop/DI-Bootcamp/Week3_Databases/D2/ExerciseXP/dvdrental.tar'

# Step 1: Unzip the file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extracted_folder)

# Step 2: Create a .tar archive from the extracted folder
with tarfile.open(tar_file_path, 'w') as tar_ref:
    tar_ref.add(extracted_folder, arcname=os.path.basename(extracted_folder))

print("Conversion from .zip to .tar completed successfully.")
