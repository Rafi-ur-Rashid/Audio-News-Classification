import pandas as pd
import numpy as np
import os
import random
import shutil
import audio_metadata
import mutagen
import pickle
from mutagen.mp3 import MP3


SEED = 2245
random.seed(SEED)

BASE_FOLDER = "corpus"
labels = ['economics', 'entertainment', 'international', 'national', 'sports']

'''Gather statistics of only one file'''
def get_stats(file_name):
    # audio = MP3(file_name)
    
    try:
        metadata = audio_metadata.load(file_name)
        
        # print(metadata)
        
        try:
            channel_name = metadata['tags']['artist']
            title = metadata['tags']['title']
        except:
            channel_name = "<NULL>"
            title = "<NULL>"
        return channel_name, title, str(metadata)
    except:
        print("Problem with {}".format(file_name))
        return None, None, None


# cols = ["Filename", "Label", "Metadata"]

def dump_pickle(file_name, object):
    with open(file_name, mode='wb') as fout:
        pickle.dump(object, fout)


def load_pickle(file_name):
    with open(file_name, mode='rb') as fin:
        return pickle.load(fin, encoding='utf-8')    

def gather_statistics():
    file_names = []
    labels_save = []

    channel_names = []
    titles = []
    metadatas = []
    
    for label in labels:
        folder = os.path.join(BASE_FOLDER, label)

        files = [f for f in os.listdir(folder) if f.endswith(".mp3")]
        print(f"LABEL: {label}, # audio files =  {len(files)}")
        for file_name in files:
            new_file_name = os.path.join(folder, file_name)
            
            # https://pypi.org/project/audio-metadata/
            # print(new_file_name)
            
            channel_name, title, metadata = get_stats(file_name=new_file_name)
            # print(metadata)
            
            ## append to lists
            file_names.append(file_name)
            labels_save.append(label)
            
            channel_names.append(channel_name)
            titles.append(title)
            metadatas.append(metadata)
            
            # break
        
        print("---"*10)
        
        ## print lists
        # print(file_names)
        # print(labels_save)
        # print(metadatas)

        # break

    # df = pd.DataFrame(dicts)
    # print(df.head())
    
    # df.to_csv("Report-Metadata.csv", index=False)
    
    ## Save to pickle files.
    FOLDER_PICKLE = "Reports-Dataset-Sampling"
    

    join = lambda x: os.path.join(FOLDER_PICKLE, str(x))
    
    dicts = {
        "file_names": file_names,
        "labels": labels_save,
        "channel_names": channel_names,
        "titles": titles,
        "metadatas": metadatas
    }
    
    for key in dicts.keys():
        print("Key = {}".format(key), end=' ')
        print(f"Len of list = {len(dicts[key])}")
    
    # dump_pickle(file_name=join("dicts.pkl"), object=dicts)
    
    # dump_pickle(file_name=join("file_names.pkl"), object=file_names)
    # dump_pickle(file_name=join("labels.pkl"), object=labels)
    # dump_pickle(file_name=join("metadatas.pkl"), object=metadatas)
    
    # df = pd.DataFrame(columns=list(dicts.keys()))
    df = pd.DataFrame(dicts)
    
    df.to_csv(join("Reports-20June.csv"), index=False)
    
    # return df


def load_stats(file_name):
    obj = load_pickle(file_name)
    metadatas = obj['metadatas']

    md0 = metadatas[0]
    print(md0)
    
    m0 = dict(md0)
    print(m0)

####################################################################################################

gather_statistics()

# load_stats(file_name="Reports-Dataset-Sampling/dicts.pkl")

# _, _, metadata = get_stats(file_name="corpus/sports/700.mp3")
# print(metadata)