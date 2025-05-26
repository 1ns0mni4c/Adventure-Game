class Place:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.linked_caves = {}
    
    def link_cave(self, cave_to_link, direction):
        self.linked_caves[direction] = cave_to_link