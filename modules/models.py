from sklearn.externals import joblib


def importModel():
    return joblib.load("model.m")