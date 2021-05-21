#!/usr/bin/env python
# coding: utf-8

from time import sleep
import sys

def intro():
    print("This is where you introduce your game and say hello.")
    print("Perhaps add some pauses for effect...")
    sleep(2)
    print("""You can type "n", "s", "e", "w" to move north, south, east and west.""")
    print("""You can type "pocket" to see what rubbish is in there.""")
    print("""Type "look" to see what objects are available and the name of the object to take it.""")
    print("""Some items can be used once you pick them up by typing "use" and then the item name.""")
    print("""Finally, you can type "exit" when you get bored!""")

    pocket = ["Just some pocket fluff"]   # This is a list of what your starting pocket contains
    flags = {"flag1": False}   # This is a dictionary that stores when special stuff happens
    room_1(pocket, flags)   # this is your starting room

#######################################################
### these are the general functions used everywhere ###
#######################################################

def open_pocket(pocket):
# displays what's in yer pocket #
    for item in pocket:
        print(item)
    return

def items_available(initial_items, pocket):
# looks at the initial items and ignores anything in your pocket
    available_items = [item for item in initial_items if item not in pocket]
    return available_items

def check_txt(txt, initial_items, pocket):
# general function to respond to words pocket, exit, look, exit and the name of items

    if txt == "pocket":
        open_pocket(pocket)
    elif txt == "exit":
        print("Back to normality!")
        sys.exit()
    elif txt == "look":
        print("There is:")
        for item in items_available(initial_items, pocket):
            print(item)
    elif txt in items_available(initial_items, pocket):
        print("You take the", txt)
        pocket.append(txt)
    else:
        print("?")
    return pocket

def directions(doors, txt, pocket, flags):
# if the user types n, s, e, w this pulls the name of the next room from the room dictionary
# and then jumps to that room
    if txt in doors.keys():
        eval(doors[txt] + "(pocket, flags)")
    else:
        return


###########################################################
### These are the functions for the different locations ###
###########################################################

def room_1(pocket, flags):

    initial_items = ["item 1"]
    doors = {"s": "room_2"}

    print("Welcome to room 1.")
    sleep(1)
    print("There is a door to the south.")

    while True:
        txt = input(">")
        directions(doors, txt, pocket, flags)
        pocket = check_txt(txt, initial_items, pocket)

        # section for special item use
        if txt == "use item 1" and "item 1" in pocket:
            print("you have now used item 1 in the right place!")
            flags["flag1"] = True

def room_2(pocket, flags):

    initial_items = ["item 2"]
    doors = {"n": "room_1", "w": "room_3"}

    print("Welcome to room 2.")
    sleep(1)
    print("There are doors to the north and west.")

    while True:
        txt = input(">")
        directions(doors, txt, pocket, flags)
        pocket = check_txt(txt, initial_items, pocket)

        # section for special item use
        if txt == "use item 2" and flags["flag1"]:
            print("I see you have used item 1 in room 1, you can now use item 2!")
        elif txt == "use item 2" and not flags["flag1"]:
            print("I see you haven't used item 1 in room 1 yet, so you can't use item 2.")

def room_3(pocket, flags):

    initial_items = ["item 3"]
    doors = {"e": "room_2"}
    sleep(1)
    print("There is a door to the east.")

    while True:
        txt = input(">")
        directions(doors, txt, pocket, flags)
        pocket = check_txt(txt, initial_items, pocket)

    # section for special item use


### add more room functions here BEFORE the "intro()" or nothing works! HAHAHAH! ####

intro()



