#Reader
import csv
import os
import pandas as pd
import modules.utils as ut
#import utils as ut
from collections import Counter

def readDataset(dataset):
    return pd.read_csv(ut.getDatasetsFullPath(dataset))


def getColumn(column):
    dataset = readDataset('rawData.csv')
    return dict(Counter(list(dataset[column])))