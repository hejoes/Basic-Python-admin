import pwd

maxuid = 0

for line in open("/etc/passwd"):
  split = line.split(":")
  if int(split[2]) > maxuid:
    maxuid = int(split[2])


import os

def find_and_delete_files():
    for root, dirs, files in os.walk("/home/hejoes/test"):
        for file in files:
            file_path = os.path.join(root, file)
            if oct(os.stat(file_path).st_mode & 0o777) == '0o777':
                print("File: ", file_path)
                choice = input("Do you want to delete this file? (y/n)")
                if choice == 'y':
                    os.remove(file_path)
                    print("File deleted!")
                else:
                    print("File not deleted.")

find_and_delete_files()

      
