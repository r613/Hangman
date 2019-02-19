def Game_on(words,letters,chances): #one round, in game
    text = "  "
    
    for word in words:
        final_w = " "
        
        for letter in word:
            final_l = "_"
            for l in letters:
                if letter == l:
                    final_l = letter
                else:
                    pass
            final_w += final_l
        text +=  final_w
        text += " "
    return text
def check(text):
    for l in text:
        
        if l == "_":
            return True
        else:
            pass
    return False