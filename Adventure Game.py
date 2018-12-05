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
Dungeon["MainRoom"] = Room("MainRoom", "Description here",{"W": "StorageRoom", "S": "Outside", "E": "ThroneRoom"})
Dungeon["StorageRoom"] = Room("StorageRoom", "Description here",{"E": "MainRoom"}, ["Small Key"])
Dungeon["ThroneRoom"] = Room("ThroneRoom", "Description here",{"W": "MainRoom", "N": "Kitchen"},["Oil Lamp"],["N"])
Dungeon["Kitchen"] = Room("Kitchen", "Description here",{"S": "ThroneRoom", "W": "SecretPassage"}, ["Matches"], ["W"])
Dungeon["SecretPassage"] = Room("SecretPassage", "Description here",{"W": "KingsChamber", "E": "Kitchen"})
Dungeon["KingsChamber"] = Room("KingsChamber", "Description here",{"E": "SecretPassage", "N": "EndRoom"}, ["FloorTile"], ["N"])
Dungeon["EndRoom"] = Room("EndRoom", "Description here",{})
Dungeon["Outside"] = Room("Outside", "Description here",{})

#Creating Player Class
class player(object):
    def __init__(self):
        self.CurrentRoom = Dungeon["MainRoom"]
        self.Inventory = []
Player = player()

#Processing Player Input Function
def ProcessInput(PlayerChoice):
    if PlayerChoice[0] == "go":
        if PlayerChoice[1] == "north":
            print ("going north")
            if "N" in Player.CurrentRoom.Connections:
                Player.CurrentRoom = Dungeon[Player.CurrentRoom.Connections["N"]]
            else:
                print ("You can not go that way")
        elif PlayerChoice[1] == "south":
            print ("soing south")
            if "S" in Player.CurrentRoom.Connections:
                Player.CurrentRoom = Dungeon[Player.CurrentRoom.Connections["S"]]
            else:
                print ("You can not go that way")
        elif PlayerChoice[1] == "east":
            print ("going east")
            if "E" in Player.CurrentRoom.Connections:
                Player.CurrentRoom = Dungeon[Player.CurrentRoom.Connections["E"]]
            else:
                print ("You can not go that way")
        elif PlayerChoice[1] == "west":
            print ("going west")
            if "W" in Player.CurrentRoom.Connections:
                Player.CurrentRoom = Dungeon[Player.CurrentRoom.Connections["W"]]
            else:
                print ("You can not go that way")

        else:
            print ("That is not a valid direction")


#Processing Player Input
Running = True
while Running == True:
    #Take player input and split on space into a list
    PlayerChoice = input("What will you do? ")
    PlayerChoice = PlayerChoice.lower()
    PlayerChoice = PlayerChoice.split(" ")
    ProcessInput(PlayerChoice)
