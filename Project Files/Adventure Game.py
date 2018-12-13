#Creating Room Class
class Room (object):
    def __init__ (self, Name, Description, Connections, Items = [], Locks= []):
        self.Name = Name
        self.Description = Description
        self.Connections = Connections
        self.Items = Items
        self.Locks = Locks
#Defining each room
Dungeon = {}
Dungeon["MainRoom"] = Room("MainRoom",open("MainRoom.txt") # Calls text file with the description of 
,{"W": "StorageRoom", "S": "Outside", "E": "ThroneRoom"})

Dungeon["StorageRoom"] = Room("StorageRoom", open("StorageRoom.txt")
,{"E": "MainRoom"}, ["carpet","key"])

Dungeon["ThroneRoom"] = Room("ThroneRoom", open("ThroneRoom.txt")
,{"W": "MainRoom", "N": "Kitchen"},["oillamp"],["N"])

Dungeon["Kitchen"] = Room("Kitchen", open("Kitchen.txt")
,{"S": "ThroneRoom", "W": "SecretPassage"}, ["crate", "matches"], ["W"])

Dungeon["SecretPassage"] = Room("SecretPassage", open("SecretPassage.txt")
,{"W": "KingsChamber", "E": "Kitchen"})

Dungeon["KingsChamber"] = Room("KingsChamber", open("KingsChamber.txt")
,{"E": "SecretPassage", "N": "EndRoom"}, ["tile1", "tile2", "tile3"], ["N"])

Dungeon["EndRoom"] = Room("EndRoom", open("EndRoom.txt") ,{})

Dungeon["Outside"] = Room("Outside", open("Outside.txt") ,{})

#Creating Player Class
class player(object):
    def __init__(self):
        self.CurrentRoom = Dungeon["MainRoom"]
        self.Inventory = []
Player = player()

#Item class
class Item (object):
    def __init__ (self, Name, Description):
        self.Name = Name
        self.Description = Description
#Defining each Item
ItemDictionary = {}
ItemDictionary["key"] = Item("kitchenKey", "A small key with a cooking pot forged onto the end")
ItemDictionary["tile1"] = Item("tile1", "This tile depicts a man standing in a triumphant pose atop the bodies of his enemies.")
ItemDictionary["tile2"] = Item("tile2", "This tile depicts a large bear stood upright, broadsword in its left hand.")
ItemDictionary["tile3"] = Item("tile3", "This tile depicts a man raising a shield to cover himself from a dragons flame.”")
ItemDictionary["matches"] = Item("matches", "A small box of unused matches")
ItemDictionary["oillamp"] = Item("oillamp", "You examine the Oil Lamp hung on the side of the throne room, still a small amount of fuel left")
ItemDictionary["carpet"] = Item("carpet", "Under the Carpet you find a small hole. Within which you find a small key with a small metal cooking pot forged onto the end")
ItemDictionary["crate"] = Item("crate", "You move the crate to one side find a secret passage behind it. It is too dark to enter without light.")

#Movement Function
def PlayerMovement(PlayerChoice):
    if len(PlayerChoice) < 2:
        print ("Please choose a direction")
    elif PlayerChoice[1] == "north":
        #Check if room has a north connection
        if "N" in Player.CurrentRoom.Connections:
            #check if connection is locked
            if "N" in Player.CurrentRoom.Locks:
                print ("The door is Locked")
            else:
                print ("going north")
                #Move player
                Player.CurrentRoom = Dungeon[Player.CurrentRoom.Connections["N"]]
        else:
            print ("You can not go that way")
    elif PlayerChoice[1] == "south":
        if "S" in Player.CurrentRoom.Connections:
            print ("going south")
            Player.CurrentRoom = Dungeon[Player.CurrentRoom.Connections["S"]]
        else:
            print ("You can not go that way")
    elif PlayerChoice[1] == "east":
        if "E" in Player.CurrentRoom.Connections:
            print ("going east")
            Player.CurrentRoom = Dungeon[Player.CurrentRoom.Connections["E"]]
        else:
            print ("You can not go that way")
    elif PlayerChoice[1] == "west":
        if "W" in Player.CurrentRoom.Connections:
            if "W" in Player.CurrentRoom.Locks:
                print ("The passage is too dark. Find something to light your way")
            else:
                print ("going west")
                Player.CurrentRoom = Dungeon[Player.CurrentRoom.Connections["W"]]
        else:
            print ("You can not go that way")
    else:
        print ("That is not a valid direction")

def PlayerLook(PlayerChoice):
    if len(PlayerChoice) < 2:
        #prints room decription
        print (Player.CurrentRoom.Description.read())
    elif PlayerChoice[1] in Player.CurrentRoom.Items:
        #prints item description if item is in the room
        print (ItemDictionary[PlayerChoice[1]].Description)
    else:
        print ("That item is not in this room")

