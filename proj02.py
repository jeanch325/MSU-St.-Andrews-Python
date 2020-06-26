#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 18:07:12 2020

@author: jeancho
"""
x = False

#Input strings
str1 = str(input('Input the first string: ')).lower()
str2 = str(input('Input the second string: ')).lower()

#beginning program
while x == True:

    uinput = str(input('''What do you want to do?
                       a: add indel
                       d: delete indel
                       s: show score
                       q: quit
                       ''')).lower()
                       
    #add
    if uinput == 'a':
        pickstr = input('Enter 1 for string 1 or 2 for string 2: ')
        pickindex = int(input('Enter the index where you want to add an indel: '))
        if pickstr == '1' and pickindex <= len(str1):
            str1 = str1[:pickindex] + '-' + str1[pickindex:]
            
        elif pickstr == '2' and pickindex <= len(str2):
            str2 = str2[:pickindex] + '-' + str2[pickindex:]
            
        else:
            print('Invalid input')
    
    #delete
    elif uinput == 'd':
        pickstr = input('Enter 1 for string 1 or 2 for string 2: ')
        pickindex = int(input('Enter the index where you want to delete an indel: '))
        if pickstr == '1':
            if str1[pickindex] != '-':
                print("Invalid input. No indel found")
            else:
                str1 = str1[:pickindex] + str1[pickindex + 1:]
                
        elif pickstr == '2':
            if str2[pickindex] != '-':
                print("Invalid input. No indel found")
            else:
                str2 = str2[:pickindex] + str2[pickindex + 1:]
                
        else:
            print('Invalid input')
            
    #score
    elif uinput == 's':
        mismats = 0
        if len(str1) < len(str2): 
            difference = len(str2) - len(str1)
            str1 = str1 + ('-' * difference)
        elif len(str2) < len(str1): 
            difference = len(str1) - len(str2)
            str2 = str2 + ('-' * difference)
        for i, char in enumerate(str1):
            if str2[i] != char:
                mismats += 1
                str1 = str1[:i] + str1[i].upper() + str1[i + 1:]
                str2 = str2[:i] + str2[i].upper() + str2[i + 1:]                
        if str1[-1] == '-' and str2[-1] == '-':
            str1 = str1[:len(str1) - 1]
            str2 = str2[:len(str2) - 1]
        mats = len(str1) - mismats
        print(f'Matches: {mats}  Mismatches: {mismats}')
        print(f'String 1: {str1}   String 2: {str2}')         
            
    #quit        
    elif uinput == 'q':
        print("Program terminated")
        x = False
        
    #else
    else:
        print('Unrecognizable input.')
        
        

        