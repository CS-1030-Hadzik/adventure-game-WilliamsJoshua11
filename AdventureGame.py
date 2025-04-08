'''
This is a Doc String
Adventure Game
Author: Joshua Williams
Version: 1.2
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
    print(f'welcome {name}, your journey begins now...')
    player = Player(name)
    return player

# ----- describe starting area

def describe_area():
    print( """
    You find yourself in a dark forest
    The sound of rustling leaves fills the air
    A faint path lies ahead, leading deeper into the
    unknown... """)

# ----- add to inventory

def add_to_inventory(self, item):
    player.inventory.append(item)
    print(f'You picked up a {item}!')

# ----- runs welcome_player and describe area

player = welcome_player()
describe_area()

#start game loop
while True:
    print('\nYou see multiple paths ahead')
    print('\t1. Take the path into the dark woods')
    print('\t2. Take the right path toward the mountain pass')
    print('\t3. Explore a nearby cave')
    print('\t4. Explore the Hidden Valley')
    print('\t5. Stay where you are')
    print('\tType \'i\' to view your inventory.')

    decision = input('What will you do? (1,2,3,4,5,i): ')
    print('')

    if decision == 'i':
        print("Inventory", player.inventory)
        continue

    elif decision == '1':
        print(f'{player.name}, you step into the dark woods. ' 
          'The trees whisper as you walk deeper.')
        add_to_inventory(player, 'lamp')
        player.has_lantern = True
    
    elif decision == '2':
        print(f'{player.name}, you make your way '
          'toward the mountain pass, feeling '
          'cold wind against your face')
        add_to_inventory(player, 'map')
        player.has_map = True
    
    elif decision == '3':
        print(f'{player.name}, you bravely enter the dark cave, your senses sharpen in the quiet darkness')
        if player.has_lantern == True:
            print(f'You find some fantastical treasure hidden in the darkness')
            add_to_inventory(player, 'treasure')
        else:
            print(f'It is too dark for you to see without a lantern')

    elif decision == '4':
        if player.has_map == True:
            print(f'You come across a fantastic valley seemingly hidden by time itself')
            print(f'as you travel this valley you come across some rare herbs')
            add_to_inventory(player, 'rare herbs')
        else:
            print(f'You look for the hidden valley, but seem to just be walking in circles')
    elif decision == '5':
        print(f'You stay still, listening to the'
          'sounds of the forest')
        
    else:
        print('that option does not work adventurer, please choose'
          '1, 2, 3, 4, 5, or \'i\' ')

    # ask if player wishes to continue
    playAgain = input('Do you wish to continue exploring?'
      '(yes or no): ')
    if playAgain != 'yes':
        print(f'Thank you for playing, {player.name} '
          'See you next time.')
        break



# TODO: After picking up new items, confirm to the player they got it
# TODO: Save your changes (Ctrl+S or Command+S)
# TODO: Commit with a message like:
#       REF unlock new areas based on inventory items
# TODO: Push your commits to GitHub