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
    
#valid input
def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lowercase()#getting user input and is case insensitive
        #getting and assessing user response
        if option1 in response:
            break
        elif option2 in response:
             break       
    return response
    
       
#print introductory message before game starts
def intro_message():
    print_pause("You find yourself standing in an open savannah "
                "filled with long grass and scattered trees.")
    print_pause("Rumor has it that an evil Sangoma "
                 "is around here and has been terrifying "
                 "the nearby village")
    print_pause("In front of you is a Manyatta aka a house")
    print_pause("To your right is a dark cave")
    print_pause("In your had you hold your trusty "
                "(but not effective) dagger \n")
    
#giving player a choice

def player_selection():
    print_pause("Enter 1 to knock on the door of the Manyatta")
    print_pause("Enter 2 to peer into the cave")
    print_pause("What would you like to do?")
    response = valid_input("(Please enter 1 or 2).\n ", 
                           "1" , "2")
    if "1" in response:
        #call manyatta-house function
        print_pause("Heyyy! manyatta \n")
        manyatta_house()
        #call cave function
    elif "2" in response:
         print_pause("Heyyy! house")


#events that happen when the player fights
def fight():
    print_pause("You do your best...")
    print_pause("but your dagger is "
                " not match for the Sangoma")
    print_pause("Ooops! you have been defeated! \n")
    response = valid_input("Would you like to play again?  "
                           "YES or NO \n", "yes", "no")
    if "yes" in response:
        print_pause("Excellent! Restarting the game...")
        intro_message()
    else:
        print_pause("Thank you for playing! Kwaheri!")
        exit()
        
  


#events that happens to the player goes in the cave
#def cave():
    
    
#events that happen when the player runs back to the field
#def field():

#events that happen to the player in the house.

def manyatta_house(): 
#introductory message
    print_pause("You approach the door "
                "of the house")
    print_pause("You are about to knock "
                "when the door opens "
                "and out steps a scary Sangoma ")
    print_pause("Eeep! This is the Sangoma's house ")
    print_pause("The Sangoma attacks you!")
    print_pause("You feel a bit "
                "under-prepared for this, "
                "what with only having a tiny dagger ")
    print_pause("Would you like to "
                "(1) FIGHT or (2) RUN AWAY? ")
    response = valid_input("Please key in an option: \n ", "1", "2")
    
    if "1" in response:
        print_pause("wow!")
        fight()
    elif "2" in response:
        print_pause("pole ndungu")
        exit()
        
    
    

    
        
        

    
         

    
    
    
    
    
intro_message()
player_selection()
manyatta_house()
