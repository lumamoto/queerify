from ..Notebooks.dataset import ari_to_features
import pandas as pd
import re
import os
from tqdm import tqdm

def data_preprocessing(dataset,savefile=None):
    #note dataset and savefile are just filenames and not the entire path.
    #dataset must be stored in datafile
    dataPath = os.path.join('./data',dataset)
    df = pd.read_csv(dataPath)
    df.head()
    df["track_uri"] = df["track_uri"].apply(lambda x: re.findall(r'\w+$', x)[0])
    df["track_uri"]

    datalist=df['track_uri'].unique()
    featureLIST=[]
    for i in tqdm([uri for uri in datalist]):
        try:
            featureLIST.append(ari_to_features(i))
        except:
            continue
    featureDF = pd.DataFrame(featureLIST)
    testDF=df
    new_df = pd.merge(testDF,featureDF, left_on = "track_uri", right_on= "id")
    if savefile==None:
        new_df.to_csv(dataPath)
    else:
        new_df.to_csv(os.path.join('./data',savefile))

