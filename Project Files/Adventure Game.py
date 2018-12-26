#Creating Room Class which outlines the features of a room needed by the game
class Room (object):
    def __init__ (self, Name, Description, Connections, Items = [], Locks= [], PointsOfInterest = []):
        self.Name = Name
        self.Description = Description
        self.Connections = Connections
        self.Items = Items #Items, Locks and Points Of Interest are optional features of a room
        self.Locks = Locks
        self.PointsOfInterest = PointsOfInterest
#Defining the details of each room using the class to specify features
Dungeon = {}
Dungeon["MainRoom"] = Room("MainRoom",open("MainRoom.txt") # Calls text file with the description of the room
,{"W": "StorageRoom", "S": "Outside", "E": "ThroneRoom"}, ["torch"])

Dungeon["StorageRoom"] = Room("StorageRoom", open("StorageRoom.txt")
,{"E": "MainRoom"}, ["carpet","key"], [], ["shelf"])

Dungeon["ThroneRoom"] = Room("ThroneRoom", open("ThroneRoom.txt")
,{"W": "MainRoom", "N": "Kitchen"},["lamp"],["N"], ["throne"])

Dungeon["Kitchen"] = Room("Kitchen", open("Kitchen.txt")
,{"S": "ThroneRoom", "W": "SecretPassage"}, ["matches", "pots"], ["W"], "crate")

Dungeon["SecretPassage"] = Room("SecretPassage", open("SecretPassage.txt")
,{"W": "KingsChamber", "E": "Kitchen"})

Dungeon["KingsChamber"] = Room("KingsChamber", open("KingsChamber.txt")
,{"E": "SecretPassage", "N": "EndRoom"}, ["tile1", "tile2", "tile3"], ["N"])

Dungeon["EndRoom"] = Room("EndRoom", open("EndRoom.txt") ,{})

Dungeon["Outside"] = Room("Outside", open("Outside.txt") ,{})

#Creating a Player to store collected items and the current room
class player(object):
    def __init__(self):
        self.CurrentRoom = Dungeon["MainRoom"] # Setting where the Player will begin
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
ItemDictionary["lamp"] = Item("lamp", "You examine the Oil Lamp hung on the side of the throne room, still a small amount of fuel left")
ItemDictionary["carpet"] = Item("carpet", "Under the Carpet you find a small hole. Within which you find a small key with a small metal cooking pot forged onto the end")
ItemDictionary["torch"] = Item("torch", "An old wooden torch that has begun to rot with time, it probably wont light.")
ItemDictionary["pots"] = Item("pot", "A large metal cooking pot, the metal itself has no value to it.")

#Points of interest (Can be looked at but not picked up)
class PointsOfInterest(object):
    def __init__(self, Name, Description):
        self.Name = Name
        self.Description = Description
#Defining each Point of Interest
PointsOfInterestDictionary = {}
PointsOfInterestDictionary["shelf"] = PointsOfInterest("shelf", "A long shelf that no doubt once held a high ammount of supplies for the palace, now they stand empty or strewn with useless items.")
PointsOfInterestDictionary["throne"] = PointsOfInterest("throne", "You once heard rumours that this throne contained as much gold as there was when the kingdom was at its richest. Now it has all been stripped away.")
PointsOfInterestDictionary["crate"] = PointsOfInterest("crate", "You move the crate to one side find a secret passage behind it. It is too dark to enter without light.")
PointsOfInterestDictionary["banner"] = PointsOfInterest("banner", "Hanging above the secret passage is a tattered old banner which displays what remains of the family crest, though there is a large amount of missing detail.")
PointsOfInterestDictionary["painting"] = PointsOfInterest("painting", "On the wall opposite the passage hangs a painting of the monarchs family, the painting is very damaged with the monarch's face missing completely")

#Defining a single function for when the Player attempts to travel a direction with no connection
def WrongDircetion():
    print ("You Can not go that way.")

#Movement Function,
def PlayerMovement(PlayerChoice):
    if len(PlayerChoice) < 2: #Checks the player has entered a direction
        print ("Please choose a direction")
    #Checks each direction the player could have entered
    elif PlayerChoice[1] == "north":
        #Check if room has a connection in that direction
        if "N" in Player.CurrentRoom.Connections:
            #check if connection is locked
            if "N" in Player.CurrentRoom.Locks:
                print ("The door is Locked")
            else:
                print ("going north")
                #Move player
                Player.CurrentRoom = Dungeon[Player.CurrentRoom.Connections["N"]]
        else:
            WrongDircetion()
    elif PlayerChoice[1] == "south":
        if "S" in Player.CurrentRoom.Connections: #No rooms have south locks and so no check is needed
            print ("going south")
            Player.CurrentRoom = Dungeon[Player.CurrentRoom.Connections["S"]]
        else:
            WrongDircetion()
    elif PlayerChoice[1] == "east":
        if "E" in Player.CurrentRoom.Connections: #No rooms have East locks and so a check is not needed
            print ("going east")
            Player.CurrentRoom = Dungeon[Player.CurrentRoom.Connections["E"]]
        else:
            WrongDircetion()
    elif PlayerChoice[1] == "west":
        if "W" in Player.CurrentRoom.Connections:
            if "W" in Player.CurrentRoom.Locks: #Only one room has a west connection in this game so a custom response can be given
                print ("The passage is too dark. Find something to light your way")
            else:
                print ("going west")
                Player.CurrentRoom = Dungeon[Player.CurrentRoom.Connections["W"]]
        else:
            WrongDircetion() #Rrevents repetition of code
    else:
        print ("That is not a valid direction")

