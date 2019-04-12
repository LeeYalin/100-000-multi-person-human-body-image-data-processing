# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 18:38:44 2019

@author: LiYalin
"""

import h5py
import json

aa = str(int('0001'))
it = h5py.File('G://lin0//training//Data@Body//MP_val_dataset.h5','r')

it.keys()
point = it['dataset']

print(point)
for i in range(13):
    z = str(i).zfill(7)
    pp = point[z]
    v = json.loads(pp.value)
    vv = json.loads(pp.attrs['meta'])
    print(v)
    print(vv)
