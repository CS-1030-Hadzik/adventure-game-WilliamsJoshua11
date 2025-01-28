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
print("Welcome to the Adventure Game")
print("Your journey begins here...")

# Ask for Player's name
player_name = input("What is your name, adventurer? ")

#Concatenate strings to create a personalized message (3 strings concatenated)
print("Welcome, " + player_name + "! Your journey begins now.")

# Using f-strings allow for more readability
print(f'Welcome, {player_name}! Your journey begins now')

# Description of starting area
starting_area = """You find yourself in a dark forest.
The sound of rustling leaves fills the air.
A faint path lies ahead, leading deeper into the unknown...
"""
print(starting_area)

# Ask the player for their first decision
decision = input("Do you wish to take the path? (yes or no): ").lower()

# Respond based on the player's decision (change to f strings later)
if decision == "yes":
    print(f"Brave choice, {player_name}! You step onto the path and venture forward.")
elif decision == "no":
    print(player_name + ", you decide to wait. Perhaps courage will find you later.") # Concatenation example
else:
    print("Confused, you stand still, unsure of what to do.")