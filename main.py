#Starting the program 13/2/19 4:30 (GMT) or 5:30

## this is halarious! no one will ever be reading this!!!

"""
from chaimson import dictionary 
from chaimson import generate_word
def menu():
    game_on = True 
    words = generate()
    while game_on:
        
        around(words,letters)
"""
def menu():
        game_on = True
        words = "Ruby Awesome!"
        n_rounds = 0
        attempts_left = 6
        letters = []

        while game_on:
                n_rounds += 1
                letter = around(words,letters)
                letters.append(letter)
                result()

def around(words,letters): #this function starts one round 

def result(): #this function prints the result of the past round 
