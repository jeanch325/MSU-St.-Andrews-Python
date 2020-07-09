#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 13:27:16 2020

@author: jeancho
"""

def build_map( in_file1, in_file2 ):
    '''
    Parameters
    ----------
    in_file1 : Text file
        CONTINENTS AND COUNTRIES
    in_file2 : Text file
        COUNTRIES AND CITIES

    Returns
    -------
    data_map : nested dictionary -> dictionary{dictionary{list[]}}
        {KEY-Continent : VALUE-{KEY-Country : VALUE-[City]}}
    '''
    
    data_map = {}
    in_file1.readline()
    in_file2.readline()
    
    #READ EACH LINE FROM FILE 1

    for line in in_file1: # Split the line into two words
        continent_list = line.strip().split()
        
        # Convert to Title case, discard whitespace
        continent = continent_list[0].strip().title()
        country = continent_list[1].strip().title()
        
        country_map = {}
        country_map[country] = []
        
        if continent != "" and continent not in data_map: # Ignore empty strings
            # If current continent not in map, insert it 
            # YOUR CODE
            data_map[continent] = country_map
        elif continent != '':
            temp_map = data_map[continent]
            temp_map[country] = []
            data_map[continent] = temp_map        
    

    #READ EACH LINE FROM FILE 2
    for line in in_file2: # Split the line into two words
        countries_list = line.strip().split()
        
        # Convert to Title case, discard whitespace
        country = countries_list[0].strip().title()
        city = countries_list[1].strip().title()
        
            
            # insert city (country is guaranteed to be in map)
        for continent in data_map:
            if country in data_map[continent]:
                # YOUR CODE
                map_country = data_map[continent]
                l_city = map_country[country]
                if city not in l_city:
                    l_city.append(city)
    return data_map




def display_map( data_map ):
    '''
    Parameters
    ----------
    data_map : Nested dictionary

    Returns
    -------
    Print output w formatting
    '''
    
    # Modify this code to display a sorted nested dictionary
    continents_list = list(data_map.keys()) #sorted list of the continent keys
    # For each continent
    for continent in continents_list:
        print(f'{continent}: ') #continents in continents_list
        countries_list = list(data_map[continent].keys())
        #print(countries_list)#sorted list of the countries keys in the continents
        for country in countries_list: # For each country
            print("{:>10s} --> ".format(country),end = '') #countries in countries_list
            cities_list = list(data_map[continent][country]) #sorted list of the cities
            for city in cities_list: # For each city 
                if len(cities_list) == 1 or city == cities_list[len(cities_list) - 1]:# if it is the last, don't add a comma and a space.
                    print('{}'.format(city))
                # city in cities      
                else: #As long as not last city, add a comma and a space after the cities names
                    print('{}, '.format(city),end = ' ')

        print('\n')
             

def open_file():

    try:
        filename = input("Enter file name: ")
        in_file = open( filename, "r" )
        
    except IOError:
        print( "\n*** unable to open file ***\n" )
        in_file = None

    return in_file

def main():

    #Asking for file names
    data_map = {}
    in_file1 = open_file() #Continents with countries file: continents.txt
    in_file2 = open_file() #Countries with cities file: cities.txt

    if in_file1 != None and in_file2 != None:
        
        data_map = build_map( in_file1, in_file2 ) # data_map is a dictionary
        display_map( data_map )
        in_file1.close()
        in_file2.close()

if __name__ == "__main__":
    main()

