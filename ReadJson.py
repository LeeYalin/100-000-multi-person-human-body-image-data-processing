# -*- coding: utf-8 -*-

import json

f = open("F:/Data/coco/annotations_trainval2017/annotations/person_keypoints_val2017.json",encoding = 'utf-8')
f1 = open("G:/codesave/lyl0/data/json/val/000001.json",encoding = 'utf-8')
t = json.load(f)
r = json.load(f1)
