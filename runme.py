import json
# from urllib.parse import parse_qs
from fastapi import FastAPI
# from wsgiref.simple_server import make_server
from typing import Optional
from pydantic import BaseModel
# Python WEB接口开发 Flask -> FastAPI
import modules.datasets as ds
import modules.models as md 
import modules.statistic as st


app = FastAPI()

@app.get('/test')
def test():
    return {'message': 'Init FastAPI successfully.'}

@app.get('/{scale}/column/target')
def getRawTarget(scale: str):
    if scale == 'ext':
        return {'message': '请求扩展数据集G3中'}
    elif scale == 'raw':
        return {'message': '请求原始G3中'}
    else:
        return {'message': '未找到请求目标'}

@app.get('/{scale}/column/{colType}/{col}')
def getRawColumn(scale: str,colType: str, col: str):
    return {'message': '请求{}数据集中{}类型的{}数据统计'.format(scale,colType, col)}

@app.get('/model/{modelType}/{target}')
def getModel(modelType: str, target: str):
    return {'message': '请求{}模型中的{}项'.format(modelType,target)}

class attributes(BaseModel):
    School: str
    Class: int
    Age: int
    Address: str
    Famsize: str
    Pstatus: str
    Medu: int
    Fedu: int
    Mjob: str
    Fjob: str
    Reason: str
    Guardian: str
    TravelTime: int
    StudyTime: int
    Failures: int
    SchoolSup: bool
    FamSup: bool
    Paid: bool
    Activities: bool
    Nursery: bool
    Higher: bool
    Internet: bool
    Romantic: bool
    FamRel: int
    FreeTime: int
    GoOut: int
    Dalc: int
    Walc: int
    Health: int
    Absences: int
    # G: int



@app.get('/stat/importance')
def getImportance():
    return st.importance

@app.get('/stat/appearance')
def getAppearance():
    return st.appearance

@app.post('/predict/form')
def getPredict(form: attributes):
    #return {''}
    return {'message': '预测单个项目'}

@app.post('/predict/dataset')
def getPredictSet(dataset: str):
    return {'message': '预测数据集'}