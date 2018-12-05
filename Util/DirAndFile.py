#encoding=utf-8
import os
from ProjectVar.Var import *

def createDir(path,dirName):
    #os.path.join(x,y)是拼接路径用的
    dirPath=os.path.join(path,dirName)
    #判断路径是否存在，存在则pass，否则新建
    if os.path.exists(dirPath):
        return dirPath
        pass
    else:
        os.mkdir(dirPath)
        return dirPath
