import os
import shutil
import zipfile
import tempfile
from pathlib import Path

def merge_directories(src, dst):
    """
    Merge two directories, preserving unique files and handling naming conflicts.
    
    Args:
        src (str): Source directory path
        dst (str): Destination directory path
    """
    src_path = Path(src)
    dst_path = Path(dst)
    
    for src_file in src_path.rglob('*'):
        if src_file.is_file():
            # Get the relative path from the source directory
            rel_path = src_file.relative_to(src_path)
            dst_file = dst_path / rel_path
            
            # Create parent directories if they don't exist
            dst_file.parent.mkdir(parents=True, exist_ok=True)
            
            # If the file doesn't exist in destination, copy it
            if not dst_file.exists():
                shutil.copy2(src_file, dst_file)
                print(f"Copied unique file: {rel_path}")
            else:
                # If file exists, compare sizes and modification times
                if src_file.stat().st_size != dst_file.stat().st_size:
                    # Files are different, create a numbered version
                    counter = 1
                    while True:
                        new_name = dst_file.parent / f"{dst_file.stem}_{counter}{dst_file.suffix}"
                        if not new_name.exists():
                            shutil.copy2(src_file, new_name)
                            print(f"Copied as alternate version: {new_name}")
                            break
                        counter += 1

def extract_and_merge_zips(input_dir, output_dir, base_filename):
    """
    Extracts split ZIP files while preserving unique files and folder structures.
    
    Args:
        input_dir (str): Directory containing the split ZIP files
        output_dir (str): Directory where files will be extracted
        base_filename (str): Base name of the split files
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    try:
        part_num = 1
        while True:
            # Check for next part
            part_name = f"{base_filename}{str(part_num).zfill(3)}.zip"
            part_path = os.path.join(input_dir, part_name)
            
            if not os.path.exists(part_path):
                break
                
            print(f"\nProcessing part {part_num}: {part_name}")
            
            # Create a temporary directory for this part
            with tempfile.TemporaryDirectory() as temp_dir:
                print(f"Extracting part {part_num} to temporary directory...")
                
                # Extract this part to temporary directory
                with zipfile.ZipFile(part_path, 'r') as zip_ref:
                    zip_ref.extractall(temp_dir)
                
                # Merge the contents with the output directory
                print(f"Merging contents of part {part_num}...")
                merge_directories(temp_dir, output_dir)
            
            part_num += 1
        
        if part_num == 1:
            raise FileNotFoundError("No ZIP parts found!")
            
        print(f"\nSuccessfully processed {part_num - 1} parts.")
        print(f"All unique files have been extracted to: {output_dir}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise

# Usage example with your specific paths
input_directory = '/Volumes/Manu/Jean Pierre Weill Media/Rar'
output_directory = '/Volumes/Manu/Jean Pierre Weill Media/Unrar'
base_filename = 'filename'  # Just the base name without numbers or extension

extract_and_merge_zips(input_directory, output_directory, base_filename)