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
Dungeon["MainRoom"] = Room("MainRoom", """You enter what appears to be the main entrance room of the ruined palace.
Four pillars stand, weathered and damaged, one in each corner of the room. Wooden torches surround the outer walls, unlit and rotting away. Moss grows through many cracks in the floor, ceiling and walls.
To the South is the entrance door, still slightly open from your entrance.
To the North is a large, impressive door with the old monarch’s family crest engraved onto it, a large bear stood upright, broadsword in its left hand, though its colour has faded with time.
To the East is a slightly less impressive but still grand door, more worn and weathered than the Northern door. The symbol of a throne is engraved onto this door.
To the West is an ordinary wooden door, far less grand than the others in the room. Time has taken its tole on this door however there is a vague chest engraving upon it."""
,{"W": "StorageRoom", "S": "Outside", "E": "ThroneRoom"})

Dungeon["StorageRoom"] = Room("StorageRoom", """The door gives a loud creek as you pass through into what was clearly once a storage chamber for palace supplies.
However, time and looting have left very few items in the room.
A large central shelfing unit runs down the centre of the room while wall mounted shelfs run along the two side walls.
A small carpet sits under part of the shelf, its corner crumpled to reveal part of a small hidden hole.
Nothing remains on the central shelf while the side shelfs are covered in the crumbs of food and shards of wood.
The only door to this room leads back into the main entrance area to the west."""
,{"E": "MainRoom"}, ["carpet","key"])

Dungeon["ThroneRoom"] = Room("ThroneRoom", """You open the door marked with the throne and find yourself (Rather predictably) in the main throne room of the palace.
At the far east end of the room lays the monarchs throne, fallen onto its side and missing the golden furnishings that marked it as the seat of the king.
Next to it in a similarly ruined state lays the seat of the monarch’s wife, it too has had all that made it valuable removed.
Oil lamps line the walls, they too are unlit but still contain a small amount of oil, left behind by looters.
A tattered and faded red carpet stretches from the eastern door up to the thrones themselves.
To the West is the door to the main entrance room.
In the North Eastern corner of the room, behind both thrones, is a door with a cooking pot engraved onto it."""
,{"W": "MainRoom", "N": "Kitchen"},["oillamp"],["N"])

Dungeon["Kitchen"] = Room("Kitchen", """With a small ammount of force you open the door into the palace’s kitchen area.
Metal pots, pans and other cooking equipment are scattered around the room both across the many worktops and around the floor.
Small remains of food are strewn across the floor, too old for even the rats to eat at this time.
The only missing items from the room are large, sharp preparation knifes and the monarch’s famous solid gold cutlery.
On the ground by the door is a small box of Matches.
To the south is the door back into the throne room.
A small crate sits in a gap between the work stations on the western wall. It looks considerably less weathered and damaged than its surroundings."""
,{"S": "ThroneRoom", "W": "SecretPassage"}, ["crate", "matches"], ["W"])

Dungeon["SecretPassage"] = Room("SecretPassage", """You light the oil lamp with the match you have found and enter the secret passage;
the walls are rough and seem to have been dug in a rush. Cobwebs line the roof, but the spiders that made them are nowhere to be found.
The Eastern entrance leads to the kitchen.
The Western entrance appears to lead to into the Kings chamber."""
,{"W": "KingsChamber", "E": "Kitchen"})

Dungeon["KingsChamber"] = Room("KingsChamber", """You exit the secret passage and enter the kings chamber from behind a banner which bears the family crest.
The room appeared to once be the grandest in the entire palace, however now it stands in ruin with all items of value torn out and the chests looted.
A large bed sits facing along the centre of the northern wall, facing the rooms southern entrance.
Two paintings remain, likely un-looted due to the damage present on the artwork.
One hangs directly across from the passage and shows the entire royal family, the monarch with his wife by his side and their two children standing in front.
The second painting hangs above the large bed along the northern wall.
A small section of wall within the painting is missing, however the damage does not look to be due to age or looting.
In the south west corner there are 3 fragments matching the design of the walls piled one on top of the other.
Their size and shapes match that of the damage within the painting but each has a unique design painted onto it.
Use “look tile1” to view the first and “take tile1” to take it.
Use “look tile2” to view the second and “take tile2” to take it.
Use “look tile3” to view the third and “take tile3” to take it.
The large door leading back to the main room is locked even from the inside, no keyhole is visible"""
,{"E": "SecretPassage", "N": "EndRoom"}, ["tile1", "tile2", "tile3"], ["N"])