def PlayerLook(PlayerChoice):
    if len(PlayerChoice) < 2:
        #If the Player enters only Look the game will print the rooms description
        print (Player.CurrentRoom.Description.read())
    elif PlayerChoice[1] in Player.CurrentRoom.Items:
        #prints item description if item is in the room
        print (ItemDictionary[PlayerChoice[1]].Description)
    elif PlayerChoice[1] in Player.CurrentRoom.PointsOfInterest:
        #If the Player enters a point of interest in the room rather than an item
        print (PointsOfInterestDictionary[PlayerChoice[1]].Description)
    else:
        print ("That is not a thing in this room")

def PlayerTake(PlayerChoice):
    if len(PlayerChoice) < 2: #Checks the player has specified an item to take
        print ("Please choose an item to pick up")
    elif PlayerChoice[1] in Player.CurrentRoom.Items: #If item is in the room
        Player.Inventory.append(PlayerChoice[1]) #Add the item to the inventory
        Player.CurrentRoom.Items.remove(PlayerChoice[1]) #Removes item from the room
        print (PlayerChoice[1] + " was added to your inventory") #Informs the player that the item has been taken
    else:
        print("That item does not exist in this room")

def PlayerDrop(PlayerChoice): #Reverse of taking item
    if len(PlayerChoice) < 2:
        print ("Please choose an item to drop")
    elif PlayerChoice[1] in Player.Inventory:
        Player.Inventory.remove(PlayerChoice[1])
        Player.CurrentRoom.Items.append(PlayerChoice[1])
        print ("You dropped " + PlayerChoice[1])
    else:
        print ("You do not have that item")

def WrongItemUse(): #Preventing repeated code
    print ("Now isnt the time to use that.")

def PlayerUse(PlayerChoice):
    if len(PlayerChoice) < 2: #Checking the Player specified an item to use
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
        elif PlayerChoice[1] == "lamp":
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
        elif PlayerChoice[1] == "matches":
            if Player.CurrentRoom == Dungeon["Kitchen"]:
                if "lamp" in Player.Inventory:
                    print ("You use the match to light the lamp. You can now pass through the passage")
                    Player.CurrentRoom.Locks = []
                else:
                    print ("You have nothing to light with the match")
            else:
                WrongItemUse()
        #Using Tile2 to open end room
        #checks for which tile the player is holding
        elif PlayerChoice[1] == "tile1":
            #incorrect does nothing
            if Player.CurrentRoom == Dungeon["KingsChamber"]:
                print ("You place the tile in the slot on the wall, but nothing happens. You remove the tile.")
        elif PlayerChoice[1] == "tile2":
            #correct tile opens ending
            if Player.CurrentRoom == Dungeon["KingsChamber"]:
                Player.CurrentRoom.Locks = [] #Only tile2 removes the lock to the end room
                Player.Inventory.remove(PlayerChoice[1])
                print ("You place the tile into the slot on the wall. Suddenly the whole wall begins shaking and the section behind the bed slides back to reveal a new room to the North.")
        elif PlayerChoice[1] == "tile3":
            if Player.CurrentRoom == Dungeon["KingsChamber"]:
                print ("You place the tile in the slot on the wall, but nothing happens. You remove the tile.")
        else: #The item is in the players inventory but has no use
            print("That item has no use")
    else:
        print ("You do not have that item in your inventory")

def PlayerHelp(): # Prints all commands usable by the player and what they do
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
        Running = False
    elif Player.CurrentRoom == Dungeon["EndRoom"]:
        print (Player.CurrentRoom.Description.read())
        Running = False

#Running the Game
Running = True #Starts loop till game ends
print ("""You are a famous explorer who has come to the ruins of an ancient monarchs palace seeking the legendary treasure they left behind
Many have failed on this journey, can you find what they could not?
Use help to see a list of the commands you can use to move around the palace""")
while Running == True:
    #Take player input and split on space into a list
    PlayerChoice = input("What will you do? ")
    PlayerChoice = PlayerChoice.lower()
    PlayerChoice = PlayerChoice.split(" ")
    ProcessInput(PlayerChoice)
