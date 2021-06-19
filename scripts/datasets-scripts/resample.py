import pandas as pd
import os
import random
import shutil

SEED = 2245
random.seed(SEED)

BASE_FOLDER = "corpus"
labels = ['economics', 'entertainment', 'international', 'national', 'sports']

print(os.listdir(BASE_FOLDER))

proportions = [0.7, 0.1, 0.2]

## return train, val, test at {70, 10, 20}% respectively
def get_sampled_files(corpus_folder):
    files = os.listdir(corpus_folder)
    random.shuffle(files) # shuffle once.
    
    lens = [int(len(files)*p) for p in proportions]
    
    train = files[:lens[0]]
    val = files[lens[0]: lens[0]+lens[1]]
    test = files[lens[0]+lens[1]: ]
    
    print(f"lens = {lens}")
    
    print(f"Len whole = {len(files)}, lens train = {len(train)}\
, val = {len(val)}, test = {len(test)}")
    
    return train, val, test
    
# Naive way to write to CSV ... <file name> <label>
def write_log(label, train, val, test):
    
    def write_csv(label, list_data, csv_file_name):
        print(f"label = {label}, csv_file_name = {csv_file_name}")
        with open(csv_file_name, mode='a') as fout:
            for f in list_data:
                s = label + "\t" + str(f) + "\n"
                fout.write(s)
                
    base_folder = "Reports_Dataset_Sampling"
    
    csv_files = ["Shuffled-Train-June8.txt", "Shuffled-Val-June8.txt", "Shuffled-Test-June8.txt"]
    datas = [train, val, test]
    
    for list_data, csv_file_name in zip(datas, csv_files):
        csv_file_name = os.path.join(base_folder, csv_file_name)
        
        write_csv(label, list_data, csv_file_name)
        
    
################################################################


## Sample and write indices.
# for label in labels:
    # folder = os.path.join(BASE_FOLDER, label)
    # train, val, test = get_sampled_files(corpus_folder=folder)
    # write_log(label, train, val, test)
    
    
    
    
## Move datasets accordingly.

### First raw audio files (mp3 format)
csv_files = ["Shuffled-Train-June8.txt", 
"Shuffled-Val-June8.txt", 
"Shuffled-Test-June8.txt"]

modes = ["train", "val", "test"]

def copy_mp3_files(csv_file, mode='train'):
    cnt = 1
    with open(csv_file, mode='r') as fin:
        lines = [l.strip() for l in fin.readlines()]
        for line in lines:
            # economics<\t>1.mp3
            arr = line.split("\t")
            label = arr[0]
            file_name_src = arr[1]
            file_name_targ = "{}-{}.mp3".format(label, cnt)
            cnt += 1
            
            file_name_src = os.path.join("corpus", label, file_name_src)
            file_name_targ = os.path.join("corpus-shuffled", mode, file_name_targ)
            
            # print("Copy from {} to {}".format(file_name_src, file_name_targ))
            print("{}\t{}".format(file_name_src, file_name_targ))
            
            shutil.copy(file_name_src, file_name_targ)


def move_pkl_files(csv_file, mode='train'):
    cnt = 1
    with open(csv_file, mode='r') as fin:
        lines = [l.strip() for l in fin.readlines()]
        for line in lines:
            # economics<\t>1.mp3
            arr = line.split("\t")
            label = arr[0]
            
            counter = arr[1].split(".")[0]
            file_name_src = os.path.join("preprocessed", "sampled", label, "{}.pkl".format(counter))
            
            file_name_targ = "{}-{}.pkl".format(label, cnt)
            file_name_targ = os.path.join("preprocessed-shuffled", "sampled", mode, file_name_targ)            
            
            cnt += 1
            
            
            # print("Moving from {} to {}".format(file_name_src, file_name_targ))
            print("{}\t{}".format(file_name_src, file_name_targ))
            
            shutil.move(file_name_src, file_name_targ)
            

        
idx = 2

csv_files = [os.path.join("Reports_Dataset_Sampling", f) for f in csv_files]

move_pkl_files(csv_files[idx], mode=modes[idx])

# copy_mp3_files(csv_file=csv_files[idx], mode=modes[idx])

