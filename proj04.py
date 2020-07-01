#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 09:18:15 2020

@author: jeancho
"""
    ###########################################################
    #  proj04.py : GDP
    #
    #  Algorithm
    #    prompt for a filename
    #    input an existing filename
    #    try until filename exists (GDP.txt)
    #       call functions to find min/max percent, gdp, year
    #       output min_val, min_year, min_val_gdp, max_val, max_year, max_val_gdp       
    ###########################################################

def open_file(): 
    '''Repeatedly prompt until a valid file name allows the file to be opened.'''
    not_valid_file = True
    while not_valid_file:
        file = input('Enter a filename: ')
        try:
            outfile = open(file, 'r')
            not_valid_file = False
        except FileNotFoundError:
            print('Invalid filename. Please try again.')
    return outfile

   
def find_min_percent(file, line_num):
    '''Find the min percent change in the line; return the value and the index.'''
    line = file[line_num - 1]
    min_value = 10 ** 6
    min_value_index = None
    for i in range(47):
        value = float(line[76 + (12 * i) : 76 + (12 * (i + 1))].strip())
        if value < min_value:
            min_value = value
            min_value_index = i
    return(min_value, min_value_index)

def find_max_percent(file, line_num):
        '''Find the max percent change in the line; return the value and the index.'''
        line = file[line_num - 1]
        max_value = 0
        max_value_index = None
        for i in range(47):
            value = float(line[76 + (12 * i) : 76 + (12 * (i + 1))].strip())
            if value > max_value:
                max_value = value
                max_value_index = i
        return(max_value, max_value_index)

def find_gdp(file, line_num, index):
    '''Use the index to find the gdp value in the line; return the value'''
    line = file[line_num - 1]
    gdp = line[76 + (12 * index) : 76 + (12 * (index + 1))]
    return(gdp)  

def find_year(file, index):
    line = file[42]
    year = line[76 + (12 * index) : 76 + (12 * (index + 1))]
    return(year) 

        
def display(min_val, min_year, min_val_gdp, max_val, max_year, max_val_gdp):
    '''Display values; convert billions to trillions first.'''    
    print("{:<10s}{:>8.1f}{:>6s}{:>18.2f}".format('Min', min_val, min_year, (float(min_val_gdp) * 0.001)))
    print("{:<10s}{:>8.1f}{:>6s}{:>18.2f}".format('Max', max_val, max_year, (float(max_val_gdp) * 0.001)))
    
def main():
    outfile = open_file().readlines()   
    min_val = find_min_percent(outfile, 9)[0]
    min_year = find_year(outfile, find_min_percent(outfile, 9)[1])
    min_val_gdp = find_gdp(outfile, 44, find_min_percent(outfile, 9)[1])
    max_val = find_max_percent(outfile, 9)[0]
    max_year = find_year(outfile, find_max_percent(outfile, 9)[1])
    max_val_gdp = find_gdp(outfile, 44, find_max_percent(outfile, 9)[1])
    print('\nGross Domestic Product')
    print('{:<10s}{:>8s}{:>7s}{:>25s}'.format("Min/Max", 'Change', 'Year', 'GDP(trillions)'))
    display(min_val, min_year, min_val_gdp, max_val, max_year, max_val_gdp)


# Calls the 'main' function only when you execute within Spyder (or console)
# Do not modify the next two lines.
if __name__ == "__main__":
    main()
