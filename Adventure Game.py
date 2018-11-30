class Room (objects):
    def __init__ (self, Name, Description, Connections, Items = [], Locks= []):
        self.Name = Name
        self.Description = Description
        self.Connections = Connections
        self.Items = Items
        self.Locks = Locks

Dungeon = {}
Dungeon["MainRoom"] = Room("MainRoom", "Description here",{"W": "StorageRoom", "S": "Outside", "E": "ThroneRoom"})
Dungeon["StorageRoom"] = Room("StorageRoom", "Description here",{"E": "MainRoom"}, ["Small Key"])
Dungeon["ThroneRoom"] = Room("ThroneRoom", "Description here",{"W": "MainRoom", "N": "Kitchen"},["Oil Lamp"],["N"])
Dungeon["Kitchen"] = Room("Kitchen", "Description here",{"S": "ThroneRoom", "W": "SecretPassage"}, ["Matches"], ["W"])
Dungeon["SecretPassage"] = Room("SecretPassage", "Description here",{"W": "KingsChamber", "E": "Kitchen"})
Dungeon["KingsChamber"] = Room("KingsChamber", "Description here",{"E": "SecretPassage", "N": "EndRoom"}, ["FloorTile"], ["N"])
Dungeon["EndRoom"] = Room("EndRoom", "Description here")
Dungeon["Outside"] = Room("Outside", "Description here")
