'''
DOCSTRING
Adventure Game
Author: Joshua Williams
Version: 2.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
'''

#this will be the class that stores the player info
class Player:
    # constructor
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.health = 100
        self.has_map = False
        self.has_lantern = False

# ----- welcomes the player,

def welcome_player():
    # Welcome message and introduction
    print("Welcome to the Adventure Game!")  
    print('Your journey begins here... ')

        # Ask for the player's name
    name = input("What is your name, adventurer? ")
    player = Player(name)

    # Use an f-string to display the same message in a more readable way
    print(f'Welcome, {player.name}! Your journey begins now.')

    return player

#-----

def describe_area():
    # Describe the starting area
    print( """
    You find yourself in a dark forest
    The sound of rustling leaves fills the air
    A faint path lies ahead, leading deeper into the
    unknown... """)

# ----- 

def add_to_inventory(self, item):
    player.inventory.append(item)
    print(f"You picked up a {item}!")

# ----- allows welcome_player func to run

player = welcome_player()

# ----- describes area

describe_area()

# ----- option number 1

def explore_dark_woods(player):
    print(f'{player.name}, you step into the dark woods...')
    # if no lantern
    if 'lantern' not in player.inventory:
        add_to_inventory(player, 'lantern')
        print(f'\'lantern\' has been added to your inventory!')
    else:
        print(f'You have already found the lantern in the dark woods!')

# ----- option number 2

def explore_mountain_pass(player):
    print(f'you make your way towards the mountain pass, feeling the cold wind against your face.')
    # if no map
    if 'map' not in player.inventory:
      add_to_inventory(player, 'map')
      print(f'\'map\' has been added to your inventory')
      player.has_map = True
    else:
        print(f'You already have the map!')

# ----- option number 3

def explore_cave(player):
    print(f'{player.name}, you bravely enter the dark cave, your senses sharpen in the quiet darkness')
    if player.has_lantern == True:
        print(f'You find some fantastical treasure hidden in the darkness')
        add_to_inventory(player, 'treasure')
    else:
        print(f'It is too dark for you to see without a lantern')
        print(f'You banged your knee while stumbling through the cave')
        player.health -= 10

# ----- option number 4

def explore_hidden_valley(player):
    if player.has_map == True:
        print(f'You come across a fantastic valley seemingly hidden by time itself')
        print(f'as you travel this valley you come across some rare herbs')
        add_to_inventory(player, 'rare herbs')
    else:
        print(f'You look for the hidden valley, but seem to just be walking in circles')
        print(f'you got attacked by a squirrel while looking for the valley')
        player.health -= 10

# ----- option number 5

def stay_still(player):
    print(f'you stand there {player.name}, unsure of your next move')
    print(f'You got bit by a mosquito')
    player.health -= 10

while True:
    print('\nYou see some paths ahead:')
    print('\t1. Take the left path into the dark woods.')
    print('\t2. Take the right path toward the mountain pass.')
    print('\t3. Explore a nearby cave')
    print('\t4. Explore the Hidden Valley')
    print('\t5. Do nothing')
    print('\tType \'i\' to view your inventory.')

    decision = input("What will you do (1,2,3, 4, 5, or i): ").lower()

    # ---

    if decision == 'i':
        print("Inventory", player.inventory)
        continue

    # ---

    if decision == '1':
        explore_dark_woods(player)
        player.has_lantern = True

    # ---

    elif decision == '2':
        explore_mountain_pass(player)
        player.has_map = True

    # ---
      
    elif decision == '3':
        explore_cave(player)

    # ---

    elif decision == '4':
        explore_hidden_valley(player)

    # ---

    elif decision == '5':
        stay_still(player)

    # ---

    else: 
        print("Invalid choice. Please choose "
              "1, 2, or 3.")
    
    # ---
    
    # Ask if they want to continue
    play_again = input("Do you want to continue "
                       "exploring? (yes or no): ").lower()
    if play_again != "yes":
        print(f"Thanks for playing, {player.name} "
              "See you next time.")
        break # Exit the loop and end the game












# TODO: Add a health attribute to the Player class (start at 100)
# TODO: Create a function stay_still(player)
#       - Subtract 10 health when the player stays still
# TODO: Modify explore_cave(player)
#       - If player does not have lantern, subtract 10 health
# TODO: Modify explore_hidden_valley(player)
#       - If player does not have map, subtract 10 health
# TODO: Create a function check_win(player)
#       - If "treasure" and "rare herbs" are both in inventory, print win message and exit
# TODO: Create a function check_lose(player)
#       - If health is 0 or lower, print lose message and exit
# TODO: Show the player's current health after every action
# TODO: Continue using good Git habits: save, commit, push!
# TODO: Final commit message example: "COMPLETE Final Adventure Game"