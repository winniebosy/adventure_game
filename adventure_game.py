#animals to use in my game
#sangoma-house
#popo bawa -house
# Jengu-cave
#Groostlang



#project file modules
import time
import random

#print pause
def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)

#introductory message
def intro_message(items, options):
    def intro_message():
        print_pause("You find yourself standing in an open savannah "
                    "filled with long grass and scattered trees.")
        print_pause(f"Rumor has it that an evil {options} "
                 "is around here and has been terrifying "
                 "the nearby village")
        print_pause("In front of you is a Manyatta aka a house")
        print_pause("To your right is a dark cave")
        print_pause("In your had you hold your trusty "
                "(but not effective) dagger \n")


    



def play_game():
#empty list
    items = []
#random animal options
    options = random.choice(["Sangoma", "Popo bawa", "Jengu", "Grootslang"])
    intro_message()



play_game()
