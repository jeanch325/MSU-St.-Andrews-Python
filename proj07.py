#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 14:07:39 2020

@author: jeancho
"""


def open_file():
    '''
    Returns
    -------
    document
    '''
    doc = open('ap_docs.txt', 'r')
    return(doc)


def list_file(doc):
    '''
    Parameters
    ----------
    doc : document
        output from open_file().

    Returns
    -------
    1) doclist: list of lists, with each mini list being one 'document'. 
        The elements of the mini list are single words.
    2) docset: list of sets, with each set being a set version of the mini
        lists from the list of lists. The sets have no punctuation and 
        are all lowercase.
    '''
    #Outputs
    doclist = []
    docset = [] 
    
    newlist = []
    
    for line in doc:
        split_line = line.split() #split lines into lists with word elements
        if len(split_line) == 0:
            newlist = newlist
        elif '<' not in split_line[0]: #skipping past <NEW DOCUMENT>
            newlist += split_line    
        else:
            doclist.append(newlist)
            newlist = []
    doclist.append(newlist)
          
    templist = doclist.copy()
    for item in templist:
        set_item = item.copy()
        set_word = ''
        for i, word in enumerate(set_item):
            if not word.islower():
                lower_word = word.lower()
                set_word = word.replace(word, lower_word)
                set_item[i] = set_word
            else:
                for char in word:
                    if not char.isalpha() and not char.isdigit():
                        set_word = word.replace(char, '')
                        set_item[i] = set_word
        docset.append(set_item)
        
    
            
    return(doclist, docset)

def search_doc(inpt, docset):
    '''
    Parameters
    ----------
    inpt : string
        key word or words to search for in docset.
    docset : list of sets 
        each set is a set of each document.

    Returns
    -------
    document numbers.

    '''
    docnums = []
    for i in range(len(docset)):
        uinpt = inpt.split() #to cover if there are multiple words searched
        if len(uinpt) == 1 and uinpt[0] in docset[i]: #if only one word
            docnums.append(str(i))
        elif len(uinpt) > 1: #if multiple words
            counter = 0
            for j in range(len(uinpt)): 
                if uinpt[j] in docset[i]:
                    counter += 1
            if counter == len(uinpt): #to check if ALL words inputted are in doc
                docnums.append(str(i))
    if len(docnums) == 1 and docnums[0] == '0':
        return('No relevant documents found')
    if len(docnums) > 0:
        num_return = '' #print format
        for i, num in enumerate(docnums): 
            if i == len(docnums) - 1:
                num_return += f'{num}'
            else:
                num_return += f'Documents: {num}, '
        return(num_return)

    else:
        return('No relevant documents found')

def read_doc(num, doclist):
    '''
    Parameters
    ----------
    num : integer
        document # that user wants to view.
    doclist : list of lists
        each list is a document.

    Returns
    -------
    Document in string format.

    '''
    index = int(num)
    outdoc = ''
    if index <= len(doclist) and index > 0:
        outlist = doclist[index]
        for word in outlist:
            outdoc = outdoc + word + ' '
        return outdoc
    else:
        return('Document number inputted is out of range')



def main():
    doc = open_file()
    listedfile = list_file(doc)
    x = True
    while x == True:
        openline = input('What would you like to do? \n1) Search for documents \n2) Read document \n3) Quit program\n>')
        if openline == '1':
            searchinp = (input('Enter search word(s): ')).lower()
            print(search_doc(searchinp, listedfile[1]))
        elif openline == '2':
            searchinp = input('Enter document number: ')
            print(read_doc(searchinp, listedfile[0]))
        elif openline == '3':
            x = False
        else: 
            print('Error in input. Try again')
    doc.close()
    
    
    
if __name__ == "__main__":
    main()














