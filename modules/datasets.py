#Reader
import csv
import os
import modules.utils as ut
def readDataset(dataset):
    with open(ut.getDatasetsFullPath(dataset), encoding='utf-8') as d:
        return d
    pass

def readRawDataset():
    return readDataset("rawData.csv")


def readExtDataset():
    return readDataset("extData.csv")