'''
    Number Guessing Game
-------------------------------------------------------------
'''


import random


def guess_game():
    number_of_tries = 0
    
    number = random.randint(1,100)
    
    print("Hello Welcome to the game !")
    player_name = input("What is your name :")

    wanna_play = input(f'So, {player_name} you still wanna play ? (yes or no)')

    if wanna_play.lower == 'no':
        print("o malk msd3 lina krna la mabarich tl3b ")
        exit()

    while wanna_play.lower() == 'yes':
        guess = int(input('Pick a number between 1 and 100: '))
        if guess < 1 or guess > 100:
            print('Please guess a number within the given range')
        
            if guess == number:
                print(f"Lessgooo you found it ! It took you {number_of_tries} try.")

            wanna_play = input('Would you like to play again? (Enter Yes/No): ')


            if wanna_play.lower == 'no':
                print("ylh sf ghyriha")

            else :
                number_of_tries = 0
                number = random.randint(1, 100)
                continue
        else:
            if guess > number:
                print('It\'s lower')
            else :
                print('It\'s higher')
    
    print("That is not a valid value try again")


guess_game()