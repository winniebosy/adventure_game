# time module
import time

# random module
import random


# print pause
def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


# print introductory message before game starts
def intro_message(items, options):
    print_pause("\n You find yourself standing in an open savannah "
                "filled with long grass and scattered trees.")
    print_pause(f"Rumor has it that an evil {options} "
                "is around here and has been terrifying "
                "the nearby village")
    print_pause("In front of you is a Manyatta aka a house")
    print_pause("To your right is a dark cave")
    print_pause("In your had you hold your trusty "
                "(but not effective) dagger \n")


# valid input
def valid_input(prompt, choices):
    while True:
        choice = input(prompt).lower()
        if choice in choices:
            return choice
    print_pause(f"Sorry,the option {choice} is invalid. Try again")


# field events
def field_events(items, options):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    response = valid_input("Please enter (1) or (2)\n", ["1", "2"])
    if "1" in response:
        house_events(items, options)
    elif "2" in response:
        # call the cave events here
        cave_events(items, options)
    else:
        return response
        field_events(items, options)


# house events
def house_events(items, options):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door "
                f"opens and out steps a {options}.")
    print_pause(f"Eep! This is the {options}'s house!")
    print_pause(f"The {options} attacks you!\n")
    if "sword" not in items:
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.\n")
    house_response = valid_input("Would you like to (1) fight or (2) "
                                 "run away? \n", ["1", "2"])
    if "1" in house_response:
        if "sword" in items:
            print_pause(f"As the {options} moves to attack, "
                        "you unleash your new sword.")
            print_pause("The Sword of Ogoroth shines brightly in "
                        "your hand as you brace yourself for the "
                        "attack.")
            print_pause(f"But the {options} takes one look at "
                        "your shiny new toy and runs away!")
            print_pause(f"You have rid the town of the {options}.")
            print_pause("Congratulations!! You are victorious!\n")
        else:
            print_pause("You do your best...")
            print_pause("but your dagger is no match for the "
                        f"{options}.")
            print_pause("Ooops! You have been defeated!\n")
    elif "2" in house_response:
        print_pause("You run back into the field. ")
        print_pause("Luckily, you don't seem to have been "
                    "followed.\n")
        field_events(items, options)


# cave_events
def cave_events(items, options):
    if "sword" in items:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten all "
                    " the good stuff. It's just an empty cave "
                    " now.")
        print_pause("You walk back to the field.\n")
        field_events(items, options)
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a "
                    "rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take "
                    "the sword with you.")
        print_pause("You walk back out to the field.\n")
        items.append("sword")
        field_events(items, options)


# play a another round
def play_again():
    play_again = valid_input("Would you like to play again? "
                             "'yes' or 'no' ", ["yes", "no"])
    if "no" in play_again:
        print_pause("Thank you for playing again..Kwaheri")
        exit(0)
    elif "yes" in play_again:
        print_pause("Excellent! lets play another round!")
        play_game()
    else:
        return play_again


# play game
def play_game():
    items = []
    wild_creatures = ["Sangoma", "Popo Bawa", "Jengu", "Grootslang"]
    options = random.choice(wild_creatures)

    intro_message(items, options)
    field_events(items, options)
    play_again()


if __name__ == '__main__':
    play_game()
