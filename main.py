import os
import shutil

def create_folder(directory):
    try:
        os.makedirs(directory)
    except FileExistsError:
        pass

def sort_files(source_dir):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    destination_dir = os.path.join(script_dir, 'Sorted Files')
    create_folder(destination_dir)

    files = os.listdir(source_dir)
    for file in files:
        if os.path.isfile(os.path.join(source_dir, file)):
            extension = os.path.splitext(file)[1][1:].lower()
            if extension == os.path.splitext(os.path.basename(__file__))[1][1:].lower():
                continue  # Skip the script file itself
            destination_folder = os.path.join(destination_dir, extension)
            create_folder(destination_folder)
            shutil.move(os.path.join(source_dir, file), os.path.join(destination_folder, file))

# Sort the files in the same directory as the script
script_directory = os.path.dirname(os.path.abspath(__file__))
sort_files(script_directory)
