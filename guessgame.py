#This is a guess the number game.
import random
secretNumber = random.randint(1, 30)
print('There exists a number of great significance between 1 and 30.')

#Asks the payer to guess 7 times.
for guessesTaken in range(1, 8):
    print('What is the number? Your attempts are few.')
    guess = int(input())

    if guess < secretNumber:
        print('You chose poorly try something larger')
    elif guess > secretNumber:
        print('You chose poorly try something smaller')
    else:
        break   #This condition is the correct answer.

if guess == secretNumber:
    print('You chose wisely it only took you ' + str(guessesTaken) + 'attempts.')
else:
    print(' You have failed and now you must die. By the way the number was ' + str(secretNumber))
