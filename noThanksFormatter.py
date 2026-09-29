from pathlib import Path

folder_path = Path("./bots")

# Get absolute paths of files only in the main folder
file_paths = [str(file.resolve()) for file in folder_path.iterdir() if file.is_file()]

print(file_paths)