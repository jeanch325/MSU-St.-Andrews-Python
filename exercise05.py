#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 10:21:48 2020

@author: jeancho
"""

import csv
from operator import itemgetter



def read_file(fp):
    '''
    Input: file pointer as an argument
    Output: a list of lists of the contents of each data row of 
    fp EXCEPT header, footnote, and empty rows.'''
    
    output_list = []
    reader = csv.reader(fp) # attaches a reader to the file fp
    next(reader,None) # skips a line, such as a header line
    for line_lst in reader: # line_lst is a list
        if line_lst[1] == 'Michigan':
            output_list.append(line_lst)
        elif line_lst[1] == 'New York':
            output_list.append(line_lst)
        elif line_lst[1] == 'Arizona':
            output_list.append(line_lst)
        elif line_lst[1] == 'Texas':
            output_list.append(line_lst)
        elif line_lst[1] == 'California':
            output_list.append(line_lst)
    return(output_list)


def get_totals(states, data):
    '''
    Input: list of lists returned by the read_file() function 
    Output: list of tuples values where each tuple is a state and total covid cases'''
    
    oplist = [[], [], [], [], []]
    for i in range(len(states)): 
        revdata = data[-1::-1]
        for mini in revdata:
            if mini[1] == states[i] and  len(oplist[i]) == 0:
                tup = (mini[1], mini[3])
                oplist[i] = tup
    return(oplist)



def get_spike_dates(states,data):
    '''
    Input: states list and list of lists returned by the read_file()
    Output: list of tuples; each tuple is: (state, date of spike, number of cases that date)'''
    oplist = [[],[],[],[],[]]
    for j in range(len(states)): 
        dayb4 = 0
        spike = 0
        date = ''
        for i in range(len(data)):
            if data[i][1] == states[j] and (int(data[i][3]) - dayb4) > spike:
                spike = (int(data[i][3]) - dayb4)
                date = data[i][0]
            if data[i][1] == states[j]:
                dayb4 = int(data[i][3])
        oplist[j] = tuple([states[j], date, spike])
    return(oplist)


def main():    

    states = ['Michigan','New York','Arizona','Texas','California']

    fp = open("covid-19-us-states.csv")
    file_data = read_file(fp)
    
    
    state_totals = get_totals(states, file_data)
    if state_totals:  # if their values are not None
        print("\nTotal Coronavius cases by state\n")
        print("{:24s} {:10s}".format("State","#Cases"))
        for tup in state_totals:
            print("{:24s} {:2}".format(tup[0],tup[1]))

    state_spikes = get_spike_dates(states, file_data)
    if state_spikes:  # if their values are not None
        print("\nDate of Coronavius spike by State \n")
        print("{:24s} {:10s} {:>8s}".format("State","Date","#Cases"))
        for tup in state_spikes:
            print("{:24s} {:10s} {:8d}".format(tup[0],tup[1],tup[2])) 

if __name__ == "__main__":
    main()

    
    
    
    
    


