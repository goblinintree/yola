 # -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os 


def GetFileList(FindPath,FlagStr=[]): 
    FileList=[] 
    FileNames=os.listdir(FindPath) 
    if (len(FileNames)>0): 
        for fn in FileNames: 
            if (len(FlagStr)>0): 
                #返回指定类型的文件名
                if (IsSubString(FlagStr,fn)):
                    fullfilename=os.path.join(FindPath,fn)
                    FileList.append(fullfilename)
            else: 
                #默认直接返回所有文件名
                fullfilename=os.path.join(FindPath,fn)
                # print type(fullfilename) 
                FileList.append(fullfilename)
            #对文件名排序
        if (len(FileList)>0):
            FileList.sort()
            
    return FileList

def list_file(FindPath,FlagStr=[]): 
    FileList=[] 
    FileNames=os.listdir(FindPath) 
    if (len(FileNames)>0): 
        for fn in FileNames: 
            if (len(FlagStr)>0): 
                #返回指定类型的文件名
                if (IsSubString(FlagStr,fn)):
                    # fullfilename=os.path.join(FindPath,fn)
                    fullfilename=fn
                    FileList.append(fullfilename)
            else:
                #默认直接返回所有文件名
                # fullfilename=os.path.join(FindPath,fn)
                fullfilename=fn
                FileList.join(fullfilename.encode("UTF-8"))
            #对文件名排序
        if (len(FileList)>0):
            FileList.sort()
    return FileList


def IsSubString(SubStrList,Str): 
    ''''' 
    #判断字符串Str是否包含序列SubStrList中的每一个子字符串 
    #>>>SubStrList=['F','EMS','txt'] 
    #>>>Str='F06925EMS91.txt' 
    #>>>IsSubString(SubStrList,Str)#return True (or False) 
    '''
    flag=True
    for substr in SubStrList: 
        if not(substr in Str): 
            flag=False
    return flag 