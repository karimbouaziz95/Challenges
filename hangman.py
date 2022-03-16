import random
import time

def start_game():
    global words_to_geuss
    global word
    global allowed_mistakes
    global sequence
    
    words_to_geuss = ["BreakingBad", "Elektrotechnik", "Batterie", "SelfDefence", "Nauka", "Software", "Coding", "Automation", "Systems", "LosPollosHermanos"]
    word = random.choice(words_to_geuss)
    allowed_mistakes = 6
    sequence = "_" * len(word)
    
    
def hang_man():
    global words_to_geuss
    global word
    global allowed_mistakes
    global sequence
    
    while "_" in sequence and allowed_mistakes > 0:
        guessed = input("Please enter a valid character: ")
        if guessed.lower() in word.lower():
            pass
    
    