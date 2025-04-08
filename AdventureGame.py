'''
This is a Doc String
Adventure Game
Author: Joshua Williams
Version: 1.1
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
'''


# ----- Welcome Message and Introduction

class Player:
    # constructor
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.health = 100
        self.has_map = False
        self.has_lantern = False

# -----

def welcome_player():
    # Welcome message and introduction
    print('Welcome to the Adventure Game!')  
    print('Your journey begins here... ')

        # Ask for the player's name
    name = input('What is your name, adventurer? ')
    player = Player(name)

# -----

player_name = input('What is your name, adventurer? ')

# -----

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



# TODO: Define a function called welcome_player() that:
#       - Prints a welcome message
#       - Asks the user for their name using input()
#       - Welcomes the user using an f-string
#       - Returns the player's name

# TODO: Define a function called describe_area() that:
#       - Prints a multi-line string describing the starting location of the game

# TODO: Define a function called add_to_inventory(item) that:
#       - Takes an item (string) as a parameter
#       - Adds the item to the inventory list
#       - Prints a message saying the item was picked up

# TODO: Call welcome_player() and store the result in a variable called player_name

# TODO: Call describe_area() to print the scene before the game loop starts

# TODO: Inside the game loop:
#       - If the user types "i", print the contents of the inventory
#       - If the user chooses option 1, call add_to_inventory("lantern")
#       - If the user chooses option 2, call add_to_inventory("map")