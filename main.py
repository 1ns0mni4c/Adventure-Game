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

cavern.link_cave(mine, "north")
cavern.link_cave(grotto, "east")
cavern.link_cave(subway, "south")
cavern.link_cave(dungeon, "west")