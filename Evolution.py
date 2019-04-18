# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 01:14:23 2019

@author: Dharmraj Rathod
"""
import random
def evolve(data):
    index = random.randint(0,len(data)-1)
    p = random.randint(1,10)
    print(p)
    if(p == 1):
        print(index,"1 occure",data[index])
        if(data[index] == '0'):
            data[index] = '1'
        else:
            data[index] = '0'
with open('dna_data.txt','r+') as binary_file:
    data = binary_file.read()
    data = list(data)
    print(data)
for i in range(len(data)):
    evolve(data)
print(data)
