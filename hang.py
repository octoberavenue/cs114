#This is a code for a standard game of Hangman.
import random

def main():
    start = ['Welcome to Hangman! A word will be chosen at random and','you must try to guess the word correctly letter by letter','before you run out of attempts. Good luck!']
    print ("Are you ready to play judge jury and executioner?")
    print ("(1)Yes, death is inevitable.\n(2)No, I dont want to be responsible for anothers life!")
    user_choice_1 = raw_input("-->")

    if user_choice_1 == '1':
        print("Preparing the noose, knots are tight, getting tighter, now preparing murderers, finding one at random, fantastic say hello to",
    random.murderer(murderers))
        ().HANGMAN
    elif user_choice_1 == '2':
        print ("I'll be seeing you again real soon...")
        exit()
    else:
        print ("Speak up! did you say Yes? Please tell me you said yes, we can't just hang people with your input.")
        ().main
    for line in start:
        print(line, sep='\n')
        
    play_again = True

    while play_again:

        words = ["money", "cyborg", "singing", "toilet", "funny", "music", "rocket", "computer", "biology", "ninjas", "turtle", "kitten,"]
        chosen_word = random.choice(words).lower()
        murderers = ["George the red", "Mike the biter", "Steve the scratcher", "Mary the strangler", "Susan the widowmaker", "Stacy the stabber"]
        chosen_murderer = random.murderer(murderers)
        player_guess = None
        guess_letters = []
        for letter in chosen_word:
            word_guessed.append("-")
        joined_word = None

        HANGMAN = (
"""
-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  -|-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-|-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-|-\
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-|-\
|   |
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-|-\
|   |
|   |
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|   |
|   |
|  |
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|   |
|   |
|  |
|  |
|
--------
""",
"""
-----
|   |
|   0
| /-|-\
|   |
|   |
|  | |
|  |
|
--------
""",
"""
-----
|   |
|   0
| /-|-\
|   |
|   |
|  | |
|  | |
|
--------
""")

    print(HANGMAN[0])
    attempts = len(HANGMAN) - 1

    while (attempts != 0 and "-" in word_guessed):
        print(("\nYOu have {} attempts remaining").format(attempts))
        joined_word = "".join(word_guessed)
        print(joined_word)

        try:
            player_guess = str(input("\nPlease select a letter between A-Z" + "\n> ")).lower()
        except:
            print("That is not a valid input. Please try again.")
            continue
        else:
            if not player_guess.isalpha():
                print("That is not a letter. Please try again.")
                continue
            elif len(player_guess) > 1:
                print("That is more than one letter. Please try again")
            elif player_guess in guess_letters:
                print("You have already guess that letter. Please try again.")
                continue
            else:
                pass
        guessed_letters.append(player_guess)

        for letter in range(len(chosen_word)):
            if player_guess == chosen_word[letter]:
                word_guess[letter] = player_guess

        if player_guess not in chosen_word:
            attempts -= 1
            print(HANGMAN[(len(HANGMAN) - 1) - attempts])

        if "-" not in word_guess:
            print(("\nCongratulations! {} was the word").format(chosen_word))
        else:
            print(("\nUnlucky! The word was {}.").format(chosen_word))

        print("\nWould you like to play again?")

        response = input("> ").lower()
        if response not in ("yes", "y"):
            play_again = False
if __name__ == "__start__":
    start()
