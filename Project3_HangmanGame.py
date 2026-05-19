# Hangman Game in Python......................
import random  #This module is used to pick a random word from the list.
import hangman_stages  #This is your custom Python file (e.g., hangman_stages.py) that contains ASCII art drawings of the Hangman stages
import word_file

#word_list=['apple','beautiful','potato','python','developer','programming','hangman']
#chosen_word=random.choice(word_list) #Randomly selects one word from the list to be the chosen_word.

chosen_word=random.choice(word_file.words)
lives=6   # have 6 chances (or "lives") to guess the word correctly before the game ends.
print(chosen_word)

#Initializes a list called display filled with underscores (_), one for each letter in the chosen word.
# If the word is "apple", display becomes ['_', '_', '_', '_', '_'].
display=[]
for i in range(len(chosen_word)):
    display += '_'
print(display)

game_over=False  #A flag to track whether the game has ended. It will change to True when the player wins or loses.

#Main game loop  --> Keeps running the game until game_over becomes True
while not game_over:
    guessed_letter=input("Guess a letter:").lower()   #for lower letter .low() function (so 'A' and 'a' are treated the same).
    #If the guessed letter matches the letter at that position, it updates the corresponding _ in display.
   
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter
    print(display)  #show current progress

    #If the guessed letter isn't in the word, subtract 1 life.
    if guessed_letter not in chosen_word:
        lives -= 1
        if lives == 0:     #If lives reaches 0, set game_over = True and print "You lose!"
            game_over = True
            print("You lose!")

    if '_' not in display:  #If there are no more _ in the display, it means the user has guessed the full word → game won.
        game_over=True
        print('You win..')
    
    #Based on the number of lives left, prints the corresponding Hangman stage drawing (from hangman_stages.stages list).
    print(hangman_stages.stages[lives])