import pandas as pd
import os
import random
import shutil

SEED = 2245
random.seed(SEED)

BASE_FOLDER = "corpus"
labels = ['economics', 'entertainment', 'international', 'national', 'sports']
inside_folders = ['new', 'old']

def move_files():
    for label in labels:
        folder = os.path.join(BASE_FOLDER, label)
        print(folder)
        
        # merge everything from 'new' and 'old' to 'this'
        for inside in inside_folders:
            folder_inside = os.path.join(folder, inside)
            
            files = os.listdir(folder_inside)
            
            for file_name in files:
                # print(file_name)
                # shutil.move(src/old, dest/new)
                
                old_file_name = os.path.join(folder_inside, file_name)
                new_file_name = os.path.join(folder, file_name)
                
                print(old_file_name, new_file_name)
                shutil.move(old_file_name, new_file_name)
                
                # break
            
        
        # print(os.listdir(folder))
        
        print("---"*10)




####################################################################################################

# move_files()
# remove_folders()
