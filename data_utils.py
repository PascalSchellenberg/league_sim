import json
import os
import random
import string






def create_store_dir():


    # Get the current directory where the script is located
    current_dir = os.path.dirname(os.path.realpath(__file__))
    current_dir = os.path.join(current_dir, "runs")
    # Define the folder 
    
    chars = string.ascii_letters
    rnd_name = ''.join(random.choices(chars, k=12))
    #new_folder = os.path.join(current_dir, rnd_name)
    new_folder = os.path.join(current_dir, "test")
    
    # Check if the folder exists
    if os.path.exists(new_folder):
        print(f"The folder '{new_folder}' already exists.")
    else:
        os.makedirs(new_folder, exist_ok=True)
        print(f"Folder created at: {new_folder}")
    return str(new_folder)


def store_level_distribution(directory, level_map, run_nr):

    filename =filename = os.path.join(directory,'run' + str(run_nr) +'.json')
    with open(filename, 'w') as json_file:
        json.dump(level_map, json_file, indent=4)
