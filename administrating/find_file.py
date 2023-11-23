import os
import time

def search_file(filename):
    for root, dirs, files in os.walk("/"):
        for file in files:
            if file.startswith(filename):
                file_path = os.path.join(root, file)
                file_stats = os.stat(file_path)
                last_mod_time = time.ctime(file_stats.st_mtime)
                file_created = time.ctime(file_stats.st_ctime)
                return (file_path, last_mod_time, file_created)
    return None

file_name = input("Enter the file name without extension (like without .png in the end): ")
file_path, last_mod, file_created = search_file(file_name)
if file_path:
    print("File path:", file_path)
    print("Last Modified:", last_mod)
    print("File Created:", file_created)
else:
    print(f"{file_name} not found.")