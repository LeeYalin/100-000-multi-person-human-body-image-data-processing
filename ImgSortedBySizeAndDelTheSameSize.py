# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:21:21 2019

@author: LiYalin
"""
import os
import cv2

count = 0
fn= []
fn1 = []

def listdir(path, list_name):  #传入存储的list
    for file in os.listdir(path):  
        file_path = os.path.join(path, file)  
        if os.path.isdir(file_path):  
            listdir(file_path, list_name)  
        else:  
            list_name.append(file_path)
       
            
filepath = "F://crawler//poseFull//ori"
listdir(filepath, fn)
l= len(fn)        
for i in range(l):

    filesize = os.path.getsize(fn[i])
    fn1.append(filesize)
    
    
a = dict(zip(fn,fn1))
#print(a.items())
sortfileDict = sorted(a.items(), key=lambda a:a[1], reverse = True)
    
for i in range(l-1):
    k= i+1
    if sortfileDict[i][1] == sortfileDict[k][1]:
        #print(str(sortfileDict[i][0])[:23]+"1//" +str(sortfileDict[i][0])[27:])
        Img = cv2.imread(sortfileDict[i][0])
        cv2.imwrite(str(sortfileDict[i][0])[:23]+"1//" +str(sortfileDict[i][0])[27:], Img)
        os.remove(sortfileDict[i][0])
        count += 1

        
print(count)