def PlayerTake(PlayerChoice):
    if len(PlayerChoice) < 2:
        print ("Please choose an item to pick up")
    elif PlayerChoice[1] in Player.CurrentRoom.Items:
        #Remove item from room items and add to inventory
        Player.Inventory.append(PlayerChoice[1])
        Player.CurrentRoom.Items.remove(PlayerChoice[1])
        print (PlayerChoice[1] + " was added to your inventory")
    else:
        print("That item does not exist in this room")

def PlayerDrop(PlayerChoice):
    if len(PlayerChoice) < 2:
        print ("Please choose an item to drop")
    elif PlayerChoice[1] in Player.Inventory:
        #Reverse of taking item
        Player.Inventory.remove(PlayerChoice[1])
        Player.CurrentRoom.Items.append(PlayerChoice[1])
        print ("You dropped " + PlayerChoice[1])
    else:
        print ("You do not have that item")

def WrongItemUse():
    print ("A voice echoes through the room. There is a time and a place for everything, but not now!")

def PlayerUse(PlayerChoice):
    if len(PlayerChoice) < 2:
        print ("Please choose an item to use")
    elif PlayerChoice[1] in Player.Inventory:
        if PlayerChoice[1] == "key":
            #Checks that player is in the correct room to use item
            if  Player.CurrentRoom == Dungeon["ThroneRoom"]:
                #removes lock
                Player.CurrentRoom.Locks = []
                print("You turn the key in the door and it unlocks")
            else:
                WrongItemUse()
        #Using Lamp
        if PlayerChoice[1] == "oillamp":
            if Player.CurrentRoom == Dungeon["Kitchen"]:
                #checks for lamp and matches
                if "matches" in Player.Inventory:
                    print ("You use the match to light the lamp. You can now pass through the passage")
                    Player.CurrentRoom.Locks = []
                else:
                    print ("You have nothing to light the lamp with")
            else:
                WrongItemUse()
        #Using Matches (Same effect as using Lamp)
        if PlayerChoice[1] == "matches":
            if Player.CurrentRoom == Dungeon["Kitchen"]:
                if "oillamp" in Player.Inventory:
                    print ("You use the match to light the lamp. You can now pass through the passage")
                    Player.CurrentRoom.Locks = []
                else:
                    print ("You have nothing to light with the match")
            else:
                WrongItemUse()
        #Using Tile2 to open end room
        #checks for which tile the player is holding
        if PlayerChoice[1] == "tile1":
            #incorrect does nothing
            if Player.CurrentRoom == Dungeon["KingsChamber"]:
                print ("You place the tile in the slot on the wall, but nothing happens. You remove the tile.")
        if PlayerChoice[1] == "tile2":
            #correct tile opens ending
            if Player.CurrentRoom == Dungeon["KingsChamber"]:
                Player.CurrentRoom.Locks = []
                Player.Inventory.remove(PlayerChoice[1])
                print ("You place the tile into the slot on the wall. Suddenly the whole wall begins shaking and the section behind the bed slides back to reveal a new room to the North.")
        if PlayerChoice[1] == "tile3":
            if Player.CurrentRoom == Dungeon["KingsChamber"]:
                print ("You place the tile in the slot on the wall, but nothing happens. You remove the tile.")
    else:
        print ("You do not have that item in your inventory")

def PlayerHelp():
    print ("""These are the commands you can use:
    Go (Direction)- Moves your character
    Look- Gives you the room Description
    Look (Item)- Gives you the description for the item specified.
    Take (Item)- Takes the item from the room and puts it in your inventory
    Drop (Item)- Drops the item specified in the rooms
    Use (Item)- Uses the item for its purpose if you are in the correct room""")

#Processing Player Input Function
def ProcessInput(PlayerChoice):
    #Movement
    if PlayerChoice[0] == "go":
        PlayerMovement(PlayerChoice)

    #Looking Commands
    elif PlayerChoice[0] == "look":
        PlayerLook(PlayerChoice)

    #Take object
    elif PlayerChoice[0] == "take":
        PlayerTake(PlayerChoice)

    #Drop Item
    elif PlayerChoice[0] == "drop":
        PlayerDrop(PlayerChoice)

    #Use Item
    elif PlayerChoice[0] == "use":
        PlayerUse(PlayerChoice)

    #Help Command
    elif PlayerChoice[0] == "help":
        PlayerHelp()

    else:
        print ("That is not a valid command")
    #Checking for the two scripted ending Room
    if Player.CurrentRoom == Dungeon["Outside"]:
        print (Player.CurrentRoom.Description.read())
        Running = false
    elif Player.CurrentRoom == Dungeon["EndRoom"]:
        print (Player.CurrentRoom.Description.read())
        Running = false

#Running the Game
Running = True
print ("""You are a famous explorer who has come to the ruins of an ancient monarchs palace seeking the legendary treasure they left behind
Many have failed on this journey, can you find what they could not?
Use help to see a list of the commands you can use to move around the palace""")
while Running == True:
    #Take player input and split on space into a list
    PlayerChoice = input("What will you do? ")
    PlayerChoice = PlayerChoice.lower()
    PlayerChoice = PlayerChoice.split(" ")
    ProcessInput(PlayerChoice)
