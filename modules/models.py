# from sklearn.externals import joblib
import joblib
import pandas as pd
import modules.utils as ut
from sklearn.preprocessing import LabelEncoder

# availableModels = [
#     'v1_GaussianNB_Classifier_4.m', 'v1_MultiNB_Classifier_4.m',
#     'v2_GaussianNB_Classifier_2.m', 'v2_MultiNB_Classifier_2.m',
#     'v3_XGBRegressor.m', 'v4_CatBoostRegressor.m'
# ]
availableNoModels = [
    'v1_GaussianNB_Classifier_4.m', 'v1_MultiNB_Classifier_4.m',
    'v2_GaussianNB_Classifier_2.m', 'v2_MultiNB_Classifier_2.m',
    'v3_XGBRegressor.m'
]

availablePreModels = ['v4_CatBoostRegressor.m']


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
    data['more_high'] = data['higher'] & (data['schoolsup'] | data['paid']
                                          )  # 3
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
    print("[NAN]TO MODEL", data)
    res = clf.predict(data)
    return res
    pass


def runWithPreProcess(model, data: pd.DataFrame):
    clf = importModel(model)
    data = dataTransform(data)
    data = dataPreProcessing(data)
    print("[PRE]TO MODEL", data)
    print("[PRE]TITLING", data.columns)
    res = clf.predict(data)
    return res


# In stucture order
def predictForm(form, process=True):
    predictResult = []
    thisForm = vars(form)
    dataSet = {}
    print("this: ", thisForm)
    # logging.info("")
    dataSet['school'] = thisForm['School']
    dataSet['class'] = thisForm['Class']
    dataSet['age'] = thisForm['Age']
    dataSet['address'] = thisForm['Address']
    dataSet['famsize'] = thisForm['Famsize']
    dataSet['Pstatus'] = thisForm['Pstatus']
    dataSet['Medu'] = thisForm['Medu']
    dataSet['Fedu'] = thisForm['Fedu']
    dataSet['Mjob'] = thisForm['Mjob']
    dataSet['Fjob'] = thisForm['Fjob']
    dataSet['reason'] = thisForm['Reason']
    dataSet['guardian'] = thisForm['Guardian']
    dataSet['traveltime'] = thisForm['TravelTime']
    dataSet['studytime'] = thisForm['StudyTime']
    dataSet['failures'] = thisForm['Failures']
    dataSet['schoolsup'] = thisForm['SchoolSup']
    dataSet['famsup'] = thisForm['FamSup']
    dataSet['paid'] = thisForm['Paid']
    dataSet['activities'] = thisForm['Activities']
    dataSet['nursery'] = thisForm['Nursery']
    dataSet['higher'] = thisForm['Higher']
    dataSet['internet'] = thisForm['Internet']
    dataSet['romantic'] = thisForm['Romantic']
    dataSet['famrel'] = thisForm['FamRel']
    dataSet['freetime'] = thisForm['FreeTime']
    dataSet['goout'] = thisForm['GoOut']
    dataSet['Dalc'] = thisForm['Dalc']
    dataSet['Walc'] = thisForm['Walc']
    dataSet['health'] = thisForm['Health']
    dataSet['absences'] = thisForm['Absences']

    print("multi:", dataSet)

    for m in availableNoModels:
        predictResult.append(
            {"model": m[:4], "outcome": float(list(runWithNoProcess(m, pd.DataFrame.from_dict([dataSet])))[0])})
    for m in availablePreModels:
        predictResult.append(
            {"model": m[:4] , "outcome": float(list(runWithPreProcess(m, pd.DataFrame.from_dict([dataSet])))[0])})
    return predictResult
    # form = [value for value in args]


def predictFile(file: str, process=True):
    df = pd.read_csv("file")
    if process:
        return runWithPreProcess(df)
    else:
        return runWithNoProcess(df)