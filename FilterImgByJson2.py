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
#fn_img = []
filepath = "F://CPro//openpose-1.4.0-win64-cpu-binaries//output"

listdir(filepath, fn)
#listdir(filepath_img, fn_img)
l= len(fn)        

for i in range(l):
    json_dat = fn[i]
    img_ori1 = "F://CPro//openpose-1.4.0-win64-cpu-binaries//1//" + fn[i][52:-15] +".jpg"
    img_ori2 = "F://CPro//openpose-1.4.0-win64-cpu-binaries//1//" + fn[i][52:-15] +".png"
    img_ori3 = "F://CPro//openpose-1.4.0-win64-cpu-binaries//1//" + fn[i][52:-15] +".bmp"
    img_ori4 = "F://CPro//openpose-1.4.0-win64-cpu-binaries//1//" + fn[i][52:-15] +".JPG"
    img_ori5 = "F://CPro//openpose-1.4.0-win64-cpu-binaries//1//" + fn[i][52:-15] +".jpeg"
    img_ori6 = "F://CPro//openpose-1.4.0-win64-cpu-binaries//1//" + fn[i][52:-15] +".JPEG"
    img_ori7 = "F://CPro//openpose-1.4.0-win64-cpu-binaries//1//" + fn[i][52:-15] +".BMP"
    img_ori8 = "F://CPro//openpose-1.4.0-win64-cpu-binaries//1//" + fn[i][52:-15] +".PNG"

    if os.path.exists(img_ori1):
        Img = cv2.imread(img_ori1)
        img_ori = img_ori1
    elif os.path.exists(img_ori2):
        Img = cv2.imread(img_ori2)
        img_ori = img_ori2
    elif os.path.exists(img_ori3):
        Img = cv2.imread(img_ori3)
        img_ori = img_ori3
    elif os.path.exists(img_ori4):
        Img = cv2.imread(img_ori4)
        img_ori = img_ori4
    elif os.path.exists(img_ori5):
        Img = cv2.imread(img_ori5)
        img_ori = img_ori5
    elif os.path.exists(img_ori6):
        Img = cv2.imread(img_ori6)
        img_ori = img_ori6
    elif os.path.exists(img_ori7):
        Img = cv2.imread(img_ori7)
        img_ori = img_ori7
    elif os.path.exists(img_ori8):
        Img = cv2.imread(img_ori8)
        img_ori = img_ori8
    else:
        continue
    with open(json_dat, encoding='utf-8') as f:
        json_data = json.load(f)
        if len(json_data['people']) >0 and len(json_data['people']) <10:
            keypoints = json_data['people'][0]['pose_keypoints_2d']
            ccc = keypoints.count(0)
            if keypoints.count(0) >30:

                cv2.imwrite("F://CPro//openpose-1.4.0-win64-cpu-binaries//3//" + img_ori[48:], Img)
                os.remove(img_ori)
        else:

            cv2.imwrite("F://CPro//openpose-1.4.0-win64-cpu-binaries//4//" + img_ori[48:], Img)
            os.remove(img_ori)
