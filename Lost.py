#!/usr/bin/env python
# coding: utf-8

from time import sleep
import sys

def intro():
    print("Welcome to somewhere.\nNot sure where, but it hums and smells a bit like a space ship.")
    sleep(1)
    print("So let's go with that.")
    sleep(1)
    print("\n")
    print("You can type n, s, e, w to move north, south, east and west.")
    print("You can type pocket to see what rubbish is in there.")
    print("Type look to see what objects are available and the name of the object to take it (theft).")
    print("Some items can be used once you pick them up by typing use and then the item name.")
    print("Finally, you can type exit when you get bored!")

    pocket = ["Just some pocket fluff"]   # This is what your starting pocket contains
    flags = {"space suit": False, "oxygen tank": False}   # This is where stuff that happens in stored
    airlock(pocket, flags)   # this is your starting room

#######################################################
### these are the general functions used everywhere ###
#######################################################

def open_pocket(pocket):
    for item in pocket:
        print(item)
    return

def items_available(initial_items, pocket):
    available_items = [item for item in initial_items if item not in pocket]
    return available_items

def check_txt(txt, initial_items, pocket):

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
    if txt in doors.keys():
        eval(doors[txt] + "(pocket, flags)")
    else:
        return


###########################################################
### These are the functions for the different locations ###
###########################################################

def airlock(pocket, flags):

    initial_items = ["torch"]
    doors = {"s": "corridor1", "n": "space"}

    print("You're in an airlock, there's not much room.")
    print("There's a device-thingy screwed to the wall to help you put on space suits.")
    sleep(1)
    print("There are doors to the north and south.")

    while True:
        txt = input(">")
        directions(doors, txt, pocket, flags)
        pocket = check_txt(txt, initial_items, pocket)

        # section for special item use
        if txt == "use space suit" and "space suit" in pocket:
            print("You use the wall device to help you put on the space suit.")
            sleep(2)
            print("It was a bit inconvenient in your pocket anyway.")
            flags["space suit"] = True


def space(pocket, flags):

    if flags["space suit"] and flags["oxygen tank"]:
        print("You escape into space and thanks to your space suit you don't die.")
        sleep(2)
        print("You float out towards the nearby escape pod and head home.")
        sleep(2)
        print("Good bye!")
        sys.exit()
    else:
        print("Yep, that's the airlock door to space.")
        sleep(2)
        print("No amount of pocket fluff can save you now.")
        print("You're dead.")
        sleep(2)
        print("try again.")
        print("\n")
        sys.exit()

def corridor1(pocket, flags):

    initial_items = ["shoelace"]
    doors = {"n": "airlock", "w": "engineering", "s": "control_room", "e": "corridor2"}
    print("You are in a short corridor with doors to the north, south, east and west.")
    print("There are no windows to enjoy the view")

    while True:
        txt = input(">")
        directions(doors, txt, pocket, flags)
        pocket = check_txt(txt, initial_items, pocket)


def engineering(pocket, flags):

    initial_items = ["mop", "screwdriver"]
    doors = {"s": "engineering_cupboard","e": "corridor1"}

    print("You are in the engineer room, there is an exceptional number of flashing lights and twiddly things.")
    print("You are sorely tempted to press all of them.")
    print("There are doors to the south and east.")
    
    while True:
        txt = input(">")
        directions(doors, txt, pocket, flags)
        pocket = check_txt(txt, initial_items, pocket)


def engineering_cupboard(pocket, flags):

    initial_items = ["wasp spray"]
    doors = {"n": "engineering"}

    print("You are in a dark cupboard full of tools and broken things.")
    print("It's a bit of a mess.")
    print("A panel is half-hanging off one wall with something hidden behind it.")
    print("There is a door out to the north.")
    
    while True:
        txt = input(">")
        directions(doors, txt, pocket, flags)
        pocket = check_txt(txt, initial_items, pocket)

        # section for special item use
        if txt == "use hammer" and "hammer" in pocket:
            print("You swing the hammer at the loose panel and it comes off completely.")
            sleep(2)
            print("CLANG!")
            sleep(3)
            print("CLANGGETY- CLANG!")
            sleep(3)
            print("[clang]")
            sleep(2)
            print("That last clang was an oxygen tank falling to the floor.")
            print("You pick it up and place it in your increasingly full pocket.")
            pocket.append("oxygen tank")

