#The game gives players a description of what's happening, and then asks them to make a choice.
#Something different happens depending on the choice the player made.
#The game also includes some random factors, so that it's a little different each time.
#The game has conditions for winning and losing.
#When the game is over, it asks if the player wants to play again.
#time module
import time

#random module
import random

#print pause
def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)
    
#print introductory message before game starts
def intro_message():
    print_pause("You find yourself standing in an open savannah "
                "filled with long grass and scattered trees.")
    print_pause("Rumor has it that an evil Sangoma,"
                 "is around here and has been terrifying "
                 "the nearby village")
    print_pause("In front of you is a Manyatta aka a house")
    print_pause("To your right is a dark cave")
    print_pause("In your had you hold your rusty "
                "(but not effective) dagger")
    
#giving player a choice
def player_selection():
    print_pause
    

intro_message()
items = []