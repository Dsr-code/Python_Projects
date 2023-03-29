import os
import getpass

# Define the path to the folder you want to lock
folder_path = "C:\Users\devde\Desktop\formatOS"

# Define the correct password
password = "khuljasimsim"

# Function to lock the folder
def lock_folder():
  # Add the hidden attribute to the folder
  os.system("attrib +h " + folder_path)

# Function to unlock the folder
def unlock_folder():
  # Remove the hidden attribute from the folder
  os.system("attrib -h " + folder_path)

# Prompt the user for the password
entered_password = getpass.getpass("Enter password to lock/unlock folder: ")

# If the password is correct, lock or unlock the folder
if entered_password == password:
  if os.path.isdir(folder_path):
    if os.path.exists(folder_path + "\\.locked"):
      # If the .locked file exists, the folder is already locked, so unlock it
      unlock_folder()
      print("Folder unlocked")
    else:
      # If the .locked file does not exist, the folder is not locked, so lock it
      lock_folder()
      print("Folder locked")
else:
  print("Incorrect password")

