# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 22:34:35 2020

@author: bijuangalees
"""


from PIL import Image
end=100

def show_board():
    img=Image.open('snakeladder.jpg')
    img.show()
def check_ladder(points):
    if points==8:
        print('Ladder')
        return 26
    elif points==21:
        print('Ladder')
        return 82
    elif points==43:
        print('Ladder')
        return 77
    elif points==50:
        print('Ladder')
        return 91
    elif points==54:
        print('Ladder')
        return 82
    elif points==62:
        print('Ladder')
        return 96
    elif points==66:
        print('Ladder')
        return 87
    elif points==80:
        print('Ladder')
        return 100
    else:
        return points
def check_snake():
       if points==8:
        print('Ladder')
        return 26
    elif points==21:
        print('Ladder')
        return 82
    elif points==43:
        print('Ladder')
        return 77
    elif points==50:
        print('Ladder')
        return 91
    elif points==54:
        print('Ladder')
        return 82
    elif points==62:
        print('Ladder')
        return 96
    elif points==66:
        print('Ladder')
        return 87
    elif points==80:
        print('Ladder')
        return 100
    else:
        return points
    
def reached_end(points):
    if points==end:
        return true
    else:
        return false
    
    
    
def play(): 
    p1_name=raw_input("Player 1,Please enter your name:")
    p2_name=raw_input("Player 2,Please enter your name:")
    #intial points of player 1
    pp1=0
    #intial points of player 2
    pp2=0
    
    turn=0
    
    while(1):
        if turn%2==0:
            #player 1 turn
            print(p1_name,'your turn')
            #ask player's choice to continue
            c=input('Press 1 to continue, 0 to quit')
            if c==0:
                print(p1_name,'scored',pp1)
                print(p2_name,'scored ',pp2)
                print('Quitting the game, Thanks for playing')
                break
            #geneate a random number from 1,2,3,4,5,6
            dice=random.randint(1,6)
            print('Dice showed:'dice)
            #add points
            pp1=pp1+dice
            
            pp1=check_ladder(pp1)
            
            pp1=Check_snake(pp1)
            #check if player goes beyond the board
            if pp1>end:
                pp1=end
            print(p1_name,'You score:',pp1)
            
            if reached_end(pp1):
                print(p1_name,'won')
                break
            else:
                #player 2 turn
                print(p2_name,'your turn')
                #ask player's choice to continue
            c=input('Press 1 to continue, 0 to quit')
            if c==0:
                print(p1_name,'scored',pp1)
                print(p2_name,'scored ',pp2)
                print('Quitting the game, Thanks for playing')
                break
            #geneate a random number from 1,2,3,4,5,6
            dice=random.randint(1,6)
            print('Dice showed:'dice)
            #add points
            pp2=pp2+dice
            pp2=check_ladder(pp2)
            pp2=Check_snake(pp2)
            #check if player goes beyond the board
            if pp2>end:
                pp1=end
            print(p2_name,'You score:',pp2)
            
            if reached_end(pp2):
                print(p2_name,'won')
                break
            turn=turn+1
show_board()
play()
            
    
    
show_board()   


    