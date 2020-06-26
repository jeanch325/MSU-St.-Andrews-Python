#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 13:24:21 2020

@author: jeancho
"""

machine_on = True

while machine_on == True:
    customer_code = str(input('Customer Code: '))
    if customer_code.lower() == 'r' or  customer_code.lower() == 'c' or customer_code.lower() == 'i':
        bmeter = float(input('Beginning meter reading: '))
        emeter = float(input('End meter reading: '))
        gused = None
        if emeter < bmeter:
            gused = emeter + (1000000000.0 - bmeter)
        else:
            gused = emeter - bmeter
        bill = 0
        
        
        if customer_code.lower() == 'r':
            bill = 5.0 + 0.0005 * gused
    
        elif customer_code.lower() == 'c':
            if gused <= 4000000.0:
                bill = 1000.0 
    
            else:
                bill = 1000.0 + 0.00025 * (gused - 4000000.0)
    
        else:
            if gused <= 4000000.0:
                bill = 1000.0
    
            elif gused > 4000000.0 and gused <= 10000000.0:
                bill = 2000.0 
    
            else: 
                bill = 2000.0 + 0.00025 * (gused - 10000000)
        print(f'Customer Code: {customer_code}')
        print(f'Beginning meter reading: {str(int(bmeter)).zfill(9)}')
        print(f'End meter reading: {str(int(emeter)).zfill(9)}')
        print(f'Gallons used: {(gused * 0.1) :.1f}') 
        print(f'Bill: ${bill :.2f}')            
      
    else:
        print('invalid code')
    