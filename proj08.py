#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 12:31:06 2020

@authoimport cards
"""

    ###########################################################
    #  proj08.py Free Cell Solitaire
    #
    #  Algorithm
    #   display rules and help
    #   display tableau, cells, foundation
    #    loop while x == True
    #       prompt for a move
    #       if move valid:
    #           call function for move
    #       if invalid, display error nessage
    #       refresh board every time a move is made
    #    if foundation is full or if q:
    #       display closing message
    ###########################################################


def setup():
    """
    paramaters: None (deck can be created within this function)
    returns:
    - a foundation (list of 4 empty lists)
    - cell (list of 4 empty lists)
    - a tableau (a list of 8 lists, the dealt cards)
    """
    foundation = [[], [], [], []] 
    cell = [[], [], [], []]
    tableau = [[], [], [], [], [], [], [], []]
    my_deck = cards.Deck()
    my_deck.shuffle()         
    for i in range(52): #all cards in deck
        for j in range(8): #all elements in tableau list
            tableau[j].append(my_deck.deal())
            if None in tableau[j]:
                tableau[j].pop()
    return foundation,tableau,cell
    


def move_to_foundation(tableau,foundation,t_col,f_col): #
    '''
    parameters: a tableau, a foundation, column of tableau, column of foundation
    returns: Boolean (True if the move is valid, False otherwise)
    moves a card at the end of a column of tableau to a column of foundation
    This function can also be used to move a card from cell to foundation
    '''
    tabcard = tableau[t_col][-1]
    foundcard = None
    if len(foundation[f_col]) > 0: #if foundation not empty, establish foundation card
        foundcard = foundation[f_col][-1]
    redcards = [1,4]
    blackcards = [2,3]
    if len(foundation[f_col]) == 0 and tabcard.rank() == 1: #if empty foundation & if ace
        foundation[f_col].append(tableau[t_col].pop())
        return True
    elif (tabcard.suit() in redcards and foundcard.suit() in blackcards) or \
        (tabcard.suit() in blackcards and foundcard.suit() in redcards): #matching up opposite suites
        if foundcard.rank() == tabcard.rank() - 1:
            foundation[f_col].append(tableau[t_col].pop())
            return True
        else:
            return False
    else:
        return False
    

def move_to_cell(tableau,cell,t_col,c_col):
    '''
    parameters: a tableau, a cell, column of tableau, column of cell
    returns: Boolean (True if the move is valid, False otherwise)
    moves a card at the end of a column of tableau to a cell
    '''
    cellcard = cell[c_col]
    if len(cellcard) == 0:
        cellcard.append(tableau[t_col].pop())
        return True
    

def move_to_tableau(tableau,cell,t_col,c_col):
    '''
    parameters: a tableau, a cell, column of tableau, a cell
    returns: Boolean (True if the move is valid, False otherwise)
    moves a card in the cell to a column of tableau
    remember to check validity of move
    '''
    tabcard = tableau[t_col][-1]
    redcards = [1,4] 
    blackcards = [2,3]
    cellcard = cell[c_col][0]

    if len(tableau[t_col]) == 0: #if empty tableau column
        tableau[t_col].append(cell[c_col].pop())
        return True
    elif (tabcard.suit() in redcards and cellcard.suit() in blackcards) or \
        (tabcard.suit() in blackcards and cellcard.suit() in redcards): #matching up opposite suites
        if cellcard.rank() == tabcard.rank() - 1:
            tableau[t_col].append(cell[c_col].pop())
            return True
        else:
            return False
    else:
        return False
        

def is_winner(foundation):
    '''
    parameters: a foundation
    return: Boolean
    '''
    for i in range(4):
        if len(foundation[i]) == 13: #if all elements in foundation list are full
            return 1


def move_in_tableau(tableau,t_col_source,t_col_dest):
    '''
    parameters: a tableau, the source tableau column and the destination tableau column
    returns: Boolean
    move card from one tableau column to another
    remember to check validity of move
    '''
    dest = tableau[t_col_dest][-1]
    source = tableau[t_col_source][-1]
    redcards = [1,4]
    blackcards = [2,3]
    if len(tableau[t_col_dest]) == 0: #if empty tableau column
        tableau[t_col_dest].append(tableau[t_col_source].pop())
        return True
    elif (dest.suit() in redcards and source.suit() in blackcards) or \
        (dest.suit() in blackcards and source.suit() in redcards): #matching up opposite suites
        if source.rank() == dest.rank() - 1:
            tableau[t_col_dest].append(tableau[t_col_source].pop())
            return True
        else:
            return False
    else:
        return False
            

def print_game(foundation, tableau,cell):
    """
    parameters: a tableau, a foundation and a cell
    returns: Nothing
    prints the game, i.e, print all the info user can see.
    Includes:
        a) print tableau  
        b) print foundation ( can print the top card only)
        c) print cells

    """
    print()
    print("                 Cells:                              Foundation:")
    # print cell and foundation labels in one line
    for i in range(4):
        print('{:8d}'.format(i+1), end = '')
    print('    ', end = '')
    for i in range(4):
        print('{:8d}'.format(i+1), end = '')
    print()  # carriage return at the end of the line

    # print cell and foundation cards in one line; foundation is only top card
    for c in cell:
        # print if there is a card there; if not, exception prints spaces.
        try:
            print('{:>8s}'.format(str(c[0])), end = '')
        except IndexError:
            print('{:8s}'.format(''), end = '')
            
    print('    ', end = '')
    for stack in foundation:
        # print if there is a card there; if not, exception prints spaces.
        try:
            print('{:>8s}'.format(str(stack[-1])), end = '')
        except IndexError:
            print('{:8s}'.format(''), end = '')

    print()  # carriage return at the end of the line
    print('----------')

    print("Tableau")
    for i in range(len(tableau)):  # print tableau headers
        print('{:8d}'.format(i + 1), end = '')
    print()  # carriage return at the end of the line
    print()
    
    # Find the length of the longest stack
    max_length = max([len(stack) for stack in tableau])

    # print tableau stacks row by row
    for i in range(max_length):  # for each row
        print(' '*7, end = '')  # indent each row
        for stack in tableau:
            # print if there is a card there; if not, exception prints spaces.
            try:
                print('{:8s}'.format(str(stack[i])), end = '')
            except IndexError:
                print('{:8s}'.format(''), end = '')
        print()  # carriage return at the end of the line
    print('----------')

def print_rules():
    '''
    parameters: none
    returns: nothing
    prints the rules
    '''
    print("Rules of FreeCell")

    print("Goal")
    print("\tMove all the cards to the Foundations")

    print("Foundation")
    print("\tBuilt up by rank and by suit from Ace to King")

    print("Tableau")
    print("\tBuilt down by rank and by alternating color")
    print("\tThe bottom card of any column may be moved")
    print("\tAn empty spot may be filled with any card ")

    print("Cell")
    print("\tCan only contain 1 card")
    print("\tThe card may be moved")

def show_help():
    '''
    parameters: none
    returns: nothing
    prints the supported commands
    '''
    print("Responses are: ")
    print("\t t2f #T #F - move from Tableau to Foundation")
    print("\t t2t #T1 #T2 - move card from one Tableau column to another")
    print("\t t2c #T #C - move from Tableau to Cell")
    print("\t c2t #C #T - move from Cell to Tableau")
    print("\t c2f #C #F - move from Cell to Foundation")
    print("\t 'h' for help")
    print("\t 'q' to quit")
    



def play():
    ''' 
    Main program. Does error checking on the user input. 
    '''
    print_rules()
    foundation, tableau, cell = setup() 
    x = True #loop
    show_help()
    while x == True:
        # Uncomment this next line. It is commented out because setup doesn't do anything so printing doesn't work.
        print_game(foundation, tableau, cell)
        response = input("Command (type 'h' for help): ")
        response = response.strip()
        response_list = response.split()
        if len(response_list) > 0:
            r = response_list[0]
            if r == 't2f':
                t_col = int(response_list[1]) - 1
                f_col = int(response_list[2]) - 1
                move_to_foundation(tableau, foundation, t_col, f_col) 
                
            elif r == 't2t':
                t_col_source = int(response_list[1]) - 1
                t_col_dest = int(response_list[2]) - 1
                move_in_tableau(tableau, t_col_source, t_col_dest)  
                
            elif r == 't2c':
                t_col = int(response_list[1]) - 1
                c_col = int(response_list[2]) - 1    
                move_to_cell(tableau, cell, t_col, c_col)
                   
            elif r == 'c2t':
                c_col = int(response_list[1]) - 1
                t_col = int(response_list[2]) - 1
                move_to_tableau(tableau,cell,t_col,c_col)
                
            elif r == 'c2f':
                c_col = int(response_list[1]) - 1
                f_col = int(response_list[2]) - 1
                move_to_foundation(cell,foundation,c_col,f_col)
                         
            elif r == 'q':
                print('game quit')
                x = False
            elif r == 'h':
                show_help()
            else:
                print('Unknown command:',r)
         
        else:
            print("Unknown Command:",response)
         
        if is_winner(foundation) == 1:
            print('You won!')
            x = False
            
    print('Thanks for playing')

if __name__ == '__main__':
    play()

        
    

