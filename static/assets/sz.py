import os

def rename_png_files(folder_path):
    # List all files in the folder
    files = os.listdir(folder_path)

    # Filter only PNG files
    png_files = [file for file in files if file.endswith('.PNG')]

    # Rename each PNG file to lowercase .png
    for png_file in png_files:
        old_path = os.path.join(folder_path, png_file)
        new_path = os.path.join(folder_path, png_file[:-4] + '.png')  # Change extension to lowercase .png

        # Rename file
        os.rename(old_path, new_path)
        print(f"Renamed {old_path} to {new_path}")

# Example usage:
folder_path = 'images'  # Replace with the path to your folder containing PNG files
rename_png_files(folder_path)
