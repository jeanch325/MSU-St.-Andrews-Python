#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 09:24:16 2020

@author: jeancho
"""
    ###########################################################
    #  proj05.py
    #
    #  Algorithm
    #    prompt for a year
    #    input a year(must be int)
    #    display py plot
    #    loop while x = 0
    #       prompt for range or percent
    #       output the range or percent that the year inputted is in
    #       if not in range, output error message
    ###########################################################


import pylab
    
def open_file():
    '''
    User inputs a year between 1990 and 2015.
    Opens yearXXXX.txt where XXXX is the year inputted.
    Continues to loop until valid year entered.
    Appropriate error message shown if file can'tt be opened or 
    if the year number is invalid'''
    not_valid_file = True
    while not_valid_file:
        year_str = input("Enter a year where 1990 <= year <= 2015: ")
        if year_str.isdigit():
            year_str = int(year_str)
            if year_str in range(1990, 2016):
                filename = 'year' + str(year_str) + '.txt'
                try:
                    outfile = open(filename, 'r')
                    not_valid_file = False
                except ValueError:
                    print("Error in year. Please try again.")
                except FileNotFoundError:
                    print("Error in file name:",filename," Please try again.")
    
        else:
            print("Error in year. Please try again.")
    return(outfile, int(year_str))
   
     
def read_file(outfile):
    '''
    Input: fp
    Output: list of lists with each mini list representing each column'''
    oplist = [[],[],[],[],[],[],[],[]]
    for line in outfile:
        if line[0].isdigit(): #to move past the top description
            line = line.split()
            for i in range(8):
                if line[i].isalpha():
                    line[i] = line[i]
                elif ',' in line[i]:
                    line[i] = float(line[i].replace(',', ''))
                elif '-' not in line[i]: #for column 1
                    line[i] = float(line[i])
                oplist[i].append(line[i])
    oplist[1][len(oplist[1]) - 1] = '-'
    oplist[2][len(oplist[2]) - 1] = '1,000,000,000,000'
    return oplist



def find_average(inptlist):
    '''
    Input: oplist from read_file()
    inplist[6] (wages) / inplist[4] (total num) = average salary
    Output: Average salary
    '''
    wagetotal = 0
    salarylist = inptlist[6]
    totalnum = inptlist[4][len(salarylist) - 1]
    for i in salarylist:
        wagetotal += float(i)    
    avg = wagetotal / totalnum
    return float('{:.2f}'.format(avg))


    
def find_median(inptlist):
    '''
    Input: oplist from read_file()
    Output: median wage
    '''
    return get_range(inptlist, 50)[2]


        
def get_range(inptlist, percent):
    '''
    Input: oplist from read_file()
    Takes inputted % and look at index in col5 where col5 % is >= inputted %
    Output: item's index in col0, col2 for salary range; col5 % that is >= input%, item's index in
            col7 for average income
            tuple((col0, col2), col5, col7)'''
    c5 = inptlist[5]
    ind = None
    stop = 0
    for i, value in enumerate(c5):
        if value >= percent and stop == 0:
            ind = i
            stop = 1
    outlist = [inptlist[0][ind], inptlist[2][ind], c5[ind], inptlist[7][ind]]
    salrange = [outlist[0], outlist[1]]
    return tuple(salrange), outlist[2], outlist[3]


def get_percent(inptlist,salary):
    '''
    Input: oplist from read_file() and a salary amount
    Output: cumulative % (col5) of the salary range the salary amount inputted
            is in; range the salary amount is in(col0 and col2)
            (tuple(col0, col2), col5)
        '''
    ranlis = []
    ind = None
    for i in range(len(inptlist[0])):
        ranlis.append([inptlist[0][i], inptlist[2][i]])
    for j, sublist in enumerate(ranlis):
        if salary >= sublist[0] and salary <= sublist[1]:
            ind = j
    salrange = [ranlis[ind][0], ranlis[ind][1]]    
    return(tuple(salrange), inptlist[5][ind])



def do_plot(x_vals,y_vals,year):
    '''Plot x_vals vs. y_vals where each is a list of numbers of the same length.'''
    pylab.xlabel('Income')
    pylab.ylabel('Cumulative Percent')
    pylab.title("Cumulative Percent for Income in "+str(year))
    pylab.plot(x_vals,y_vals)
    pylab.show()

def main():
    fp = open_file()
    inptlist = read_file(fp[0])
    year = fp[1]
    avg = find_average(inptlist)
    median = find_median(inptlist)    
    print("\n{:<6s}${:<14s}{:<14s}".format('Year', 'Mean', 'Median'))
    print("\n{:<6d}${:<14,.2f}${:<14,.2f}".format(year, avg, median))
    
    response = input("Do you want to plot values (yes/no)? ")
    if response.lower() == 'yes':
        x_vals = inptlist[0][:40]
        y_vals = inptlist[5][:len(x_vals)]
        do_plot(x_vals, y_vals, year)
    elif response.lower() != 'no':
        print("Invalid response")
        
    x = 0 #for the loop
    
    while x == 0:
        choice = input("Enter a choice to get (r)ange, (p)ercent, or nothing to stop: ")
        if choice.lower() == 'r':
            percent = float(input('Enter a percentile: '))
            if percent <= 100 and percent > 0:
                r_range = get_range(inptlist, percent)[0][0]
                print('{:4.2f}% of incomes are below ${:<13,.2f}'.format(percent, r_range))
            else:
                print("Error: income must be positive")
        elif choice.lower() == 'p':
            salary = input('Enter an income: ')
            if not salary.isdigit():
                print('Invalid salary input. Remove all non numeric characters')
            elif float(salary) > 0:
                salary = float(salary)
                p_percent = get_percent(inptlist, salary)[1]
                print("An income of ${:<13.2f} is in the top {:4.2f}% of incomes".format(salary, p_percent))
            else:
                print("Error: income must be positive")
        elif choice == '':
            x = 1
        else:
            print("Error in selection.")
           

if __name__ == "__main__":
    main()





