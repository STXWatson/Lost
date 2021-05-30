
from time import sleep
import sys


def intro():
    print("""You awake on an abandoned submarine.\nYou know that because the words 'Submarine 01170' are printed on the wall and there is no-one else there. """)
    sleep(2)
    print("You decide that you should leave as soon as possible.")
    sleep(2)
    help_txt()
    print("\n")

    # The pocket is a dictionary of items you carry with you
    # If an item is set to "True" they are displayed when you type "pocket"
    # If false they don't appear anymore e.g. you can use or eat them.
    pocket = {"Just some pocket fluff": True}

    # flags is a dictionary that can store when something special happens
    # Allow something you do in one room to affect other rooms
    flags = {"flag1": False, "flag2": False}

    conning_tower(pocket, flags)   # this is your starting room


def help_txt():
    print("""You can type "north", "south", "east", "west", "up", "down" to move in that direction.""")
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
    elif txt == "doors":   # doors = {"north": ["lounge", True]}
        print(door_text)
    elif txt in doors.keys() and doors.get(txt)[1]:
        eval(doors[txt][0] + "(pocket, flags)")
    elif txt in doors.keys() and not doors.get(txt[1]):
        print("The way", txt, "is locked.")
    elif txt in ["north", "south", "east", "west", "up", "down"] and txt not in doors.keys():
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
    doors = {"south": ["room_2", True]}   # format is {direction:[destination,  boolean]}, boolean denotes locked/unlocked

    print(location_text)
    sleep(1)
    print(door_txt)

    while True:
    
    # first check txt for special item use
        txt = input(">")
        if txt == "use item 1" and "item 1" in pocket.keys() and pocket.get("item 1"):
            print("You have now used item 1 in the right place!")
            print("It now vanishes mysteriously")
            flags["flag1"] = True
            pocket["item 1"] = False
        
        else:
    #then general check 
            pocket = check_txt(txt, initial_items, pocket, doors, flags, location_text, door_txt)



def room_2(pocket, flags):

    location_text = "Welcome to room 2."
    door_txt = "There are doors to the north and west."
    initial_items = ["item 2"]
    doors = {"north": ["room_1", True], "west": ["room_3", True]}

    print(location_text)
    sleep(1)
    print(door_txt)

    while True:
        
        txt = input(">")
        
        if txt == "use item 2" and flags["flag1"]:
            print("I see you have used item 1 in room 1, you can now use item 2!")
        elif txt == "use item 2" and "item 2" in pocket.values() and not flags["flag1"]:
            print("I see you haven't used item 1 in room 1 yet, so you can't use item 2.")        

        # section for special item use        
        else:
            pocket = check_txt(txt, initial_items, pocket, doors, flags, location_text, door_txt)




def room_3(pocket, flags):

    location_text = "Welcome to room 3."
    door_txt = "There is a door to the east and a trapdoor leading down."
    initial_items = ["key"]
    if flags["flag2"]:
        doors = {"east": ["room_2", True], "down": ["room_4", True]} #if used key, door unlocked
    else:
        doors = {"east": ["room_2", True], "down": ["room_4", False]}  # else door locked

    print(location_text)
    sleep(1)
    print(door_txt)

    while True:
                
    # first check txt for special item use
        txt = input(">")
        if txt == "use key" and "key" in pocket:
            print("You have unlocked the trapdoor going down!")
            flags["flag2"] = True
            doors = {"east": ["room_2", True], "down": ["room_4", True]}
        
        else:
    # then general check         
            pocket = check_txt(txt, initial_items, pocket, doors, flags, location_text, door_txt)

def room_4(pocket, flags):

    location_text = "Welcome to room 4."
    door_txt = "There are stairs going up."
    initial_items = []
    doors = {"up": ["room_3", True]}

    print(location_text)
    sleep(1)
    print(door_txt)

    while True:
    #
        txt = input(">")
        pocket = check_txt(txt, initial_items, pocket, doors, flags, location_text, door_txt)

    # section for special item use

### add more room functions here BEFORE the "intro()" or nothing works! HAHAHAH! ####

