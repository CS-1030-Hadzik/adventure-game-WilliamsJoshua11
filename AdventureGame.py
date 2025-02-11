'''
This is a Doc String
Adventure Game
Author: Joshua Williams
Version: 1.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
'''


# Welcome Message and Introduction
print('Welcome to the Adventure Game')
print('Your journey begins here...')

# Ask for Player's name
player_name = input('What is your name, adventurer? ')

#Concatenate strings to create a personalized message (3 strings concatenated)
# print('Welcome,' + player_name, + '! Your journey begins now.')

# Using f-strings allow for more readability
print(f'Welcome, {player_name}! Your journey begins now')

# Description of starting area
starting_area = """You find yourself in a dark forest.
The sound of rustling leaves fills the air.
A faint path lies ahead, leading deeper into the unknown...
"""
print(starting_area)

#start game loop
while True:
    print('\nYou see two paths ahead')
    print('\t1. Take the path into the dark woods')
    print('\t2. Take the right path toward the mountain pass')
    print('\t3. Stay where you are')
    decision = input('What will you do? (1,2,3): ')

    if decision == '1':
        print(f'{player_name}, you step into the dark woods. ' 
          'The trees whisper as you walk deeper.')
    elif decision == '2':
        print(f'{player_name}, you make your way '
          'toward the mountain pass, feeling '
          'cold wind against your face')
    elif decision == '3':
        print(f'You stay still, listening to the'
          'sounds of the forest')
    else:
        print('that option does not work adventurer, please choose'
          '1, 2, or 3. ')

    # ask if player wishes to continue
    playAgain = input('Do you wish to continue exploring?'
      '(yes or no): ')
    if playAgain != 'yes':
        print(f'Thank you for playing, {player_name} '
          'See you next time.')
        break
