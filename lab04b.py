#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 20:49:03 2020

@author: jeancho
"""
    
#PART B
 
#FUNCTIONS
def avg(total, num):
    av = total / num
    return av
def find_bmi(w, h):
    bmi_result = w / (h ** 2)
    return float(f'{bmi_result}')



def write_data_file():
    
    #OPEN FILE
    outfile = open("data_output.txt", "w")
    data_textfile = open("data.txt", "r")
    
    #VARIABLES
    name = ''
    height = ''
    height_sum = 0
    height_av = 0
    height_min = 10 ** 6
    height_max = 0
    weight = ''
    weight_sum = 0
    weight_av = 0
    weight_min = 10 ** 6
    weight_max = 0
    bmi_max = 0
    bmi_min = 10 ** 6
    datanum = 0
   
    
    #CODE
    data = data_textfile.readlines()[1:]
    outfile.write('{:<12s}{:<12s}{:<12s}{:<12s}'.format('Name', 'Height(m)', 'Weight(kg)', 'BMI'))
    for line in data:
        #datanum
        datanum += 1
        line = line.strip()
        
        #variables
        name = str(line[:12].strip())
        height = float(line[12:24].strip())
        weight = float(line[24:].strip())
        height_sum = height_sum + height  
        weight_sum = weight_sum + weight
        
        #min/max
        if height < height_min:
            height_min = height
        if weight < weight_min:
            weight_min = weight
        if height > height_max:
            height_max = height 
        if weight > weight_max:
            weight_max = weight
        
        #bmi
        bmi = find_bmi(weight, height)
        outfile.write(f'\n{name:<12s} {height:<12.2f} {weight:<12.2f} {bmi:<12.2f}')
        if bmi < bmi_min:
            bmi_min = bmi
        if bmi > bmi_max:
            bmi_max = bmi
        
    height_av = avg(height_sum, datanum)
    weight_av = avg(weight_sum, datanum)
    bmi_av = find_bmi(weight_av, height_av)
    outfile.write('\n{:<13s}{:<13s}{:<13s}{:<12s}'.format('Average', f'{height_av}', f'{weight_av}', f'{bmi_av:<12.2f}'))
    outfile.write('\n{:<13s}{:<13s}{:<13s}{:<12s}'.format('Maximum', f'{height_max}', f'{weight_max}', f'{bmi_max:<12.2f}'))
    outfile.write('\n{:<13s}{:<13s}{:<13s}{:<12s}'.format('Minimum', f'{height_min}', f'{weight_min}', f'{bmi_min:<12.2f}'))
         
    #Close files
    outfile.close()
    data_textfile.close()
    


#Print     
if __name__ == "__main__":
    write_data_file()
    