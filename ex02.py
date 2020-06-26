#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 16:05:18 2020

@author: jeancho
"""

x = True

while x == True:
    vowels = 'aeiou'
    word = str(input("Enter a word: ").lower())
    if word[0] in vowels:
        print(f'Pig Latin version: {word}way')

    elif word == 'quit':
        x = False
    
    else:
        stop = 0
        for i, char in enumerate(word):
            if stop == 0:
                if char in vowels:
                    print(f'Pig Latin version: {word[i:] + word[0:i]}ay')
                    stop = 1
                        
print('Program terminated')
