# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 16:42:49 2024

@author: komoto_univ
"""

a = 1e+16
b = 1e+16

a += 100000000 #1e+8

for i in range(100000000 ):
    b += 1
    
print(a)
print(b)

print(0.1 + 0.1  == 0.2 )
print(0.1 + 0.1 + 0.1 == 0.3 )