# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 10:23:43 2018

@author: Administrator
"""

import cv2

img_root = 'G://CPP//heartoutD//save//res//'#这里写你的文件夹路径，比如：/home/youname/data/img/,注意最后一个文件夹要有斜杠
fps = 5    #保存视频的FPS，可以适当调整
size=(640,480)
#可以用(*'DVIX')或(*'X264'),如果都不行先装ffmepg: sudo apt-get install ffmepg
fourcc = cv2.VideoWriter_fourcc(*'XVID')
videoWriter = cv2.VideoWriter('F:/li.avi',fourcc,fps,size)#最后一个是保存图片的尺寸

#for(i=1;i<471;++i)
#for i in range(50,420):
for i in range(1,96):
    frame = cv2.imread(img_root+str(i)+'.jpg')
    videoWriter.write(frame)
videoWriter.release()
