import random

def wordPicker():
    words = ["computer", "mouse", "keyboard", "CPU", "GPU", "monitor"]
    return random.choice(words)

stages = [
    """
       --------
       |      |
       |      
       |    
       |      
       |     
    """,
    """
       --------
       |      |
       |      O
       |    
       |      
       |     
    """,
    """
       --------
       |      |
       |      O
       |      |
       |      
       |     
    """,
    """
       --------
       |      |
       |      O
       |     /|
       |      
       |     
    """,
    """
       --------
       |      |
       |      O
       |     /|\\
       |      
       |     
    """,
    """
       --------
       |      |
       |      O
       |     /|\\
       |     / 
       |     
    """,
    """
       --------
       |      |
       |      O
       |     /|\\
       |     / \\
       |     
    """
]

theWord = list(wordPicker())
s = list('_' * len(theWord))

print("\n\nWelcome to Hangman Game by Mahmoud Hamad\n\n")
x = len(theWord)
print(f"The game idea is that there is a word with {x} letters, and you will have to guess it letter by letter.\n")
print("Note that the game is case-sensitive.\n")

counter = 7
pickedletters = ""

while True:
    while True:
        ch = input("Input your guess: ")
        
        if len(ch) == 1 and ch.isalpha() and ch not in pickedletters:
            pickedletters += ch
            break
        elif len(ch) != 1:
            print("You must input only one letter.\n")
        elif ch in pickedletters:
            print("You have already tried this letter.\n")
        else:
            print("You must input an alphabetical character.\n")
    
    ok = False
    for i in range(len(theWord)):
        if theWord[i] == ch:
            ok = True
            s[i] = ch

    if ok:
        ans = "".join(s)
        print(f"Good job! The letter {ch} is in the word.")
        print(f"Now the word will be: {ans}\n")
    else:
        counter -= 1
        print(f"Unfortunately, the letter {ch} is not in the word.")
        print(stages[6 - counter])
        print(f"You have {counter} guesses left.\n")

    if '_' not in s:
        print("Congrats, hero! You have guessed it!")
        break
    if counter == 0:
        print("Hard luck! You have no more guesses.")
        break
