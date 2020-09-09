import json
# from urllib.parse import parse_qs
from fastapi import FastAPI, File, UploadFile
# from wsgiref.simple_server import make_server

#Across Field
from starlette.middleware.cors import CORSMiddleware
from typing import Optional
from pydantic import BaseModel
# Python WEB接口开发 Flask -> FastAPI
import modules.datasets as ds
import modules.models as md 
import modules.statistic as st
import modules.utils as ut
import logging
import time
import os
#Add WEBAPP
app = FastAPI()

#Allow all
origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)
#Set Logger
logging.basicConfig(filename='runtime.log', level=logging.INFO)

@app.get('/test')
def test():
    logging.debug("Response: Test")
    try:
        logging.info("Test Success")
        return {'message': 'Init FastAPI successfully.'}
    except Exception as e:
        logging.error("Please check connection: ", str(e))
    

@app.get('/datasets/column/target')
def getRawTarget(scale: str):
    return {'message':'成功获取','result': ds.getColumn('G')}

@app.get('/datasets/column/{col}')
def getRawColumn(scale: str, col: str):
    return {'message':'成功获取','result': ds.getColumn(col)}

@app.get('/model/{modelType}')
def getModel(modelType: str):
    #v1
    #v2
    #v3
    #{'date':,'version':,'accurancy-score':,'cor':,'r2-score':,'rame'}
    return
    # return {'message': '请求{}模型中的{}项'.format(modelType)}

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
    return {'message':'成功获取', 'result':st.importance}

@app.get('/stat/appearance')
def getAppearance():
    return {'message':'成功获取', 'result':st.appearance}

@app.post('/predict/form')
def getPredict(form: attributes):
    return {'message': '成功获取', 'result': md.predictForm(form)}

@app.post('/predict/dataset')
async def getPredictSet(dataset: UploadFile = File(...)):
    start = time.time()
    try:
        res = await dataset.read()
        with open(os.path.join(ut.getDatasetsFullPath(),dataset.filename), "wb") as f:
            f.write(res)
        return {"message": "成功获取", 'time': time.time() - start, 'filename': dataset.filename}
    except Exception as e:
        return {"message": str(e), 'time': time.time() - start, 'filename': dataset.filename}