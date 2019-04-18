# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 12:53:40 2019

@author: Dharmraj Rathod
"""
from statistics import mean
#from scipy import stats
#let we have the bottle filled with marbels and we have to guess how many number of marbles are 
#there in the bottle
"""total number of marbles in the bottle is 36"""

#implementation of trim_mean function from scipy
Guess = [30,35,20,15,40,45,38,45,50,50,70,37,15,55,25,28,26,28,20,30]
#for guess we use the trimmed percentage%(should be in 100)

def Rdtrim_mean(percentage,Guess):
    if(percentage > 100 or Guess == []):
        print("Please Enter the valid Arguments")
    percentage = percentage/100
    Guess.sort()
    trimmed_value =int( percentage*len(Guess) )
    #m = stats.trim_mean(Guess,0.1)
    Guess = Guess[trimmed_value:]
    Guess = Guess[:len(Guess)-trimmed_value]
    print("Actual Value May Near About = ",mean(Guess))
    #print(m)