# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 01:30:53 2019

@author: Dharmraj Rathod
"""
from scipy import stats
import statistics
import matplotlib.pyplot as gph
Guess = [30,35,20,15,40,45,38,45,50,50,70,37,15,55,25,28,26,28,20,30]
#gph.plot(Guess,'b--')
gph.xlabel("Guess")
a=[]
for i in range(len(Guess)):
    a.append(3)
gph.plot(Guess,a,'r--')
m = stats.trim_mean(Guess,0.1)
median = statistics.median(Guess)
gph.plot(m,3,'gs')
gph.plot(median,3,'bs')    
    
