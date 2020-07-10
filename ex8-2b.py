#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 10:03:25 2020

@author: jeancho
"""

###########################################################################
## Class Time
###########################################################################

class Time( object ):
    
    
    def __init__( self, hour=0, minute=0, sec=0 ):
        
        """ Construct a Time using three integers. """

        self.__hours = hour
        self.__mins = minute
        self.__secs = sec
    
    def __repr__( self ):
        
        """ Return a string as the formal representation a Time. """
        
        out_str = "Class Time: {:02d}:{:02d}:{:02d}" \
            .format( self.__hours, self.__mins, self.__secs )

        return out_str
    
    def __str__( self ):

        """ Return a string (hh:mm:ss) to represent a Time. """

        out_str = "{:02d}:{:02d}:{:02d}" \
            .format( self.__hours, self.__mins, self.__secs )

        return out_str
    
    def from_str( self, hms_str ):
        
        """ Convert a string hh:mm:ss into a Date. """
        
        hms_list = hms_str.split(':')
        self.__hours = int(hms_list[0])
        self.__mins   = int(hms_list[1])
        self.__secs  = int(hms_list[2])
        
        
def main():
    demo = Time()
    demo.from_str("7:12:03")
    print(demo)
    
    
if __name__ == '__main__':
    main()