def sea(pocket, flags):
    print("You open the hatch.")
    print("This turns out to be a bad idea.")
    print("You are now dead.")
    print("perhaps you could try again?")
    sleep(3)
    intro()
    
def conning_tower(pocket, flags):

    location_text = "You are in the conning tower."
    door_txt = "There is a ladder leading down and a hatch up above you."
    initial_items = []
    doors = {"down": ["bridge", True], "up": ["sea", True]}   # format is {direction:[destination,  boolean]}, boolean denotes locked/unlocked

    print(location_text)
    sleep(1)
    print(door_txt)

    while True:
        txt = input(">")
        # first check txt for special item use
        if txt == "xxx":
            pass
        
        #then general check 
        else:
            pocket = check_txt(txt, initial_items, pocket, doors, flags, location_text, door_txt)

            
def bridge(pocket, flags):

    location_text = "You are on the Bridge."
    door_txt = "There is a ladder leading up and doors to the west, south and east."
    initial_items = []
    doors = {"up": ["conning_tower", True], "west": ["cupboard", True], "south": ["med_bay", True], 
             "east": ["crew_quarters", True]}   # format is {direction:[destination,  boolean]}, boolean denotes locked/unlocked

    print(location_text)
    sleep(1)
    print(door_txt)

    while True:
        txt = input(">")
        # first check txt for special item use
        if txt == "xxx":
            pass
        
        #then general check 
        else:
            pocket = check_txt(txt, initial_items, pocket, doors, flags, location_text, door_txt)

            
def cupboard(pocket, flags):

    location_text = "You are in a cupboard."
    door_txt = "There is a door east leading back onto the the bridge and another one leading south."
    initial_items = []
    doors = {"south": ["cargo_bay", True], "east": ["bridge", True]}   # format is {direction:[destination,  boolean]}, boolean denotes locked/unlocked

    print(location_text)
    sleep(1)
    print(door_txt)

    while True:
        txt = input(">")
        # first check txt for special item use
        if txt == "xxx":
            pass
        
        #then general check 
        else:
            pocket = check_txt(txt, initial_items, pocket, doors, flags, location_text, door_txt)


def crew_quarters(pocket, flags):

    location_text = "You are in the crew quarters."
    door_txt = "There are doors leading west, south and east."
    initial_items = []
    doors = {"west": ["bridge", True], "south": ["wc", True], "east": ["storage_room", True]}   # format is {direction:[destination,  boolean]}, boolean denotes locked/unlocked

    print(location_text)
    sleep(1)
    print(door_txt)

    while True:
        txt = input(">")
        # first check txt for special item use
        if txt == "xxx":
            pass
        
        #then general check 
        else:
            pocket = check_txt(txt, initial_items, pocket, doors, flags, location_text, door_txt)
 
            
def storage_room(pocket, flags):

    location_text = "You are in a storage room."
    door_txt = "There is a door west leading back to the crew quarters."
    initial_items = []
    doors = {"west": ["crew_quarters", True]}   # format is {direction:[destination,  boolean]}, boolean denotes locked/unlocked

    print(location_text)
    sleep(1)
    print(door_txt)

    while True:
        txt = input(">")
        # first check txt for special item use
        if txt == "xxx":
            pass
        
        #then general check 
        else:
            pocket = check_txt(txt, initial_items, pocket, doors, flags, location_text, door_txt)


def med_bay(pocket, flags):

    location_text = "You are in the medical bay."
    door_txt = "There are doors to the north, west and south"
    initial_items = []
    doors = {"north": ["bridge", True], "south": ["admin", True], "west": ["cargo_bay", True]}   # format is {direction:[destination,  boolean]}, boolean denotes locked/unlocked

    print(location_text)
    sleep(1)
    print(door_txt)

    while True:
        txt = input(">")
        # first check txt for special item use
        if txt == "xxx":
            pass
        
        #then general check 
        else:
            pocket = check_txt(txt, initial_items, pocket, doors, flags, location_text, door_txt)
            
            
