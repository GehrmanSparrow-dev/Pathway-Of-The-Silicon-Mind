import os
import shutil
import csv

# Specify the folder to organize
folder_path = r"C:\Pathway of the Silicon Mind\Sequence 9\.venv"

# Dictionary that maps file extensions to folder names
file_types = {
    ".txt": "Text",
    ".pdf": "Documents",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".csv": "Data"
}

# Create a CSV log file to record moved files
log_file = os.path.join(folder_path, "file_movements.csv")

with open(log_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    # Write the header row
    writer.writerow(["File Name", "Destination Folder"])

    # Loop through every item in the directory
    for file_name in os.listdir(folder_path):

        # Get the complete file path
        source = os.path.join(folder_path, file_name)

        # Skip directories (only process files)
        if os.path.isdir(source):
            continue

        # Get the file extension
        extension = os.path.splitext(file_name)[1].lower()

        # Check if the file type is supported
        if extension in file_types:

            # Determine the destination folder
            destination_folder = os.path.join(folder_path, file_types[extension])

            # Create the folder if it doesn't already exist
            os.makedirs(destination_folder, exist_ok=True)

            # Create the destination path
            destination = os.path.join(destination_folder, file_name)

            try:
                # Move the file
                shutil.move(source, destination)

                # Record the movement in the CSV log
                writer.writerow([file_name, file_types[extension]])

                print(f"Moved {file_name} -> {file_types[extension]}")

            # Handle permission errors gracefully
            except PermissionError:
                print(f"Permission denied: Could not move '{file_name}'.")

print("File organization complete!")