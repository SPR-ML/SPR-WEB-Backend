import os
import sys
import platform


def getRootPath(mode = "system"):
    if mode == "system":
        return os.getcwd()
    elif mode == "abstract":
        return os.path.abspath(os.path.dirname("."))
    else:
        return ""

def getSystemPlatform():
    os = platform.system()
    # p = platform.platform()
    return os

def getModelsPath():
    root = getRootPath()
    # return root
    return os.path.join(root,'static','models')

def getDatasetsPath():
    root = getRootPath()
    # return root
    return os.path.join(root,'static','datasets')

def getFilePath(path, fileName):
    return os.path.join(path,fileName)

def getModelsFullPath(fileName):
    return getFilePath(getModelsPath(),fileName)

def getDatasetsFullPath(fileName):
    return getFilePath(getDatasetsPath(),fileName)