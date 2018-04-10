# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 17:33:53 2018

@author: Tanaka-Lab-Desktop4
"""

import numpy as np

x = np.array([-1.0, 1.0, 2.0])
print(x)

y = x > 0
y = y.astype(np.int)
print( y )