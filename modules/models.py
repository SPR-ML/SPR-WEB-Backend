# from sklearn.externals import joblib
import joblib
import pandas as pd
import modules.utils as ut
from sklearn.preprocessing import LabelEncoder

availableModels = [
    'v1_GaussianNB_Classifier_4.m', 'v1_MultiNB_Classifier_4.m',
    'v2_GaussianNB_Classifier_2.m', 'v2_MultiNB_Classifier_2.m',
    'v3_XGBRegressor.m', 'v4_CatBoostRegressor.m'
]


def dataTransform(data):
    le = LabelEncoder()
    obj_cols = [
        col for t, col in zip(data.dtypes, data.columns) if t == 'object'
    ]
    for col in obj_cols:
        data[col] = le.fit_transform(data[col])
    return data


def dataPreProcessing(data):
    data['All_Sup'] = data['famsup'] & data['schoolsup']  # 1
    data['PairEdu'] = data[['Fedu', 'Medu']].mean(axis=1)  # 2
    data['more_high'] = data['higher'] & (data['schoolsup'] | data['paid'])  # 3
    data['All_alc'] = data['Walc'] + data['Dalc']  # 4
    data['Dalc_per_week'] = data['Dalc'] / data['All_alc']  # 5
    data.drop(['Dalc'], axis=1, inplace=True)  # 6
    data['studytime_ratio'] = data['studytime'] / (
        data[['studytime', 'traveltime', 'freetime']].sum(axis=1))  # 7
    data.drop(["studytime"], axis=1, inplace=True)  # 8
    return data


def importModel(model):
    return joblib.load(ut.getModelsFullPath(model))


# def predictDataFrame(data: pd.DataFrame):
#     pass
def runWithNoProcess(model, data: pd.DataFrame):
    clf = importModel(model)
    data = dataTransform(data)
    res = clf.predict(data)
    return res
    pass


def runWithPreProcess(model, data: pd.DataFrame):
    clf = importModel(model)
    data = dataTransform(data)
    data = dataPreProcessing(data)
    res = clf.predict(data)
    return res


# In stucture order
def predictForm(form, process=True):
    predictResult = []
    for m in availableModels:
        if process:
            predictResult.append(
                runWithPreProcess(pd.DataFrame.from_dict(vars(form))))
        else:
            predictResult.append(
                runWithNoProcess(pd.DataFrame.from_dict(vars(form))))
    return predictResult
    # form = [value for value in args]


def predictFile(file: str, process=True):
    df = pd.read_csv("file")
    if process:
        return runWithPreProcess(df)
    else:
        return runWithNoProcess(df)