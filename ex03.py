#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 12:59:12 2020

@author: jeancho
"""
#ex03.py

#Part A
def leap_year(year):
    '''
    Leap year calculator
    Value: integer input
    Returns: True or False
    '''
    if int(year) % 400 == 0:
        return True
    elif int(year) % 4 == 0 and year % 100 != 0:
        return True
    else:        
        return False

#Part B
def rotate(s,n):
    '''
    Rotates string
    Value: string input s, integer input n
    Returns: rotated string; last n characters moved to beginning
    '''
    n = int(n)
    s = str(s)
    if len(s) <= 1:
        return s
    elif n > 0 and n <= len(s):
        return s[len(s) - n :] + s[:len(s) - n]
    else:
        print('Input larger than string length')
                
#Part C:
def digit_count(num):
    '''
    Counts digits
    Value: int or float
    Returns: count of even & odd digits and zeros left of decimal point
    '''
    evens = 0
    odds = 0
    zeroes = 0
    num = int(num)
    for i in str(num): 
        if i != '.':
            if int(i) % 2 == 0 and int(i) != 0:
                evens += 1
            elif int(i) == 0:
                zeroes += 1
            else:
                odds += 1
    return(evens, odds, zeroes)
    
#Part D:
def float_check(digits):
    '''
    Checks for floats
    Value: integers or floats with digits
    Returns: True or False
    '''
    dotcount = 0
    digits = str(digits)
    if digits.isdigit():
        return True
    for i in digits:
        if i == '.':
            dotcount += 1
        elif not i.isdigit() and i != '.': 
            return False
    if dotcount > 1:
        return False
    return True
    
#Code start: 
if __name__ == '__main__':
    print(leap_year(1896))
    print(rotate('abcdefgh', 3))
    print(digit_count(0.123))
    print(float_check('123.45'))

































 
        