def control_room(pocket, flags):

    initial_items = ["pirate hat", "duct tape"]
    doors = {"n": "corridor1"}

    print("This is the control room, and it's pretty fancy.")
    print("There's an important chair in the middle of the room that someone important might sit on.")
    sleep(1)
    print("This person isn't you.")
    sleep(1)
    print("There's a door out to the north.")
    
    while True:
        txt = input(">")
        directions(doors, txt, pocket, flags)
        pocket = check_txt(txt, initial_items, pocket)

        # section for special item use

        
def corridor2(pocket, flags):

    initial_items = []
    doors = {"n": "terrarium", "w": "corridor1", "s": "sleeping_quarters"}

    print("You are in another corridor, a bit longer than the last but no more interesting.")
    sleep(1)
    print("What's with the lack of windows?")
    print("There are doors to the north, west and south.")

    while True:
        txt = input(">")
        directions(doors, txt, pocket, flags)
        pocket = check_txt(txt, initial_items, pocket)

def sleeping_quarters(pocket, flags):

    initial_items = ["sock", "hammer"]
    doors = {"n": "corridor2", "w": "bathroom"}

    print("You are in the sleeping quarters, it is full of bed.")
    print("There are also a lot of single socks everywhere.")
    sleep(1)
    print("you've always wondered where these end up.")
    print("There are doors to the west and north.")
    
    while True:
        txt = input(">")
        directions(doors, txt, pocket, flags)
        pocket = check_txt(txt, initial_items, pocket)
        
def bathroom(pocket, flags):

    initial_items = ["rubber duck"]
    doors = {"e": "sleeping_quarters"}

    print("This is the bathroom. It's a room with a bath.")
    sleep(1)
    print("That feels a little surprising for a space ship.")
    print("But there are sharp implements around the place.")
    print("There's a door out to the east.")
    
    while True:
        txt = input(">")
        directions(doors, txt, pocket, flags)
        pocket = check_txt(txt, initial_items, pocket)

        # special item use here
        if txt == "use duct tape" and "duct tape" in pocket and "oxygen tank" in pocket and flags["space suit"]:
            print("You use a sharp implement to cut the duct tape.")
            print("You use the duct tape to secure the oxygen tank to the space suit.")
            sleep(2)
            print("Hooray for duct tape and sharp implements")
            flags["oxygen tank"] = True

def terrarium(pocket, flags):

    initial_items = []
    doors = {"n": "cafe", "s": "corridor2", "e": "cupboard"}

    print("This is the terrarium, a giant garden in space covered with a great glass dome.")
    sleep(1)
    print("At last! Windows!")
    print("There are doors to the north, south and east.")
    
    while True:
        txt = input(">")
        directions(doors, txt, pocket, flags)
        pocket = check_txt(txt, initial_items, pocket)
        
def cafe(pocket, flags):

    initial_items = ["sugar sachet", "stale biscuit"]
    doors = {"s": "terrarium"}

    print("You're in a cafe. There are machines that served hot drinks and a glass case with few stale biscuits.")
    print("A window looks out onto the terrarium.")
    print("There is a door out to the south.")

    while True:
        txt = input(">")
        directions(doors, txt, pocket, flags)
        pocket = check_txt(txt, initial_items, pocket)

def cupboard(pocket, flags):

    initial_items = ["rake", "space suit"]
    doors = {"w": "terrarium"}

    print("You're in a dark cupboard. You can dimly make out some gardening tools and a hose pipe that is tangling everything up.")
    print("It smell a bit mouldy.")
    print("There is a door out to the west.")
    
    while True:
        txt = input(">")
        directions(doors, txt, pocket, flags)
        pocket = check_txt(txt, initial_items, pocket)

        #section for special item use



intro()



