import pandas as pd
import os
import random
import shutil

SEED = 2245
random.seed(SEED)

def get_pkl_name(file_name):
    return file_name.replace(".mp3", ".pkl")

BASE_FOLDER = "Reports-Dataset-Sampling"
def move_files(mode="train"):
    csv_file_name = os.path.join(BASE_FOLDER, "{}.csv").format(mode)
    df = pd.read_csv(csv_file_name)
    
    old_file_names = df['old_file_names'].values.tolist()
    new_file_names = df['new_file_names'].values.tolist()
    
    for old_file, new_file in zip(old_file_names, new_file_names):
        old_name = os.path.join("preprocessed/sampled", get_pkl_name(old_file))
        new_name = os.path.join("preprocessed-sampling", get_pkl_name(new_file))
        
        print(old_name, new_name)
        
        
        shutil.move(old_name, new_name)
        
    print(f"Completed for mode = {mode}")
        
#######################################################################################

move_files(mode='train')
move_files(mode='val')
move_files(mode='test')


    