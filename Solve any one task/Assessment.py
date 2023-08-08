# Assessment.py
import os
import shutil

def rename_and_copy_videos(source_folder, dest_folder, prefix="VS_"):
    try:
        # Create the destination folder if it doesn't exist
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)

        # Get a list of video files in the source folder
        video_files = [file for file in os.listdir(source_folder) if file.endswith(".mp4")]

        # Iterate through the video files and rename + copy them to the destination folder
        for index, video_file in enumerate(video_files, start=1):
            new_filename = f"{prefix}{index:03}.mp4"
            source_path = os.path.join(source_folder, video_file)
            dest_path = os.path.join(dest_folder, new_filename)

            shutil.copy2(source_path, dest_path)
            print(f"Renamed and copied: {video_file} -> {new_filename}")

        print("Renaming and copying complete.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    source_folder = "folder_1"
    dest_folder = "folder_2"

    rename_and_copy_videos(source_folder, dest_folder)
