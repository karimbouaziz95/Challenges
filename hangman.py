import random
import time
import re

def start_game():
    global words_to_geuss
    global word
    global allowed_mistakes
    global sequence
    global guessed_letters
    global misses
    
    words_to_geuss = ["BreakingBad", "Elektrotechnik", "Batterie", "SelfDefence", "Nauka", "Software", "Coding", "Automation", "Systems", "LosPollosHermanos"]
    word = random.choice(words_to_geuss)
    allowed_mistakes = 6
    sequence = "_" * len(word)
    guessed_letters = []
    misses = []
    
    print("Alright here we go!")
    print("Your word is:" + sequence)
    
    hang_man()
    
def play_again():
    again = input("Do you want to play again? ['y', 'n', 'Y', 'N']")
    if again not in ["y", "n"]:
        print("please enter a correct input")
        play_again()
    else:
        if again == "y":
            print("get ready for the next battle !!!")
            start_game()
        else:
            print("Thank you bye bye!")
    
    
def hang_man():
    global words_to_geuss
    global word
    global allowed_mistakes
    global sequence
    global guessed_letters
    global misses
    
    
    while "_" in sequence and allowed_mistakes > 0:
        interm = ""
        guessed = input("Please enter a valid character: ")
        positions = [m.start() for m in re.finditer(guessed.lower(), word.lower())]
        if bool(positions):
            if guessed in guessed_letters:
                print("You already got this one -_-")
                continue
                
            print("Correct Guess!")
            guessed_letters.append(guessed)
            for i in range(len(word)):
                if i in positions:
                    interm += word[i]
                else:
                    interm += sequence[i]
                    
            sequence = interm
            
            print("The word is now: " + sequence)
        else:
            if guessed in misses:
                print("This is a mistake remember?")
                print("You still have " + str(allowed_mistakes) + " tries")
                
                continue
                
            allowed_mistakes = allowed_mistakes - 1
            misses.append(guessed)
            print("Wrong guess! you still have " + str(allowed_mistakes) + " tries")
            print("The word is still: " + sequence)
            
    if allowed_mistakes == 0:
        print("Sorry you lost the game! man is dead!")
        print("The answer is: " + word)
    else:
        print("Congrats you won! the man survived")
        print("The winner word is: " + sequence)
        
    play_again()
        
    
            
start_game()

    
    