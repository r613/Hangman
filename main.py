#v1.1
import random 
from create import create
from create import creator
from stf import exists
from stf import Game_on
from stf import check

word = "Stuff"

def get_l(letters):
        letter = raw_input("Guess one letter: ")
        if len(letter) !=1:
                print "One letter only!"
                return get_l(letters)
        for l in letters:
                if l == letter:
                        print "Your already entered that letter, try again! "
                        return get_l(letters)
                else:
                        pass
        return letter

def Menu(list):
        #text = create()
        text = creator(list[random.randint(0, len(list) -1 ) ])
        letters = " "
        tries = 0

        gaming = True 
        while gaming:
                print "\n\n\n"
                #print the words/empty spaces
                print Game_on(text,letters,tries)
                #number of tries +1
                
                print "Tries: " + str(tries)
                letter = get_l(letters)
                        
                letters += letter
                #print number of tries
                

                
                # If user ran out of tries, game ends
                
                #if text is full, game ends
                gaming = check(Game_on(text,letters,tries)) #check(...) returns False if the text is found
                if exists(text,letters,letter)==False:
                        tries += 1
                else:
                        pass

                if tries > 15:
                        print "you ran out of tries"
                        gaming = False 
        print Game_on(text,letters,tries)
        print "All done. "
        #print check(Game_on(text,letters,tries))

list = ["ruby is a freaking boss","ruby is awesome","ruby is great","this code was made by a genius"]     
    
Menu(list)