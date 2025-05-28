from game import Place

cavern = Place("Cavern", "A large, empty cave.")

mine = Place("Mine", "An old, abandoned mine.")

grotto = Place("Grotto", "A small cave filled with water.")

subway = Place("Subway", "A pitch-black, abandoned subway.")

dungeon = Place("Dungeon", "An eerie complex of prison cells.")

factory = Place("Factory", "A decrepit factory filled with toxic waste.")

armoury = Place("Armoury", "A dingy cell repurposed as a weapons storage facility.")

tunnel = Place("Tunnel", "An narrow tunnel that stretches for a long distance.")

hideout = Place("Hideout", "A secret room full of amenities and resources.")

cavern.link_cave(mine, "north")
cavern.link_cave(grotto, "east")
cavern.link_cave(subway, "south")
cavern.link_cave(dungeon, "west")

subway.link_cave(cavern, "north")
subway.link_cave(factory, "south")
subway.link_cave(hideout, "west")

dungeon.link_cave(tunnel, "north")
dungeon.link_cave(cavern, "east")
dungeon.link_cave(hideout, "south")
dungeon.link_cave(armoury, "west")

tunnel.link_cave(mine, "east")
tunnel.link_cave(dungeon, "south")

hideout.link_cave(dungeon, "north")
hideout.link_cave(subway, "east")

armoury.link_cave(dungeon, "east")

current_cave = cavern          

while True:
    current_cave.get_details()         
    command = input("> ")    
    current_cave = current_cave.move(command)