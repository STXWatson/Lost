#!/usr/bin/env python
# coding: utf-8

from time import sleep
import sys

def intro():
    print("This is where you introduce your game and say hello.")
    print("Perhaps add some pauses for effect...")
    sleep(2)
    help_txt()
    print("\n")

    # The pocket is a dictionary of items you carry with you
    # If an item is set to "True" they are displayed when you type "pocket"
    # If false they don't appear anymore e.g. you can use or eat them.
    pocket = {"Just some pocket fluff": True}

    # flags is a dictionary that can store when something special happens
    # Allow something you do in one room to affect other rooms
    flags = {"flag1": False}

    room_1(pocket, flags)   # this is your starting room

def help_txt():
    print("""You can type "north", "south", "east", "west" to move in that direction.""")
    print("""You can type "pocket" to see what rubbish is in there.""")
    print("""Type "look" to see what objects are available and the name of the object to take it.""")
    print("""Some items can be used once you pick them up by typing "use" and then the item name.""")
    print("""You can type "where" or "doors" to repeat the location information for that room.""")
    print("""If you forget any of this type "help" to hear it all again.""")
    print("""Finally, you can type "exit" when you get bored!""")

#######################################################
### these are the general functions used everywhere ###
#######################################################

def open_pocket(pocket):
# displays what's in yer pocket #
    for item in pocket.keys():
        if pocket[item]:  # only prints item if it is tagged as True
            print(item)
    return

def items_available(initial_items, pocket):
# looks at the initial items and ignores anything in your pocket
    available_items = [item for item in initial_items if item not in pocket.keys()]
    return available_items

def check_txt(txt, initial_items, pocket, doors, flags, location_text, door_text):
# general function to respond to words pocket, exit, look, exit, etc

    if txt == "pocket":
        open_pocket(pocket)
    elif txt == "exit":
        print("Back to normality!")
        sys.exit()
    elif txt == "look":
        print("You can see:")
        if len(items_available(initial_items, pocket)) != 0:  #print any available items
            for item in items_available(initial_items, pocket):
                print(item)
        else:
            print("Absolutely nothing.")  # if no items available, print this!
    elif txt in items_available(initial_items, pocket):
        print("You take the", txt)
        pocket[txt] = True
    elif txt == "where":
        print(location_text)
    elif txt == "doors":
        print(door_text)
    elif txt in doors.keys():
        eval(doors[txt] + "(pocket, flags)")
    elif txt in ["north", "south", "east", "west"] and txt not in doors.keys():
        print("You can't go in that direction.")
    elif txt == "help":
        help_txt()
    else:
        print("?")
    return pocket

###########################################################
### These are the functions for the different locations ###
###########################################################

def room_1(pocket, flags):

    location_text = "Welcome to room 1."
    door_txt = "There is a door to the south."
    initial_items = ["item 1"]
    doors = {"south": "room_2"}

    print(location_text)
    sleep(1)
    print(door_txt)

    while True:
        txt = input(">")
        pocket = check_txt(txt, initial_items, pocket, doors, flags, location_text, door_txt)

        # section for special item use
        if txt == "use item 1" and "item 1" in pocket.keys() and pocket.get("item 1"):
            print("You have now used item 1 in the right place!")
            print("It now vanishes mysteriously")
            flags["flag1"] = True
            pocket["item 1"] = False

def room_2(pocket, flags):

    location_text = "Welcome to room 2."
    door_txt = "There are doors to the north and west."
    initial_items = ["item 2"]
    doors = {"north": "room_1", "west": "room_3"}

    print(location_text)
    sleep(1)
    print(door_txt)

    while True:
        txt = input(">")
        pocket = check_txt(txt, initial_items, pocket, doors, flags, location_text, door_txt)

        # section for special item use
        if txt == "use item 2" and flags["flag1"]:
            print("I see you have used item 1 in room 1, you can now use item 2!")
        elif txt == "use item 2" and "item 2" in pocket.values() and not flags["flag1"]:
            print("I see you haven't used item 1 in room 1 yet, so you can't use item 2.")

def room_3(pocket, flags):

    location_text = "Welcome to room 3."
    door_txt = "There is a door to the east."
    initial_items = ["item 3"]
    doors = {"east": "room_2"}

    print(location_text)
    sleep(1)
    print(door_txt)

    while True:
        txt = input(">")
        pocket = check_txt(txt, initial_items, pocket, doors, flags, location_text, door_txt)

    # section for special item use


### add more room functions here BEFORE the "intro()" or nothing works! HAHAHAH! ####

intro()



