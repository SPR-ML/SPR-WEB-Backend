# from sklearn.externals import joblib
import joblib
import pandas as pd
def importModel(model):
    return joblib.load(model)

def predictDataFrame(data: pd.DataFrame):
    pass

# In stucture order
def predictForm(form):
    return predictDataFrame(pd.DataFrame.from_dict(vars(form)))
    # form = [value for value in args]

def predictFile(file: str):
    df = pd.read_csv("file")
    return predictDataFrame(df)