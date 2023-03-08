import os

# Getting your current working directory
current_directory = os.getcwd()
print("Current Working Directory: \"{}\"".format(current_directory))

# getting the file tree or folder structure of a folder and its sub-folders
file_tree = 'C:\\Projects\\Python\\15.modules\\importss'
result = os.listdir(file_tree)
print("File tree for {}:\n{}".format(file_tree, result))

# Creating a new Directory
to_create = 'C:\\Projects\\Python\\16.Others'

try:
    if os.mkdir(to_create):
        print("{} was created successfully".format(to_create))
except FileExistsError as err:
    print("Error: {}".format(err))
