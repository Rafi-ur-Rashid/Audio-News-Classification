import pandas as pd
import os
import random
import shutil

SEED = 2245
random.seed(SEED)

BASE_FOLDER = "Reports-Dataset-Sampling"
def move_files(mode="train"):
    csv_file_name = os.path.join(BASE_FOLDER, "{}.csv").format(mode)
    df = pd.read_csv(csv_file_name)
    
    old_file_names = df['old_file_names'].values.tolist()
    new_file_names = df['new_file_names'].values.tolist()
    
    for old_file, new_file in zip(old_file_names, new_file_names):
        old_name = os.path.join("corpus", old_file)
        new_name = os.path.join("corpus-sampling", new_file)
        
        # print(old_name, new_name)
        
        shutil.copy(old_name, new_name)
        
    print(f"Completed for mode = {mode}")
        
#######################################################################################

move_files(mode='train')
move_files(mode='val')
move_files(mode='test')


    