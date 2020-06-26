#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 08:36:33 2020

@author: jeancho
"""


import proj03library


def main():
    string1 = 'Hello'
    string2 = 'Hello123'
    string3 = '1234'
    
    #1: is_alpha()
    print('PART 1--is_alpha()')
    print(f'Testing "{string1}": {str(proj03library.is_alpha(string1))}')
    print(f'Testing "{string2}": {str(proj03library.is_alpha(string2))}')
    print(f'Testing "{string3}": {str(proj03library.is_alpha(string3))}')
    print('\n')
    
    #2: is_digit()
    print('PART 2--is_digit()')
    print(f'Testing "{string1}": {str(proj03library.is_digit(string1))}')
    print(f'Testing "{string2}": {str(proj03library.is_digit(string2))}')
    print(f'Testing "{string3}": {str(proj03library.is_digit(string3))}')
    print('\n')
    
    #3: to_lower()
    print('PART 3--to_lower()')
    print(f'Testing "{string1}": {str(proj03library.to_lower(string1))}')
    print(f'Testing "{string2}": {str(proj03library.to_lower(string2))}')
    print('\n')
    
    #4: to_upper()
    print('PART 4--to_upper()')
    print(f'Testing "{string1}": {str(proj03library.to_upper(string1))}')
    print(f'Testing "{string2}": {str(proj03library.to_upper(string2))}')
    print('\n')
    
    #5: find_chr()
    print('PART 5--find_chr()')
    print('Testing for "e" in ' + '"' + string1 + '"' + ':' + str(proj03library.find_chr(string1, 'e')))
    print('Testing for "o" in ' + '"' + string2 + '"' + ':' + str(proj03library.find_chr(string2, 'o')))
    print('\n')
    
    #6: find_str()
    print('PART 6--find_str()')
    print(f'Testing for "el" in "{string1}": ' + str(proj03library.find_str(string1, 'el')))
    print(f'Testing for "llo" in "{string2}": ' + str(proj03library.find_str(string2, 'llo')))
    print('\n')
    
    #7: replace_chr()
    print('PART 7--replace_chr()')
    print(f'Replace "e" in "{string1}" with "3": ' + str(proj03library.replace_chr(string1, 'e', '1')))
    print(f'Replace "3" in "{string3}" with "e": ' + str(proj03library.replace_chr(string3, '3', 'e')))
    print('\n')
    
    #8: replace_str()
    print('PART 8--replace_str()')
    print(f'Replace "ello" in "{string1}" with "3110": ' + str(proj03library.replace_str(string1, 'ello', '3110')))
    print(f'Replace "123" in "{string2}" with "abc": ' + str(proj03library.replace_str(string2, '123', 'abc')))
    print('\n')
    
    
    
    
    
    
#main   
if __name__ == "__main__":
    main()
    