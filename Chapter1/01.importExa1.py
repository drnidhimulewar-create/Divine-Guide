import os

# specify the directory path, or leave blank for current directory
directory_path = "/python"

try:
    # get a list of entries in the directory
    contents = os.listdir(directory_path)  # os.listdir() lists directory contents :contentReference[oaicite:1]{index=1}

    print(f"Contents of {directory_path}:")
    for item in contents:
        print(item)

except FileNotFoundError:
    print("Error: The specified directory was not found.")
except PermissionError:
    print("Error: Permission denied to access this directory.")
