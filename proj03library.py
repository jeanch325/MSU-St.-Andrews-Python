#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 13:28:36 2020

@author: jeancho
"""
#proj03library.py 

#CONSTANTS
ASCII_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
ASCII_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DECIMAL_DIGITS = "0123456789"

#FUNCTIONS

#1
def is_alpha(string):
    #returns True if all str characters are upper/lower case ASCII; returns False otherwise
    x = True
    for i in string:
        if i not in ASCII_LOWERCASE and  i not in ASCII_UPPERCASE:
            x = False  
    if x == True:
        return True
    else:
        return False
    
#2
def is_digit(string):
    #returns True if all str characters are ASCII decimal digits; returns False otherwise
    x = True
    for i in string:
        if i not in DECIMAL_DIGITS:
            x = False
        
    if x == True:
        return True
    else:
        return False
        
 
#3
def to_lower(string):
    #returns str copy of the parameter, but all lower case ASCII letters
    for i in range(len(string)):
        if string[i] in ASCII_UPPERCASE:
            newindex = find_chr(ASCII_UPPERCASE, string[i])
            string = string[:i] + ASCII_LOWERCASE[newindex] + string[i + 1:]
    return string
    
       
 #4   
def to_upper(string):
    #returns str copy of the parameter, but all upper case ASCII letters
    for i in range(len(string)):
        if string[i] in ASCII_LOWERCASE:
            newindex = find_chr(ASCII_LOWERCASE, string[i])
            string = string[:i] + ASCII_UPPERCASE[newindex] + string[i + 1:]
        
    return string
    
    
#5   
def find_chr(string, char):
    #returns lowest index where second parameter is found in first parameter 
    #returns -1 if the second parameter is over 1 letter or is not found in first parameter
    if len(char) != 1:
        return('-1')
    elif char not in string:
        return('-1')
    else: #if char in string& char is 1 character
        stop = 0
        for i in range(len(string)):
            if stop == 0:
                if string[i] == char:
                    return(i)
    
#6
def find_str(str1, str2):
    #returns lowest index where second parameter is found in first parameter 
    #returns -1 if the second parameter is not found in first parameter
    if str2 not in str1 or len(str2) > len(str1): 
        return('-1')
    else:
        x = 0
        loop = 0
        str1_ind = 0
        for j in str1: 
            if loop == 0:
                if j == str2[0]:
                    for i in range(len(str2)):
                        if str2[i] == str1[str1_ind + i]:            
                            x += 1
                    if x == len(str2):
                        loop = 1
                    else: 
                        str1_ind += 1
                else:
                    str1_ind += 1
        return str1_ind
    
#7  
def replace_chr(str1, str2, str3):
    #second and third parameters must be of length 1
    #replaces all occurrences of 2nd parameter w 3rd parameter in the 1st parameter  
    if len(str2) != 1 or len(str3) != 1:
        return('-1')
    elif str2 not in str1:
        return('-1')
    else: 
        for i in range(len(str1)):
                if str1[i] == str2:
                    str1 = str1[:i] + str3 + str1[i + 1:]
        return(str1) 
    
#8
def replace_str(str1, str2, str3):
    #replaces all occurrences of 2nd parameter w 3rd parameter in the 1st parameter  
    #If no occurrences of 2nd parameter in 1st, returns copy of 1st parameter
    #If 2nd parameter is the empty string, returns :
    #1st parameter, but w 3rd parameter inserted before the 1st character, 
    #between each character, and after the last character. 
    if str2 not in str1:
        return(str1)
    elif str2 == '':
        str3_copy = str3
        for i in range(len(str1)):
             str3 = str3_copy + str1[i] + str3
        print(str3[::-1])
        return(str3[::-1])
    elif str2 in str1:
        if str2 in str1:
            for i in range(len(str1)):
                if str1[i : i + len(str2)] == str2:
                    str1 = str1[:i] + str3 + str1[i + len(str2) :]
        return(str1)
    
   
