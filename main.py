from create import create
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

def Menu():
        text = create()
        
        letters = " "
        tries = 0

        gaming = True 
        while gaming:
                print "\n\n\n"
                #print the words/empty spaces
                print Game_on(text,letters,tries)
                #number of tries +1
                tries += 1
                letters += get_l(letters)
                #print number of tries
                print "Tries: " + str(tries)
                # If user ran out of tries, game ends
                
                #if text is full, game ends
                gaming = check(Game_on(text,letters,tries)) #check(...) returns False if the text is found
                if tries > 15:
                        print "you ran out of tries"
                        gaming = False 
        print "All done, "
        print check(Game_on(text,letters,tries))


                
    
Menu()