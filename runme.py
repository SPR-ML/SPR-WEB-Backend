import json
# from urllib.parse import parse_qs
from fastapi import FastAPI
# from wsgiref.simple_server import make_server
from pydantic import BaseModel
# Python WEB接口开发 Flask -> FastAPI
import modules.datasets as ds
import modules.models as md

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

class form:
    formData = {}
    def __init__(self, data):
        self.formData = data

class dataset:
    fileUrl = ''
    def __init__(self, url):
        self.fileUrl = url

@app.post('/predict/form')
def getPredict(form: str):
    return {'message': '预测单个项目'}

@app.post('/predict/dataset')
def getPredictSet(dataset: str):
    return {'message': '预测数据集'}