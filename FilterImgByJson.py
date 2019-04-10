# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 17:38:14 2019

@author: LiYalin
"""

import os
import json
import cv2

     
def listdir(path, list_name):  #传入存储的list
    for file in os.listdir(path):  
        file_path = os.path.join(path, file)  
        if os.path.isdir(file_path):  
            listdir(file_path, list_name)  
        else:  
            list_name.append(file_path)
fn= []  
fn_img = []        
filepath = "F://CPro//openpose-1.4.0-win64-cpu-binaries//output"
filepath_img = "F://CPro//openpose-1.4.0-win64-cpu-binaries//1"
listdir(filepath, fn)
listdir(filepath_img, fn_img)
l= len(fn)        

for i in range(l):
    json_dat = fn[i]
    img_ori = fn_img[i]
    Img = cv2.imread(img_ori)
    with open(json_dat, encoding='utf-8') as f:
        json_data = json.load(f)
        if len(json_data['people']) >0 and len(json_data['people']) <10:
            keypoints = json_data['people'][0]['pose_keypoints_2d']
            if keypoints.count('0') >30 or keypoints[0:3] ==[0,0,0] or keypoints[3:6] ==[0,0,0]:
                cv2.imwrite(filepath_img[:-1] + '3/'+ fn_img[i][47:], Img)
                os.remove(img_ori)
        else:
            #print(filepath_img[:-1])
            #print(fn_img[i][47:])

            cv2.imwrite(filepath_img[:-1] + '3/'+ fn_img[i][47:], Img)
            os.remove(img_ori)
