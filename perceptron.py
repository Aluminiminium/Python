# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 17:09:36 2018

@author: Tanaka-Lab-Desktop4
"""

import numpy as np

x = np.array([0, 1])
w = np.array([0.5, 0.5])
b = -0.7
 
print(w*x)

print(np.sum(w*x))

print(np.sum(w*x) + b)