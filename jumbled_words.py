# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 18:45:27 2019

@author: Dharmraj Rathod
"""
import random 
def choose():
    words = ['computer','counting','factorial','design','mathematics','programming','reverse','algorithms']
    pick = random.choice(words)
    return pick
def jumble(word):
    jumbled ="".join(random.sample(word,len(word)))
    return jumbled;
def thanks(p1_name,p2_name,p1_point,p2_point):
    print(p1_name,"Your Score is ",p1_point)
    print(p2_name,"Your Score is ",p2_point)
    print("Thank you For Playing")
def Play():
    p1_name = input("Player 1 : Enter your name :")
    p2_name = input("Player 2 : Enter your name :")
    p1_point = 0
    p2_point = 0
    flag = 0
    while(1):
        picked_word = choose()
        question = jumble(picked_word)
        # for Player 1
        if(flag == 0):
            print(p1_name,"your Question is :",question)
            guess_word = input("Enter your Answer :")
            if(picked_word == guess_word):
                print("You Are Absolutly Right..")
                p1_point +=1
                print("Your Score is :",p1_point)
                flag = 1
            else:
                print("Better Luck Next Time :",picked_word)
                flag = 1
            again =input("Do You Want to Continue..y/n")
            if(again == 'n'):
                thanks(p1_name,p2_name,p1_point,p2_point)
                break
        else:
            # for Player 1
            print(p2_name,"your Question is :",question)
            guess_word = input("Enter your Answer :")
            if(picked_word == guess_word):
                print("You Are Absolutly Right!")
                p2_point +=1
                print("Your Score is :",p1_point)
                flag = 0
            else:
                print("Better Luck Next Time :",picked_word)
                flag = 0
            again =input("Do You Want to Continue..y/n")
            if(again == 'n'):
                thanks(p1_name,p2_name,p1_point,p2_point)
                break