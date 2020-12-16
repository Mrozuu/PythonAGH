import os

folder_directory = "C:\\Program Files"
counter = str(len(os.listdir(folder_directory)))
print("In " + folder_directory + " is " + counter + " files")
