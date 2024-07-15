from typing import Dict, NamedTuple, Optional, Set
import typing


from BaseClasses import Location


class KHBBSLocation(Location):
    game: str = "Kingdom Hearts Birth by Sleep"


class KHBBSLocationData(NamedTuple):
    category: str
    code: Optional[int] = None
    


def get_locations_by_category(category: str) -> Dict[str, KHBBSLocationData]:
    location_dict: Dict[str, KHBBSLocationData] = {}
    for name, data in location_table.items():
        if data.category == category:
            location_dict.setdefault(name, data)

    return location_dict

location_table: Dict[str, KHBBSLocationData] = {
    # Terra Chests
    "(T) Dwarf Woodlands Vault Balloon Letter Chest":                          KHBBSLocationData("Dwarf Woodlands",    227_1200025),
    "(T) Dwarf Woodlands Vault Ether Chest":                                   KHBBSLocationData("Dwarf Woodlands",    227_1200026),
    "(T) Dwarf Woodlands Vault Potion Chest":                                  KHBBSLocationData("Dwarf Woodlands",    227_1200027),
    "(T) Dwarf Woodlands Vault Flame Salvo Chest":                             KHBBSLocationData("Dwarf Woodlands",    227_1200028),
    "(T) Dwarf Woodlands Underground Waterway Potion Chest":                   KHBBSLocationData("Dwarf Woodlands",    227_1200031),
    "(T) Dwarf Woodlands Underground Waterway Block Recipe Chest":             KHBBSLocationData("Dwarf Woodlands",    227_1200032),
    "(T) Dwarf Woodlands Underground Waterway Poison Edge Chest":              KHBBSLocationData("Dwarf Woodlands",    227_1200033),
    "(T) Dwarf Woodlands Courtyard Fission Firaga Chest":                      KHBBSLocationData("Dwarf Woodlands",    227_1200034),
    "(T) Dwarf Woodlands Courtyard Potion Chest":                              KHBBSLocationData("Dwarf Woodlands",    227_1200035),
    "(T) Dwarf Woodlands Flower Glade Hungry Crystal Chest":                   KHBBSLocationData("Dwarf Woodlands",    227_1200036),
    "(T) Dwarf Woodlands Courtyard Map Chest":                                 KHBBSLocationData("Dwarf Woodlands",    227_1200037),
    "(T) Dwarf Woodlands Underground Waterway Fire Chest":                     KHBBSLocationData("Dwarf Woodlands",    227_1200038),
    "(T) Castle of Dreams Palace Courtyard Pulsing Crystal Chest":             KHBBSLocationData("Castle of Dreams",   227_1200051),
    "(T) Castle of Dreams Palace Courtyard Wellspring Crystal Chest":          KHBBSLocationData("Castle of Dreams",   227_1200052),
    "(T) Castle of Dreams Palace Courtyard Slow Chest":                        KHBBSLocationData("Castle of Dreams",   227_1200053),
    "(T) Castle of Dreams Ballroom Fleeting Crystal Chest":                    KHBBSLocationData("Castle of Dreams",   227_1200054),
    "(T) Castle of Dreams Foyer Strike Raid Chest":                            KHBBSLocationData("Castle of Dreams",   227_1200055),
    "(T) Castle of Dreams Foyer Potion Chest":                                 KHBBSLocationData("Castle of Dreams",   227_1200056),
    "(T) Castle of Dreams Foyer Hi-Potion Chest":                              KHBBSLocationData("Castle of Dreams",   227_1200057),
    "(T) Castle of Dreams Foyer Soothing Crystal Chest":                       KHBBSLocationData("Castle of Dreams",   227_1200058),
    "(T) Castle of Dreams Antechamber Thunder Chest":                          KHBBSLocationData("Castle of Dreams",   227_1200061),
    "(T) Castle of Dreams Palace Courtyard Map Chest":                         KHBBSLocationData("Castle of Dreams",   227_1200062),
    "(T) Castle of Dreams Chateau Thunderstorm Chest":                         KHBBSLocationData("Castle of Dreams",   227_1200063),
    "(T) Enchanted Dominion Waterside Potion Chest":                           KHBBSLocationData("Enchanted Dominion", 227_1200075),
    "(T) Enchanted Dominion Forest Clearing Blizzard Chest":                   KHBBSLocationData("Enchanted Dominion", 227_1200076),
    "(T) Enchanted Dominion Audience Chamber Zero Gravity Chest":              KHBBSLocationData("Enchanted Dominion", 227_1200077),
    "(T) Enchanted Dominion Audience Chamber Ether Chest":                     KHBBSLocationData("Enchanted Dominion", 227_1200078),
    "(T) Enchanted Dominion Audience Chamber Potion Chest":                    KHBBSLocationData("Enchanted Dominion", 227_1200081),
    "(T) Enchanted Dominion Hallway Ether Chest":                              KHBBSLocationData("Enchanted Dominion", 227_1200082),
    "(T) Enchanted Dominion Aurora's Chamber Map Chest":                       KHBBSLocationData("Enchanted Dominion", 227_1200083),
    "(T) Enchanted Dominion Tower Room Sleep Chest":                           KHBBSLocationData("Enchanted Dominion", 227_1200084),
    "(T) Enchanted Dominion Waterside Pulsing Crystal Chest":                  KHBBSLocationData("Enchanted Dominion", 227_1200085),
    "(T) Enchanted Dominion Tower Room Attack Recipe Chest":                   KHBBSLocationData("Enchanted Dominion", 227_1200086),
    "(T) Mysterious Tower Mysterious Tower Pulsing Crystal Chest":             KHBBSLocationData("Mysterious Tower",   227_1200101),
    "(T) Mysterious Tower Mysterious Tower Balloon Letter Chest":              KHBBSLocationData("Mysterious Tower",   227_1200102),
    "(T) Mysterious Tower Mysterious Tower Cure Chest":                        KHBBSLocationData("Mysterious Tower",   227_1200103),
    "(T) Mysterious Tower Tower Entrance Magic Recipe Chest":                  KHBBSLocationData("Mysterious Tower",   227_1200104),
    "(T) Radiant Garden Aqueduct Esuna Chest":                                 KHBBSLocationData("Radiant Garden",     227_1200125),
    "(T) Radiant Garden Aqueduct Blackout Chest":                              KHBBSLocationData("Radiant Garden",     227_1200126),
    "(T) Radiant Garden Aqueduct Hi-Potion Chest":                             KHBBSLocationData("Radiant Garden",     227_1200127),
    "(T) Radiant Garden Outer Gardens Fira Chest":                             KHBBSLocationData("Radiant Garden",     227_1200128),
    "(T) Radiant Garden Outer Gardens Pulsing Crystal Chest":                  KHBBSLocationData("Radiant Garden",     227_1200131),
    "(T) Radiant Garden Central Square Potion Chest":                          KHBBSLocationData("Radiant Garden",     227_1200132),
    "(T) Radiant Garden Central Square Hi-Potion Chest":                       KHBBSLocationData("Radiant Garden",     227_1200133),
    "(T) Radiant Garden Purification Facility Mega-Potion Chest":              KHBBSLocationData("Radiant Garden",     227_1200134),
    "(T) Radiant Garden Purification Facility Chaos Crystal Chest":            KHBBSLocationData("Radiant Garden",     227_1200135),
    "(T) Radiant Garden Castle Town Map Chest":                                KHBBSLocationData("Radiant Garden",     227_1200136),
    "(T) Radiant Garden Fountain Court Thunder Surge Chest":                   KHBBSLocationData("Radiant Garden",     227_1200137),
    "(T) Radiant Garden Fountain Court Fleeting Crystal Chest":                KHBBSLocationData("Radiant Garden",     227_1200138),
    "(T) Radiant Garden Fountain Court Panacea Chest":                         KHBBSLocationData("Radiant Garden",     227_1200141),
    "(T) Radiant Garden Merlin's House Shimmering Crystal Chest":              KHBBSLocationData("Radiant Garden",     227_1200142),
    "(T) Olympus Coliseum Coliseum Gates Fire Strike Chest":                   KHBBSLocationData("Olympus Coliseum",   227_1200151),
    "(T) Olympus Coliseum Coliseum Gates Mega Attack Recipe Chest":            KHBBSLocationData("Olympus Coliseum",   227_1200152),
    "(T) Olympus Coliseum Coliseum Gates Mega-Potion Recipe Chest":            KHBBSLocationData("Olympus Coliseum",   227_1200153),
    "(T) Olympus Coliseum Vestibule Map Chest":                                KHBBSLocationData("Olympus Coliseum",   227_1200154),
    "(T) Deep Space Turo Prison Block High Jump Chest":                        KHBBSLocationData("Deep Space",         227_1200175),
    "(T) Deep Space Durgon Transporter Hi-Potion Chest":                       KHBBSLocationData("Deep Space",         227_1200176),
    "(T) Deep Space Ship Corridor Ether Chest":                                KHBBSLocationData("Deep Space",         227_1200177),
    "(T) Deep Space Ship Corridor Hi-Potion Chest":                            KHBBSLocationData("Deep Space",         227_1200178),
    "(T) Deep Space Ship Corridor Pulsing Crystal Chest":                      KHBBSLocationData("Deep Space",         227_1200181),
    "(T) Deep Space Ship Corridor Warp Chest":                                 KHBBSLocationData("Deep Space",         227_1200182),
    "(T) Deep Space Control Room Hi-Potion Chest":                             KHBBSLocationData("Deep Space",         227_1200183),
    "(T) Deep Space Turo Prison Block Brutal Blast Chest":                     KHBBSLocationData("Deep Space",         227_1200184),
    "(T) Deep Space Turo Prison Block Pulsing Crystal Chest":                  KHBBSLocationData("Deep Space",         227_1200185),
    "(T) Deep Space Turo Prison Block Mega-Ether Chest":                       KHBBSLocationData("Deep Space",         227_1200186),
    "(T) Deep Space Ship Hub Hungry Crystal Chest":                            KHBBSLocationData("Deep Space",         227_1200187),
    "(T) Deep Space Machinery Bay Access Mine Square Chest":                   KHBBSLocationData("Deep Space",         227_1200188),
    "(T) Deep Space Turo Prison Block Mega-Potion Chest":                      KHBBSLocationData("Deep Space",         227_1200191),
    "(T) Deep Space Launch Deck Thundara Chest":                               KHBBSLocationData("Deep Space",         227_1200192),
    "(T) Deep Space Turo Transporter Map Chest":                               KHBBSLocationData("Deep Space",         227_1200193),
    "(T) Deep Space Launch Deck Abounding Crystal Chest":                      KHBBSLocationData("Deep Space",         227_1200195),
    "(T) Deep Space Launch Deck Wellspring Crystal Chest":                     KHBBSLocationData("Deep Space",         227_1200196),
    "(T) Deep Space Ship Hub Mega-Potion Chest":                               KHBBSLocationData("Deep Space",         227_1200197),
    "(T) Deep Space Ship Hub Fleeting Crystal Chest":                          KHBBSLocationData("Deep Space",         227_1200198),
    "(T) Neverland Gully Map Chest":                                           KHBBSLocationData("Neverland",          227_1200201),
    "(T) Neverland Gully Hi-Potion Chest":                                     KHBBSLocationData("Neverland",          227_1200202),
    "(T) Neverland Cove Ether Chest":                                          KHBBSLocationData("Neverland",          227_1200203),
    "(T) Neverland Cliff Path Hi-Potion Chest":                                KHBBSLocationData("Neverland",          227_1200204),
    "(T) Neverland Cliff Path Mega-Potion Chest":                              KHBBSLocationData("Neverland",          227_1200205),
    "(T) Neverland Cliff Path Firaga Chest":                                   KHBBSLocationData("Neverland",          227_1200206),
    "(T) Neverland Mermaid Lagoon Dark Haze Chest":                            KHBBSLocationData("Neverland",          227_1200207),
    "(T) Neverland Mermaid Lagoon Geo Impact Chest":                           KHBBSLocationData("Neverland",          227_1200208),
    "(T) Neverland Mermaid Lagoon Elixir Chest":                               KHBBSLocationData("Neverland",          227_1200211),
    "(T) Neverland Peter's Hideout Shimmering Crystal Chest":                  KHBBSLocationData("Neverland",          227_1200212),
    "(T) Neverland Peter's Hideout Mega Magic Recipe Chest":                   KHBBSLocationData("Neverland",          227_1200213),
    "(T) Neverland Jungle Clearing Hi-Potion Chest":                           KHBBSLocationData("Neverland",          227_1200214),
    "(T) Neverland Rainbow Falls: Crest Abounding Crystal Chest":              KHBBSLocationData("Neverland",          227_1200215),
    "(T) Neverland Skull Rock: Entrance Panacea Chest":                        KHBBSLocationData("Neverland",          227_1200216),
    "(T) Neverland Skull Rock: Cavern Megalixir Chest":                        KHBBSLocationData("Neverland",          227_1200217),
    "(T) Neverland Skull Rock: Cavern Ars Solum Chest":                        KHBBSLocationData("Neverland",          227_1200218),
    "(T) Neverland Skull Rock: Cavern Chaos Crystal Chest":                    KHBBSLocationData("Neverland",          227_1200221),
    "(T) Neverland Rainbow Falls: Base Megalixir Chest":                       KHBBSLocationData("Neverland",          227_1200222),
    "(T) Neverland Rainbow Falls: Base Zero Graviga Chest":                    KHBBSLocationData("Neverland",          227_1200223),
    "(T) Neverland Cove Hi-Potion Chest":                                      KHBBSLocationData("Neverland",          227_1200224),
    "(T) Disney Town Main Plaza Map Chest":                                    KHBBSLocationData("Disney Town",        227_1200225),
    "(T) Disney Town Main Plaza Potion Chest":                                 KHBBSLocationData("Disney Town",        227_1200226),
    "(T) Disney Town Raceway Abounding Crystal Chest":                         KHBBSLocationData("Disney Town",        227_1200227),
    "(T) Disney Town Raceway Payback Fang Chest":                              KHBBSLocationData("Disney Town",        227_1200228),
    "(T) Disney Town Raceway Slot Edge Chest":                                 KHBBSLocationData("Disney Town",        227_1200231),
    "(T) Disney Town Gizmo Gallery Panacea Chest":                             KHBBSLocationData("Disney Town",        227_1200234),
    "(T) Disney Town Gizmo Gallery Action Recipe Chest":                       KHBBSLocationData("Disney Town",        227_1200235),
    "(T) Disney Town Gizmo Gallery Chaos Crystal Chest":                       KHBBSLocationData("Disney Town",        227_1200236),
    "(T) Disney Town Gizmo Gallery Thunder Chest 1":                           KHBBSLocationData("Disney Town",        227_1200237),
    "(T) Disney Town Gizmo Gallery Thunder Chest 2":                           KHBBSLocationData("Disney Town",        227_1200238),
    "(T) Disney Town Pete's Rec Room Zero Graviga Chest":                      KHBBSLocationData("Disney Town",        227_1200241),
    "(T) Disney Town Pete's Rec Room Aerial Slam Chest":                       KHBBSLocationData("Disney Town",        227_1200242),
    "(T) Disney Town Gizmo Gallery Absolute Zero Chest":                       KHBBSLocationData("Disney Town",        227_1200243),
    "(T) Disney Town Pete's Rec Room Break Time Chest":                        KHBBSLocationData("Disney Town",        227_1200244),
    "(T) Disney Town Pete's Rec Room Chaos Crystal Chest":                     KHBBSLocationData("Disney Town",        227_1200245),
    "(T) Disney Town Gizmo Gallery Mega-Potion Chest":                         KHBBSLocationData("Disney Town",        227_1200246),
    "(T) Keyblade Graveyard Twister Trench Windcutter Chest":                  KHBBSLocationData("Keyblade Graveyard", 227_1200251),
    "(T) Keyblade Graveyard Twister Trench Mega-Potion Chest":                 KHBBSLocationData("Keyblade Graveyard", 227_1200252),
    "(T) Keyblade Graveyard Twister Trench Mega-Ether Chest":                  KHBBSLocationData("Keyblade Graveyard", 227_1200253),
    "(T) Keyblade Graveyard Twister Trench Megalixir Chest":                   KHBBSLocationData("Keyblade Graveyard", 227_1200254),
    "(T) Keyblade Graveyard Seat of War Elixir Chest":                         KHBBSLocationData("Keyblade Graveyard", 227_1200255),
    "(T) Keyblade Graveyard Seat of War Mega-Potion Chest":                    KHBBSLocationData("Keyblade Graveyard", 227_1200256),
    "(T) Keyblade Graveyard Seat of War Map Chest":                            KHBBSLocationData("Keyblade Graveyard", 227_1200257),

    # Terra Stickers
    "(T) Enchanted Dominion Forest Clearing Balloon Sticker":                  KHBBSLocationData("Enchanted Dominion", 227_1210002),
    "(T) Enchanted Dominion Audience Chamber Huey Sticker":                    KHBBSLocationData("Enchanted Dominion", 227_1210003),
    "(T) Enchanted Dominion Tower Room Flying Balloon Sticker":                KHBBSLocationData("Enchanted Dominion", 227_1210004),
    "(T) Castle of Dreams Chateau Traffic Cone Sticker":                       KHBBSLocationData("Castle of Dreams",   227_1210005),
    "(T) Castle of Dreams Passage Flying Balloon Sticker":                     KHBBSLocationData("Castle of Dreams",   227_1210006),
    "(T) Dwarf Woodlands Underground Waterway Louie Sticker":                  KHBBSLocationData("Dwarf Woodlands",    227_1210007),
    "(T) Dwarf Woodlands Flower Glade Balloon Sticker":                        KHBBSLocationData("Dwarf Woodlands",    227_1210008),
    "(T) Mysterious Tower Sorcerer's Chamber Balloon Sticker":                 KHBBSLocationData("Mysterious Tower",   227_1210011),
    "(T) Radiant Garden Outer Gardens Airplane Sticker":                       KHBBSLocationData("Radiant Garden",     227_1210012),
    "(T) Radiant Garden Central Square Flying Balloon Sticker":                KHBBSLocationData("Radiant Garden",     227_1210013),
    "(T) Radiant Fountain Court Dale Sticker":                                 KHBBSLocationData("Radiant Garden",     227_1210014),
    "(T) Olympus Coliseum Coliseum Gates Balloon Sticker":                     KHBBSLocationData("Olympus Coliseum",   227_1210015),
    "(T) Deep Space Turo Prison Block Flying Balloon Sticker":                 KHBBSLocationData("Deep Space",         227_1210016),
    "(T) Deep Space Ship Corridor UFO Sticker":                                KHBBSLocationData("Deep Space",         227_1210017),
    "(T) Neverland Peter's Hideout Dewey Sticker":                             KHBBSLocationData("Neverland",          227_1210018),
    "(T) Neverland Rainbow Falls: Base Rainbow Sticker":                       KHBBSLocationData("Neverland",          227_1210021),
    "(T) Neverland Skull Rock: Entrance Chip Sticker":                         KHBBSLocationData("Neverland",          227_1210022),
    "(T) Disney Town Gizmo Gallery Pete Sticker":                              KHBBSLocationData("Disney Town",        227_1210023),
    "(T) Disney Town Raceway Traffic Cone Sticker":                            KHBBSLocationData("Disney Town",        227_1210024),
    "(T) Keyblade Graveyard Twister Trench Traffic Cone Sticker":              KHBBSLocationData("Keyblade Graveyard", 227_1210025),
    
    # Terra Story Rewards
    "(T) Land of Departure Orbs Defeated Max HP Increase":                     KHBBSLocationData("Land of Departure",  227_1220000),
    "(T) Land of Departure Orbs Defeated Ventus D-Link":                       KHBBSLocationData("Land of Departure",  227_1220001),
    "(T) Land of Departure Orbs Defeated Aqua D-Link":                         KHBBSLocationData("Land of Departure",  227_1220002),
    "(T) Land of Departure Eraqus Defeated Max HP Increase":                   KHBBSLocationData("Land of Departure",  227_1220003),
    "(T) Land of Departure Eraqus Defeated Chaos Ripper":                      KHBBSLocationData("Land of Departure",  227_1220004),
    "(T) Land of Departure Eraqus Defeated Xehanort's Report 8":               KHBBSLocationData("Land of Departure",  227_1220005),
    "(T) Dwarf Woodlands Unversed Group Defeated Air Slide":                   KHBBSLocationData("Dwarf Woodlands",    227_1220100),
    "(T) Dwarf Woodlands Spirit of the Magic Mirror Defeated Air Slide":       KHBBSLocationData("Dwarf Woodlands",    227_1220101),
    "(T) Dwarf Woodlands Spirit of the Magic Mirror Defeated Max HP Increase": KHBBSLocationData("Dwarf Woodlands",    227_1220102),
    "(T) Dwarf Woodlands Spirit of the Magic Mirror Defeated Firestorm":       KHBBSLocationData("Dwarf Woodlands",    227_1220103),
    "(T) Dwarf Woodlands Spirit of the Magic Mirror Defeated Treasure Trove":  KHBBSLocationData("Dwarf Woodlands",    227_1220104),
    "(T) Castle of Dreams Cinderella Escorted Counter Hammer":                 KHBBSLocationData("Castle of Dreams",   227_1220200),
    "(T) Castle of Dreams Symphony Master Defeated Max HP Increase":           KHBBSLocationData("Castle of Dreams",   227_1220201),
    "(T) Castle of Dreams Symphony Master Defeated Deck Capacity Increase":    KHBBSLocationData("Castle of Dreams",   227_1220202),
    "(T) Castle of Dreams Symphony Master Defeated Cinderella D-Link":         KHBBSLocationData("Castle of Dreams",   227_1220203),
    "(T) Castle of Dreams Symphony Master Defeated Stroke of Midnight":        KHBBSLocationData("Castle of Dreams",   227_1220204),
    "(T) Castle of Dreams Symphony Master Defeated Royal Board":               KHBBSLocationData("Castle of Dreams",   227_1220205),
    "(T) Enchanted Dominion Unlock Aurora's Heart Maleficent D-Link":          KHBBSLocationData("Enchanted Dominion", 227_1220300),
    "(T) Enchanted Dominion Wheel Master Defeated Deck Capacity Increase":     KHBBSLocationData("Enchanted Dominion", 227_1220301),
    "(T) Enchanted Dominion Wheel Master Defeated Diamond Dust":               KHBBSLocationData("Enchanted Dominion", 227_1220302),
    "(T) Enchanted Dominion Wheel Master Defeated Fairy Stars":                KHBBSLocationData("Enchanted Dominion", 227_1220303),
    "(T) Radiant Garden Examine Pooh's Story Book Honey Pot Board":            KHBBSLocationData("Radiant Garden",     227_1220500),
    "(T) Radiant Garden Defeat Trinity Armor Max HP Increase":                 KHBBSLocationData("Radiant Garden",     227_1220501),
    "(T) Radiant Garden Defeat Trinity Armor Rockbreaker":                     KHBBSLocationData("Radiant Garden",     227_1220502),
    "(T) Radiant Garden Defeat Trinity Armor Disney Town Pass":                KHBBSLocationData("Radiant Garden",     227_1220503),
    "(T) Radiant Garden Defeat Braig Deck Capacity Increase":                  KHBBSLocationData("Radiant Garden",     227_1220504),
    "(T) Radiant Garden Defeat Braig Dark Volley":                             KHBBSLocationData("Radiant Garden",     227_1220505),
    "(T) Radiant Garden Defeat Braig Xehanort's Report 2":                     KHBBSLocationData("Radiant Garden",     227_1220506),
    "(T) Olympus Coliseum Tournament Complete Max HP Increase":                KHBBSLocationData("Olympus Coliseum",   227_1220600),
    "(T) Olympus Coliseum Tournament Complete Sonic Impact":                   KHBBSLocationData("Olympus Coliseum",   227_1220601),
    "(T) Olympus Coliseum Defeat Zack Deck Capacity Increase":                 KHBBSLocationData("Olympus Coliseum",   227_1220602),
    "(T) Olympus Coliseum Defeat Zack Zack D-Link":                            KHBBSLocationData("Olympus Coliseum",   227_1220603),
    "(T) Olympus Coliseum Defeat Zack Mark of a Hero":                         KHBBSLocationData("Olympus Coliseum",   227_1220604),
    "(T) Deep Space Defeat Unversed in Space Max HP Increase":                 KHBBSLocationData("Deep Space",         227_1220700),
    "(T) Deep Space Defeat Experiment 221 Thunderbolt":                        KHBBSLocationData("Deep Space",         227_1220701),
    "(T) Deep Space Defeat Experiment 221 Experiment 626 D-Link":              KHBBSLocationData("Deep Space",         227_1220702),
    "(T) Deep Space Defeat Experiment 221 Hyperdrive":                         KHBBSLocationData("Deep Space",         227_1220703),
    "(T) Deep Space Defeat Experiment 221 Spaceship Board":                    KHBBSLocationData("Deep Space",         227_1220704),
    "(T) Destiny Islands Scene Ends of the Earth":                             KHBBSLocationData("Destiny Islands",    227_1220800),
    "(T) Neverland Defeat Peter Pan Bladecharge":                              KHBBSLocationData("Neverland",          227_1220900),
    "(T) Neverland Defeat Peter Pan Peter Pan D-Link":                         KHBBSLocationData("Neverland",          227_1220901),
    "(T) Neverland Defeat Countless Unversed Deck Capacity Increase":          KHBBSLocationData("Neverland",          227_1220902),
    "(T) Neverland Defeat Countless Unversed Pixie Petal":                     KHBBSLocationData("Neverland",          227_1220903),
    "(T) Neverland Defeat Countless Unversed Skull Board":                     KHBBSLocationData("Neverland",          227_1220904),
    "(T) Disney Town Complete Rumble Racing Hi-Potion":                        KHBBSLocationData("Disney Town",        227_1221000),
    "(T) Disney Town Complete Rumble Racing Toon Board":                       KHBBSLocationData("Disney Town",        227_1221001),
    "(T) Keyblade Graveyard Meet With Xehanort Dark Impulse":                  KHBBSLocationData("Keyblade Graveyard", 227_1221100),
    "(T) Keyblade Graveyard Xehanort Defeated Max HP Increase":                KHBBSLocationData("Keyblade Graveyard", 227_1221101),
    "(T) Keyblade Graveyard Defeat Terranort":                                 KHBBSLocationData("Keyblade Graveyard", 227_1221102),
}

event_location_table: Dict[str, KHBBSLocationData] = {}
lookup_id_to_name: typing.Dict[int, str] = {data.code: item_name for item_name, data in location_table.items() if data.code}

location_name_groups: Dict[str, Set[str]]

# Make location categories
location_name_groups: Dict[str, Set[str]] = {}
for location in location_table.keys():
    category = location_table[location].category
    if category not in location_name_groups.keys():
        location_name_groups[category] = set([])
    location_name_groups[category].add(location)