from cave import Cave

cavern = Cave("Cavern")
cavern.set_description("A large, empty cave.")

mine = Cave("Mine")
mine.set_description("An old, abandoned mine.")

grotto = Cave("Grotto")
grotto.set_description("A small cave filled with water.")

subway = Cave("Subway")
subway.set_description("A pitch-black, abandoned subway.")

dungeon = Cave("Dungeon")
dungeon.set_description("An eerie complex of prison cells.")

factory = Cave("Factory")
factory.set_description("A decrepit factory filled with toxic waste.")

armoury = Cave("Armoury")
armoury.set_description("A dingy cell repurposed as a weapons storage facility.")

tunnel = Cave("Tunnel")
tunnel.set_description("An narrow tunnel that stretches for a long distance.")

hideout = Cave("Hideout")
hideout.set_description("A secret room full of amenities and resources.")

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