Dungeon["EndRoom"] = Room("EndRoom", """You enter the secret room and are taken aback, this room unlike all the others, looks untouched for years.
Many grand painting line the walls and torches fill every corner with light.
In the centre of the room is a large Golden chest. Bursting open with more golden coins. You have what you came for. You bested every explorer who failed.
Congratulations!
The End"""
,{})

Dungeon["Outside"] = Room("Outside", """You step back into the cold outdoors.
The sun shines brightly on your face as you walk away from the ruined palace.
This challenge has bested you., but you are not the first to have given up..."""
,{})

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

#Processing Player Input Function
def ProcessInput(PlayerChoice):
    #Movement
    if PlayerChoice[0] == "go":
        if PlayerChoice[1] == "north":
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
                if "E" in Player.CurrentRoom.Locks:
                    print ("The passage is too dark. Find something to light your way")
                else:
                    print ("going east")
                    Player.CurrentRoom = Dungeon[Player.CurrentRoom.Connections["E"]]
            else:
                print ("You can not go that way")
        elif PlayerChoice[1] == "west":
            if "W" in Player.CurrentRoom.Connections:
                print ("going west")
                Player.CurrentRoom = Dungeon[Player.CurrentRoom.Connections["W"]]
            else:
                print ("You can not go that way")
        else:
            print ("That is not a valid direction")

    #Looking Commands
    elif PlayerChoice[0] == "look":
        if len(PlayerChoice) < 2:
            #prints room decription
            print (Player.CurrentRoom.Description)
        elif PlayerChoice[1] in Player.CurrentRoom.Items:
            #prints item description if item is in the room
            print (ItemDictionary[PlayerChoice[1]].Description)
        else:
            print ("That item is not in this room")

    #Take object
    elif PlayerChoice[0] == "take":
        if PlayerChoice[1] in Player.CurrentRoom.Items:
            #Remove item from room items and add to inventory
            Player.Inventory.append(PlayerChoice[1])
            Player.CurrentRoom.Items.remove(PlayerChoice[1])
            print (PlayerChoice[1] + " was added to your inventory")
        else:
            print("That item does not exist in this room")
    #Drop Item
    elif PlayerChoice[0] == "drop":
        if PlayerChoice[1] in Player.Inventory:
            #Reverse of taking item
            Player.Inventory.remove(PlayerChoice[1])
            Player.CurrentRoom.Items.append(PlayerChoice[1])
            print ("You dropped " + PlayerChoice[1])
        else:
            print ("You do not have that item")

    #Use Item
    elif PlayerChoice[0] == "use":
        if PlayerChoice[1] in Player.Inventory:
            if PlayerChoice[1] == "key":
                #Checks that player is in the correct room to use item
                if  Player.CurrentRoom == Dungeon["ThroneRoom"]:
                    #removes lock
                    Player.CurrentRoom.Locks = []
                    print("You turn the key in the door and it unlocks")
                else:
                    print ("A voice echoes through the room. This isn't the place for that")
            #Using Lamp
            if PlayerChoice[1] == "lamp":
                if Player.CurrentRoom == Dungeon["Kitchen"]:
                    #checks for lamp and matches
                    if "matches" in Player.Inventory:
                        print ("You use the match to light the lamp. You can now pass through the passage")
                        Player.CurrentRoom.Locks = []
                    else:
                        print ("You have nothing to light the lamp with")
                else:
                    print ("A voice echoes through the room. This isn't the place for that")
            #Using Matches (Same effect as using Lamp)
            if PlayerChoice[1] == "matches":
                if Player.CurrentRoom == Dungeon["Kitchen"]:
                    if "Lamp" in Player.Inventory:
                        print ("You use the match to light the lamp. You can now pass through the passage")
                        Player.CurrentRoom.Locks = []
                    else:
                        print ("You have nothing to light with the match")
                else:
                    print ("A voice echoes through the room. This isn't the place for that")
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

    #Checking for the two scripted ending Room
    if Player.CurrentRoom == Dungeon["Outside"]:
        print (Player.CurrentRoom.Description)
        #emds game
    elif Player.CurrentRoom == Dungeon["EndRoom"]:
        print (Player.CurrentRoom.Description)
        #ends game


#Running the Game
Running = True
print ("Intro Here")
while Running == True:
    #Take player input and split on space into a list
    PlayerChoice = input("What will you do? ")
    PlayerChoice = PlayerChoice.lower()
    PlayerChoice = PlayerChoice.split(" ")
    ProcessInput(PlayerChoice)
