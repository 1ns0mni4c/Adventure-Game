class Place:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.linked_caves = {}
    
    def link_cave(self, cave_to_link, direction):
        self.linked_caves[direction] = cave_to_link
    
    def move(self, direction):
        if direction in self.linked_caves:
            return self.linked_caves[direction]
        else:
            print("You can't go that way")
            return self
    
    def get_details(self):
        print(self.description)
        
        for direction in self.linked_caves:
            cave = self.linked_caves[direction]
            print( "The " + cave.name + " is " + direction)