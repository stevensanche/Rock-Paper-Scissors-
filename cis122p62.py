'''
CIS 122 Spring 2022 Project 6-2
Author: Steven Sanchez Jimenez
Credit: CIS 122 Resources, Office Hours
Description: Rock Paper Scissors
'''
import random

def rps():
    '''
    >>> rps()
    Side 1 is r and Side 2 is s.
    The winner is Side 1!
    >>> rps()
    Side 1 is s and Side 2 is s.
    tie ... playing again
    Side 1 is p and Side 2 is s.
    The winner is Side 2!
    '''
    while True:
        side_1 = random.choice('rps')
        side_2 = random.choice('rps')
        print('side 1 is', side_1 , 'and side 2 is', side_2)

        
        if side_1 == 'r' and side_2 == 'p':
            print ('The winner is Side 2')
            break
    
        if side_1=='r' and side_2=='s':
            print ('The winner is Side 1')
            break
    
        if side_1=='p' and side_2=='s':
            print ('The winner is Side 2')
            break
    
        if side_1=='p' and side_2=='r':
            print ('The winner is Side 1')
            break
    
        if side_1=='s' and side_2=='r':
            print ('The winner is Side 2')
            break
    
        if side_1=='r' and side_2=='p':
            print ('The winner is Side 2')
            break
    
        if side_1 =='r' and side_2 =='r':
            print('tie ... playing again')
            continue
    
        if side_1 =='p' and side_2 =='p':
            print('tie ... playing again')
            continue
    
        if side_1 =='s' and side_2 =='s':
            print('tie ... playing again')
            continue

rps()



    
