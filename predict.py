import modules.utils as ut

import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder
# print(ut.getModelsPath())
# print(ut.getDatasetsPath())
# print(ut.getRootPath("abstract"))
print(ut.getSystemPlatform())

print(ut.getDatasetsFullPath("students.csv"))
print(ut.getModelsFullPath("model.m"))

clf = joblib.load(ut.getModelsFullPath("init_model.m"))
data = pd.read_csv(ut.getDatasetsFullPath("extData.csv"))

# Transform
le = LabelEncoder()
obj_cols = [col for t, col in zip(data.dtypes, data.columns) if t == 'object']
for col in obj_cols:
    data[col] = le.fit_transform(data[col])

# Pre-processing
data['All_Sup'] = data['famsup'] & data['schoolsup'] #1
data['PairEdu'] = data[['Fedu', 'Medu']].mean(axis=1) #2
data['more_high'] = data['higher'] & (data['schoolsup'] | data['paid']) #3
data['All_alc'] = data['Walc'] + data['Dalc'] # 4
data['Dalc_per_week'] = data['Dalc'] / data['All_alc'] # 5
data.drop(['Dalc'], axis=1, inplace=True) # 6
data['studytime_ratio'] = data['studytime'] / (data[['studytime', 'traveltime', 'freetime']].sum(axis=1))# 7
data.drop(["studytime"], axis=1, inplace=True) #8



y = clf.predict(data)

# data['G'] = list(map(round,y))
# data.to_csv("test.csv",index=False,sep=',')