def cargo_bay(pocket, flags):

    location_text = "You are in the cargo bay."
    door_txt = "There are doors to the north, south and east and a hatch to the west."
    initial_items = []
    doors = {"north": ["cupboard", True], "south": ["torpedo_bay", True], "west": ["sea", True], "east": ["med_bay", True]}   # format is {direction:[destination,  boolean]}, boolean denotes locked/unlocked

    print(location_text)
    sleep(1)
    print(door_txt)

    while True:
        txt = input(">")
        # first check txt for special item use
        if txt == "xxx":
            pass
        
        #then general check 
        else:
            pocket = check_txt(txt, initial_items, pocket, doors, flags, location_text, door_txt)

            
def torpedo_bay(pocket, flags):

    location_text = "You are in the torpedo bay."
    door_txt = "There are doors leading north and east and a ladder leading down."
    initial_items = []
    doors = {"north": ["cargo_bay", True], "down": ["engine_room", True], "east": ["admin", True]}   # format is {direction:[destination,  boolean]}, boolean denotes locked/unlocked

    print(location_text)
    sleep(1)
    print(door_txt)

    while True:
        txt = input(">")
        # first check txt for special item use
        if txt == "xxx":
            pass
        
        #then general check 
        else:
            pocket = check_txt(txt, initial_items, pocket, doors, flags, location_text, door_txt)
            
            
def admin(pocket, flags):

    location_text = "You are in admin."
    door_txt = "There are doors to the north, west and south."
    initial_items = []
    doors = {"north": ["med_bay", True], "west": ["torpedo_bay", True], "south": ["control_room", True]}   # format is {direction:[destination,  boolean]}, boolean denotes locked/unlocked

    print(location_text)
    sleep(1)
    print(door_txt)

    while True:
        txt = input(">")
        # first check txt for special item use
        if txt == "xxx":
            pass
        
        #then general check 
        else:
            pocket = check_txt(txt, initial_items, pocket, doors, flags, location_text, door_txt)
            
            
def wc(pocket, flags):

    location_text = "You are in the WC."
    door_txt = "There is a door to the north leading back into the crew quarters."
    initial_items = []
    doors = {"north": ["crew_quarters", True]}   # format is {direction:[destination,  boolean]}, boolean denotes locked/unlocked

    print(location_text)
    sleep(1)
    print(door_txt)

    while True:
        txt = input(">")
        # first check txt for special item use
        if txt == "xxx":
            pass
        
        #then general check 
        else:
            pocket = check_txt(txt, initial_items, pocket, doors, flags, location_text, door_txt)

        
def engine_room(pocket, flags):

    location_text = "You are in the engine room."
    door_txt = "There is a ladder leading up."
    initial_items = []
    doors = {"up": ["torpedo_bay", True]}   # format is {direction:[destination,  boolean]}, boolean denotes locked/unlocked

    print(location_text)
    sleep(1)
    print(door_txt)

    while True:
        txt = input(">")
        # first check txt for special item use
        if txt == "xxx":
            pass
        
        #then general check 
        else:
            pocket = check_txt(txt, initial_items, pocket, doors, flags, location_text, door_txt)
            
            
def control_room(pocket, flags):

    location_text = "You are in the control room."
    door_txt = "There is a door to the north and a ladder leading down."
    initial_items = []
    doors = {"north": ["admin", True], "down": ["pump_room", True]}   # format is {direction:[destination,  boolean]}, boolean denotes locked/unlocked

    print(location_text)
    sleep(1)
    print(door_txt)

    while True:
        txt = input(">")
        # first check txt for special item use
        if txt == "xxx":
            pass
        
        #then general check 
        else:
            pocket = check_txt(txt, initial_items, pocket, doors, flags, location_text, door_txt)


def pump_room(pocket, flags):

    location_text = "You are in the pump room."
    door_txt = "There is a ladder leading up."
    initial_items = []
    doors = {"up": ["control_room", True]}   # format is {direction:[destination,  boolean]}, boolean denotes locked/unlocked

    print(location_text)
    sleep(1)
    print(door_txt)

    while True:
        txt = input(">")
        # first check txt for special item use
        if txt == "xxx":
            pass
        
        #then general check 
        else:
            pocket = check_txt(txt, initial_items, pocket, doors, flags, location_text, door_txt)
            
intro()



