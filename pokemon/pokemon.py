def starter_pokemon() -> dict:
    starter_dict = {
        "bulbasaur": {'Evolution-One': 'Bulbasaur', 'Evolution-Two': 'Ivysaur', 'Evolution-Three': 'Venusaur',
                      'Class': 'Forest', 'Current HP': 100, 'Move-One': 'Tackle', 'Move-Two': 'Vine Whip',
                      'Move-Three': '',
                      'Move-Four': ''},

        "ivysaur": {'Evolution-One': 'Bulbasaur', 'Evolution-Two': 'Ivysaur', 'Evolution-Three': 'Venusaur',
                    'Class': 'Forest', 'Current HP': 150, 'Move-One': 'Tackle', 'Move-Two': 'Vine Whip',
                    'Move-Three': 'Earthquake',
                    'Move-Four': ''},

        "venusaur": {'Evolution-One': 'Bulbasaur', 'Evolution-Two': 'Ivysaur', 'Evolution-Three': 'Venusaur',
                     'Class': 'Forest', 'Current HP': 200, 'Move-One': 'Tackle', 'Move-Two': 'Vine Whip',
                     'Move-Three': 'Earthquake',
                     'Move-Four': 'Hyper Beam'},

        "charmander": {'Evolution-One': 'Charmander', 'Evolution-Two': 'Charmeleon', 'Evolution-Three': 'Charizard',
                       'Class': 'Plain', 'Current HP': 100, 'Move-One': 'Scratch', 'Move-Two': 'Ember',
                       'Move-Three': '',
                       'Move-Four': ''},
        "charmeleon": {'Evolution-One': 'Charmander', 'Evolution-Two': 'Charmeleon', 'Evolution-Three': 'Charizard',
                       'Class': 'Plain', 'Current HP': 100, 'Move-One': 'Scratch', 'Move-Two': 'Ember',
                       'Move-Three': 'Earthquake',
                       'Move-Four': ''},
        "charizard": {'Evolution-One': 'Charmander', 'Evolution-Two': 'Charmeleon', 'Evolution-Three': 'Charizard',
                      'Class': 'Plain', 'Current HP': 100, 'Move-One': 'Scratch', 'Move-Two': 'Ember',
                      'Move-Three': 'Earthquake',
                      'Move-Four': 'Hyper Beam'},

        "squirtle": {'Evolution-One': 'Squirtle', 'Evolution-Two': 'Wartortle', 'Evolution-Three': 'Blastoise',
                     'Class': 'Water', 'Current HP': 100, 'Move-One': 'Tackle', 'Move-Two': 'Water Gun',
                     'Move-Three': '',
                     'Move-Four': ''},

        "wartortle": {'Evolution-One': 'Squirtle', 'Evolution-Two': 'Wartortle', 'Evolution-Three': 'Blastoise',
                      'Class': 'Water', 'Current HP': 100, 'Move-One': 'Tackle', 'Move-Two': 'Water Gun',
                      'Move-Three': 'Earthquake',
                      'Move-Four': ''},

        "blastoise": {'Evolution-One': 'Squirtle', 'Evolution-Two': 'Wartortle', 'Evolution-Three': 'Blastoise',
                      'Class': 'Water', 'Current HP': 100, 'Move-One': 'Tackle', 'Move-Two': 'Water Gun',
                      'Move-Three': 'Earthquake',
                      'Move-Four': 'Hyper Beam'}}
    return starter_dict


def forest_pokemon() -> dict:
    forest_dict = {
        "caterpie": {'Evolution-One': 'Caterpie', 'Evolution-Two': 'Metapod', 'Evolution-Three': 'Butterfree',
                     'Class': 'Forest', 'Current HP': 30, 'Move-One': 'Tackle', 'Move-Two': '', 'Move-Three': '',
                     'Move-Four': ''},

        "weedle": {'Evolution-One': 'Weedle', 'Evolution-Two': 'Kakuna', 'Evolution-Three': 'Beedrill',
                   'Class': 'Forest',
                   'Current HP': 50, 'Move-One': 'Poison Sting', 'Move-Two': '', 'Move-Three': '', 'Move-Four': ''},

        "beedrill": {'Evolution-One': 'Weedle', 'Evolution-Two': 'Kakuna', 'Evolution-Three': 'Beedrill',
                     'Class': 'Forest',
                     'Current HP': 100, 'Move-One': 'Poison Sting', 'Move-Two': 'Agility', 'Move-Three': 'Fury Attack',
                     'Move-Four': ''},

        "pidgey": {'Evolution-One': 'Pidgey', 'Evolution-Two': 'Pidgeotto', 'Evolution-Three': 'Pidgeot',
                   'Class': 'Forest',
                   'Current HP': 30, 'Move-One': 'Tackle', 'Move-Two': 'Gust', 'Move-Three': '', 'Move-Four': ''},

        "pidgeotto": {'Evolution-One': 'Pidgey', 'Evolution-Two': 'Pidgeotto', 'Evolution-Three': 'Pidgeot',
                      'Class': 'Forest', 'Current HP': 50, 'Move-One': 'Gust', 'Move-Two': 'Quick Attack',
                      'Move-Three': 'Sand Attack', 'Move-Four': ''},

        "pidgeot": {'Evolution-One': 'Pidgey', 'Evolution-Two': 'Pidgeotto', 'Evolution-Three': 'Pidgeot',
                    'Class': 'Forest',
                    'Current HP': 100, 'Move-One': 'Wing Attack', 'Move-Two': 'Sky Attack',
                    'Move-Three': 'Feather Dance',
                    'Move-Four': 'Agility'},

        "rattata": {'Evolution-One': 'Rattata', 'Evolution-Two': 'Raticate', 'Evolution-Three': '', 'Class': 'Forest',
                    'Current HP': 50, 'Move-One': 'Tackle', 'Move-Two': '', 'Move-Three': '', 'Move-Four': ''},

        "raticate": {'Evolution-One': 'Rattata', 'Evolution-Two': 'Raticate', 'Evolution-Three': '', 'Class': 'Forest',
                     'Current HP': 100, 'Move-One': 'Hyper Fang', 'Move-Two': 'Super Fang', 'Move-Three': 'Giant Bite',
                     'Move-Four': ''},

        "ekans": {'Evolution-One': 'Ekans', 'Evolution-Two': 'Arbok', 'Evolution-Three': '', 'Class': 'Forest',
                  'Current HP': 30, 'Move-One': 'Wrap', 'Move-Two': 'Poison Sting', 'Move-Three': '', 'Move-Four': ''},

        "arbok": {'Evolution-One': 'Ekans', 'Evolution-Two': 'Arbok', 'Evolution-Three': '', 'Class': 'Forest',
                  'Current HP': 80, 'Move-One': 'Wrap', 'Move-Two': 'Poison Sting', 'Move-Three': 'Acid Shot',
                  'Move-Four':
                      ''},

        "pikachu": {'Evolution-One': 'Pichu', 'Evolution-Two': 'Pikachu', 'Evolution-Three': 'Raichu',
                    'Class': 'Forest',
                    'Current HP': 50, 'Move-One': 'Quick Attack', 'Move-Two': 'Thunderbolt', 'Move-Three': 'Iron Tail',
                    'Move-Four': ''},

        "raichu": {'Evolution-One': 'Pichu', 'Evolution-Two': 'Pikachu', 'Evolution-Three': 'Raichu', 'Class': 'Forest',
                   'Current HP': 100, 'Move-One': 'Quick Attack', 'Move-Two': 'Thunderbolt', 'Move-Three': 'Iron Tail',
                   'Move-Four': 'Focus Punch'},

        "nidoranf": {'Evolution-One': 'Nidoran♀', 'Evolution-Two': 'Nidorina', 'Evolution-Three': 'Nidoqueen',
                     'Class': 'Forest', 'Current HP': 30, 'Move-One': 'Scratch', 'Move-Two': 'Double Kick',
                     'Move-Three': '', 'Move-Four': ''},

        "nidorina": {'Evolution-One': 'Nidoran♀', 'Evolution-Two': 'Nidorina', 'Evolution-Three': 'Nidoqueen',
                     'Class': 'Forest', 'Current HP': 50, 'Move-One': 'Scratch', 'Move-Two': 'Double Kick',
                     'Move-Three': 'Poison Sting', 'Move-Four': ''},

        "nidoqueen": {'Evolution-One': 'Nidoran♀', 'Evolution-Two': 'Nidorina', 'Evolution-Three': 'Nidoqueen',
                      'Class': 'Forest', 'Current HP': 100, 'Move-One': 'Scratch', 'Move-Two': 'Double Kick',
                      'Move-Three': 'Poison Sting', 'Move-Four': 'Body Slam'},

        "nidoranm": {'Evolution-One': 'Nidoran♂', 'Evolution-Two': 'Nidorino', 'Evolution-Three': 'Nidoking',
                     'Class': 'Forest', 'Current HP': 30, 'Move-One': 'Peck', 'Move-Two': 'Double Kick',
                     'Move-Three': '',
                     'Move-Four': ''},

        "nidorino": {'Evolution-One': 'Nidoran♂', 'Evolution-Two': 'Nidorino', 'Evolution-Three': 'Nidoking',
                     'Class': 'Forest', 'Current HP': 50, 'Move-One': 'Peck', 'Move-Two': 'Double Kick',
                     'Move-Three': 'Poison Sting', 'Move-Four': ''},
        "nidoking": {'Evolution-One': 'Nidoran♂', 'Evolution-Two': 'Nidorino', 'Evolution-Three': 'Nidoking',
                     'Class': 'Forest', 'Current HP': 100, 'Move-One': 'Peck', 'Move-Two': 'Double Kick',
                     'Move-Three': 'Poison Sting', 'Move-Four': 'Thrash'},
        "paras": {'Evolution-One': 'Paras', 'Evolution-Two': 'Parasect', 'Evolution-Three': '', 'Class': 'Forest',
                  'Current HP': 30, 'Move-One': 'Scratch', 'Move-Two': 'Stun Spore', 'Move-Three': '', 'Move-Four': ''},

        "parasect": {'Evolution-One': 'Paras', 'Evolution-Two': 'Parasect', 'Evolution-Three': '', 'Class': 'Forest',
                     'Current HP': 50, 'Move-One': 'Scratch', 'Move-Two': 'Stun Spore', 'Move-Three': 'Spore',
                     'Move-Four': ''},

        "venonat": {'Evolution-One': 'Venonat', 'Evolution-Two': 'Venomoth', 'Evolution-Three': '', 'Class': 'Mine',
                    'Current HP': 30, 'Move-One': 'Tackle', 'Move-Two': 'Disable', 'Move-Three': '', 'Move-Four': ''},

        "venomoth": {'Evolution-One': 'Venonat', 'Evolution-Two': 'Venomoth', 'Evolution-Three': '', 'Class': 'Mine',
                     'Current HP': 60, 'Move-One': 'Tackle', 'Move-Two': 'Disable', 'Move-Three': 'Poison Powder',
                     'Move-Four': ''},

        "diglett": {'Evolution-One': 'Diglett', 'Evolution-Two': 'Dugtrio', 'Evolution-Three': '', 'Class': 'Mine',
                    'Current HP': 40, 'Move-One': 'Scratch', 'Move-Two': 'Growl', 'Move-Three': '', 'Move-Four': ''},

        "dugtrio": {'Evolution-One': 'Diglett', 'Evolution-Two': 'Dugtrio', 'Evolution-Three': '', 'Class': 'Mine',
                    'Current HP': 80, 'Move-One': 'Scratch', 'Move-Two': 'Growl', 'Move-Three': 'Dig', 'Move-Four': ''},

        "arceus": {'Evolution-One': 'Arceus',
                   'Class': 'Legendary',
                   'Current HP': 400,
                   'Move-One': 'Judgment',
                   'Move-Two': 'Recover',
                   'Move-Three': 'Hyper Beam',
                   'Move-Four': 'Earthquake'}}
    return forest_dict


def mine_pokemon():
    pokemon = {
        "zubat": {'Evolution-One': 'Zubat', 'Evolution-Two': 'Golbat', 'Evolution-Three': '', 'Class': 'Mine',
                  'Current HP': 40, 'Move-One': 'Leech Life', 'Move-Two': 'Supersonic', 'Move-Three': '',
                  'Move-Four': ''},

        "golbat": {'Evolution-One': 'Zubat', 'Evolution-Two': 'Golbat', 'Evolution-Three': '', 'Class': 'Mine',
                   'Current HP': 80, 'Move-One': 'Leech Life', 'Move-Two': 'Supersonic', 'Move-Three': 'Wing Attack',
                   'Move-Four': ''},
        "onix": {'Evolution-One': 'Onix', 'Evolution-Two': 'Steelix', 'Evolution-Three': '', 'Class': 'Cave',
                 'Current HP': 60, 'Move-One': 'Rock Throw', 'Move-Two': 'Tackle', 'Move-Three': '', 'Move-Four': ''},

        "steelix": {'Evolution-One': 'Onix', 'Evolution-Two': 'Steelix', 'Evolution-Three': '', 'Class': 'Cave',
                    'Current HP': 100, 'Move-One': 'Iron Tail', 'Move-Two': 'Earthquake', 'Move-Three': 'Crunch',
                    'Move-Four': 'Dragon Breath'},

        "gastly": {'Evolution-One': 'Gastly', 'Evolution-Two': 'Haunter', 'Evolution-Three': 'Gengar',
                   'Class': 'Ghost',
                   'Current HP': 30, 'Move-One': 'Lick', 'Move-Two': 'Hypnosis', 'Move-Three': 'Dream Eater',
                   'Move-Four': ''},

        "haunter": {'Evolution-One': 'Gastly', 'Evolution-Two': 'Haunter', 'Evolution-Three': 'Gengar',
                    'Class': 'Ghost',
                    'Current HP': 50, 'Move-One': 'Lick', 'Move-Two': 'Hypnosis', 'Move-Three': 'Dream Eater',
                    'Move-Four': ''},

        "gengar": {'Evolution-One': 'Gastly', 'Evolution-Two': 'Haunter', 'Evolution-Three': 'Gengar',
                   'Class': 'Ghost',
                   'Current HP': 80, 'Move-One': 'Lick', 'Move-Two': 'Hypnosis', 'Move-Three': 'Dream Eater',
                   'Move-Four': ''},

        "abra": {'Evolution-One': 'Abra', 'Evolution-Two': 'Kadabra', 'Evolution-Three': 'Alakazam',
                 'Class': 'Psychic',
                 'Current HP': 30, 'Move-One': 'Teleport', 'Move-Two': 'Psybeam', 'Move-Three': 'Recover',
                 'Move-Four': ''},

        "kadabra": {'Evolution-One': 'Abra', 'Evolution-Two': 'Kadabra', 'Evolution-Three': 'Alakazam',
                    'Class': 'Psychic',
                    'Current HP': 50, 'Move-One': 'Teleport', 'Move-Two': 'Psybeam', 'Move-Three': 'Recover',
                    'Move-Four': ''},

        "alakazam": {'Evolution-One': 'Abra', 'Evolution-Two': 'Kadabra', 'Evolution-Three': 'Alakazam',
                     'Class': 'Psychic',
                     'Current HP': 30, 'Move-One': 'Teleport', 'Move-Two': 'Psybeam', 'Move-Three': 'Recover',
                     'Move-Four': ''},

        "giratina": {'Evolution-One': 'Giratina',
                     'Evolution-Two': '',
                     'Evolution-Three': '',
                     'Class': 'Legendary',
                     'Current HP': 200,
                     'Move-One': 'Dragon Claw',
                     'Move-Two': 'Shadow Force',
                     'Move-Three': 'Aura Sphere',
                     'Move-Four': 'Hyper Beam'}
    }
    return pokemon


def ocean_pokemon():
    pokemon = {
        "magikarp": {'Evolution-One': 'Magikarp', 'Evolution-Two': 'Gyarados', 'Evolution-Three': '', 'Class': 'Water',
                     'Current HP': 50, 'Move-One': 'Splash', 'Move-Two': '', 'Move-Three': '', 'Move-Four': ''},

        "gyarados": {'Evolution-One': 'Magikarp', 'Evolution-Two': 'Gyarados', 'Evolution-Three': '', 'Class': 'Water',
                     'Current HP': 150, 'Move-One': 'Bite', 'Move-Two': 'Dragon Rage', 'Move-Three': 'Hydro Pump',
                     'Move-Four': ''},
        "dratini": {'Evolution-One': 'Dratini', 'Evolution-Two': 'Dragonair', 'Evolution-Three': 'Dragonite',
                    'Class': 'Dragon', 'Current HP': 50, 'Move-One': 'Dragon Breath', 'Move-Two': 'Agility',
                    'Move-Three': '',
                    'Move-Four': ''},

        "dragonair": {'Evolution-One': 'Dratini', 'Evolution-Two': 'Dragonair', 'Evolution-Three': 'Dragonite',
                      'Class': 'Dragon', 'Current HP': 80, 'Move-One': 'Dragon Breath', 'Move-Two': 'Thunder Wave',
                      'Move-Three': 'Aqua Tail', 'Move-Four': 'Ice Beam'},

        "totodile": {'Evolution-One': 'Totodile', 'Evolution-Two': 'Croconaw', 'Evolution-Three': 'Feraligatr',
                     'Class': 'Water',
                     'Current HP': 40, 'Move-One': 'Scratch', 'Move-Two': 'Water Gun', 'Move-Three': '',
                     'Move-Four': ''},

        "croconaw": {'Evolution-One': 'Totodile', 'Evolution-Two': 'Croconaw', 'Evolution-Three': 'Feraligatr',
                     'Class': 'Water',
                     'Current HP': 60, 'Move-One': 'Bite', 'Move-Two': 'Aqua Tail', 'Move-Three': '', 'Move-Four': ''},

        "feraligatr": {'Evolution-One': 'Totodile', 'Evolution-Two': 'Croconaw', 'Evolution-Three': 'Feraligatr',
                       'Class': 'Water',
                       'Current HP': 80, 'Move-One': 'Ice Fang', 'Move-Two': 'Waterfall', 'Move-Three': 'Crunch',
                       'Move-Four': 'Superpower'},

        "mudkip": {'Evolution-One': 'Mudkip', 'Evolution-Two': 'Marshtomp', 'Evolution-Three': 'Swampert',
                   'Class': 'Water',
                   'Current HP': 30, 'Move-One': 'Tackle', 'Move-Two': 'Water Gun', 'Move-Three': '', 'Move-Four': ''},

        "marshtomp": {'Evolution-One': 'Mudkip', 'Evolution-Two': 'Marshtomp', 'Evolution-Three': 'Swampert',
                      'Class': 'Water',
                      'Current HP': 50, 'Move-One': 'Mud Shot', 'Move-Two': 'Water Gun', 'Move-Three': 'Mud Bomb',
                      'Move-Four': ''},

        "swampert": {'Evolution-One': 'Mudkip', 'Evolution-Two': 'Marshtomp', 'Evolution-Three': 'Swampert',
                     'Class': 'Water',
                     'Current HP': 80, 'Move-One': 'Hydro Pump', 'Move-Two': 'Earthquake', 'Move-Three': 'Ice Punch',
                     'Move-Four': 'Rock Slide'},

        "seadra": {'Evolution-One': 'Horsea', 'Evolution-Two': 'Seadra', 'Evolution-Three': 'Kingdra',
                   'Class': 'Water',
                   'Current HP': 50, 'Move-One': 'Water Gun', 'Move-Two': 'Agility', 'Move-Three': 'SmokeScreen',
                   'Move-Four': 'Waterfall'},

        "kingdra": {'Evolution-One': 'Horsea', 'Evolution-Two': 'Seadra', 'Evolution-Three': 'Kingdra',
                    'Class': 'Water',
                    'Current HP': 80, 'Move-One': 'Water Gun', 'Move-Two': 'Agility', 'Move-Three': 'SmokeScreen',
                    'Move-Four': 'Waterfall'},

        "horsea": {'Evolution-One': 'Horsea', 'Evolution-Two': 'Seadra', 'Evolution-Three': 'Kingdra',
                   'Class': 'Water',
                   'Current HP': 50, 'Move-One': 'Water Gun', 'Move-Two': 'Agility', 'Move-Three': 'SmokeScreen',
                   'Move-Four': 'Ice-Beam'},

        "psyduck": {'Evolution-One': 'Psyduck', 'Evolution-Two': 'Golduck', 'Evolution-Three': '', 'Class': 'Ocean',
                    'Current HP': 50, 'Move-One': 'Scratch', 'Move-Two': 'Tail Whip', 'Move-Three': '',
                    'Move-Four': ''},

        "golduck": {'Evolution-One': 'Psyduck', 'Evolution-Two': 'Golduck', 'Evolution-Three': '', 'Class': 'Ocean',
                    'Current HP': 80, 'Move-One': 'Scratch', 'Move-Two': 'Tail Whip', 'Move-Three': 'Water Gun',
                    'Move-Four': ''},

        "articuno": {'Evolution-One': 'Articuno', 'Evolution-Two': '', 'Evolution-Three': '',
                     'Class': 'Legendary', 'Current HP': 200, 'Move-One': 'Ice Beam', 'Move-Two': 'Blizzard',
                     'Move-Three': 'Fly', 'Move-Four': ''},

        "kyogre": {'Evolution-One': 'Kyogre',
                   'Class': 'Legendary',
                   'Current HP': 250,
                   'Move-One': 'Waterfall',
                   'Move-Two': 'Thunder',
                   'Move-Three': 'Ice Beam',
                   'Move-Four': 'Surf'}}
    return pokemon


def volcano_pokemon():
    pokemon = {
        "rapidash": {'Evolution-One': 'Ponyta', 'Evolution-Two': 'Rapidash', 'Evolution-Three': '', 'Class': 'Field',
                     'Current HP': 40, 'Move-One': 'Ember', 'Move-Two': 'Stomp', 'Move-Three': 'Double Edge',
                     'Move-Four': 'Agility'},

        "ponyta": {'Evolution-One': 'Ponyta', 'Evolution-Two': 'Rapidash', 'Evolution-Three': '', 'Class': 'Field',
                   'Current HP': 80, 'Move-One': 'Ember', 'Move-Two': 'Tackle', 'Move-Three': 'Double Edge',
                   'Move-Four': ''},

        "chimchar": {'Evolution-One': 'Chimchar', 'Evolution-Two': 'Monferno', 'Evolution-Three': 'Infernape',
                     'Class': 'Mountain', 'Current HP': 30, 'Move-One': 'Scratch', 'Move-Two': 'Ember',
                     'Move-Three': 'Agility',
                     'Move-Four': ''},

        "monferno": {'Evolution-One': 'Chimchar', 'Evolution-Two': 'Monferno', 'Evolution-Three': 'Infernape',
                     'Class': 'Mountain', 'Current HP': 60, 'Move-One': 'Mach Punch', 'Move-Two': 'Flame Wheel',
                     'Move-Three': 'Taunt', 'Move-Four': 'Fury Swipes'},

        "infernape": {'Evolution-One': 'Chimchar', 'Evolution-Two': 'Monferno', 'Evolution-Three': 'Infernape',
                      'Class': 'Mountain', 'Current HP': 90, 'Move-One': 'Close Combat', 'Move-Two': 'Flare Blitz',
                      'Move-Three': 'Thunder Punch', 'Move-Four': 'Acrobatics'},

        "magby": {'Evolution-One': 'Magby', 'Evolution-Two': 'Magmar', 'Evolution-Three': 'Magmortar',
                  'Class': 'Fire',
                  'Current HP': 30, 'Move-One': 'Ember', 'Move-Two': 'Agility', 'Move-Three': 'SmokeScreen',
                  'Move-Four': 'Fire Punch'},

        "magmar": {'Evolution-One': 'Magby', 'Evolution-Two': 'Magmar', 'Evolution-Three': 'Magmortar',
                   'Class': 'Fire',
                   'Current HP': 50, 'Move-One': 'Ember', 'Move-Two': 'Agility', 'Move-Three': 'SmokeScreen',
                   'Move-Four': 'Fire Punch'},

        "magmortar": {'Evolution-One': 'Magby', 'Evolution-Two': 'Magmar', 'Evolution-Three': 'Magmortar',
                      'Class': 'Fire',
                      'Current HP': 80, 'Move-One': 'Ember', 'Move-Two': 'Agility', 'Move-Three': 'SmokeScreen',
                      'Move-Four': 'Fire Punch'},

        "moltres": {'Evolution-One': 'Moltres', 'Evolution-Two': '', 'Evolution-Three': '',
                    'Class': 'Legendary', 'Current HP': 200, 'Move-One': 'Drill Peck', 'Move-Two': 'Flamethrower',
                    'Move-Three': 'Fly', 'Move-Four': ''}}
    return pokemon


def plain_pokemon():
    pokemon = {
        "sandshrew": {'Evolution-One': 'Sandshrew', 'Evolution-Two': 'Sandslash', 'Evolution-Three': '',
                      'Class': 'Plain',
                      'Current HP': 30, 'Move-One': 'Scratch', 'Move-Two': 'Dig', 'Move-Three': 'Poison Sting',
                      'Move-Four': ''},

        "sandslash": {'Evolution-One': 'Sandshrew', 'Evolution-Two': 'Sandslash', 'Evolution-Three': '',
                      'Class': 'Plain',
                      'Current HP': 60, 'Move-One': 'Scratch', 'Move-Two': 'Dig', 'Move-Three': 'Poison Sting',
                      'Move-Four': 'Rock Slide'},

        "clefairy": {'Evolution-One': 'Clefairy', 'Evolution-Two': 'Clefable', 'Evolution-Three': '', 'Class': 'Plain',
                     'Current HP': 30, 'Move-One': 'Pound', 'Move-Two': 'Sing', 'Move-Three': '', 'Move-Four': ''},

        "clefable": {'Evolution-One': 'Clefairy', 'Evolution-Two': 'Clefable', 'Evolution-Three': '', 'Class': 'Plain',
                     'Current HP': 60, 'Move-One': 'Pound', 'Move-Two': 'Sing', 'Move-Three': 'Metronome',
                     'Move-Four': ''},

        "vulpix": {'Evolution-One': 'Vulpix', 'Evolution-Two': 'Ninetales', 'Evolution-Three': '', 'Class': 'Plain',
                   'Current HP': 40, 'Move-One': 'Ember', 'Move-Two': 'Quick Attack', 'Move-Three': '',
                   'Move-Four': ''},

        "ninetales": {'Evolution-One': 'Vulpix', 'Evolution-Two': 'Ninetales', 'Evolution-Three': '', 'Class': 'Plain',
                      'Current HP': 80, 'Move-One': 'Ember', 'Move-Two': 'Quick Attack', 'Move-Three': 'Confuse Ray',
                      'Move-Four': ''},

        "jigglypuff": {'Evolution-One': 'Jigglypuff', 'Evolution-Two': 'Wigglytuff', 'Evolution-Three': '',
                       'Class': 'Plain', 'Current HP': 25, 'Move-One': 'Pound', 'Move-Two': 'Sing', 'Move-Three': '',
                       'Move-Four': ''},

        "wigglytuff": {'Evolution-One': 'Jigglypuff', 'Evolution-Two': 'Wigglytuff', 'Evolution-Three': '',
                       'Class': 'Plain', 'Current HP': 50, 'Move-One': 'Pound', 'Move-Two': 'Sing',
                       'Move-Three': 'Body Slam', 'Move-Four': ''},

        "meowth": {'Evolution-One': 'Meowth', 'Evolution-Two': 'Persian', 'Evolution-Three': '', 'Class': 'Plain',
                   'Current HP': 30, 'Move-One': 'Scratch', 'Move-Two': 'Growl', 'Move-Three': '', 'Move-Four': ''},

        "persian": {'Evolution-One': 'Meowth', 'Evolution-Two': 'Persian', 'Evolution-Three': '', 'Class': 'Plain',
                    'Current HP': 50, 'Move-One': 'Scratch', 'Move-Two': 'Growl', 'Move-Three': 'Bite',
                    'Move-Four': ''},

        "dragonite": {'Evolution-One': 'Dratini', 'Evolution-Two': 'Dragonair', 'Evolution-Three': 'Dragonite',
                      'Class': 'Dragon', 'Current HP': 130, 'Move-One': 'Dragon Claw', 'Move-Two': 'Fly',
                      'Move-Three': 'Hyper Beam', 'Move-Four': 'Thunder Punch'},

        "aerodactyl": {'Evolution-One': 'Aerodactyl', 'Evolution-Two': '', 'Evolution-Three': '', 'Class': 'Rock',
                       'Current HP': 130, 'Move-One': 'Ancient Power', 'Move-Two': 'Wing Attack', 'Move-Three': 'Bite',
                       'Move-Four': 'Crunch'},

        "zapdos": {'Evolution-One': 'Zapdos', 'Evolution-Two': '', 'Evolution-Three': '',
                   'Class': 'Legendary', 'Current HP': 200, 'Move-One': 'Thunderbolt', 'Move-Two': 'Thunder',
                   'Move-Three': 'Fly', 'Move-Four': ''}}
    return pokemon

#
# def get_moves():
#     moves_dict = {
#         "splash": {"Damage": 0, "Message": " splashes around, nothing happens.", "SuperEffect": "Volcano"},
#         "": {"Damage": 0, "Message": " Nothing happens.", "SuperEffect": "Volcano"},
#         "empty": {"Damage": 0, "Message": " did nothing.", "SuperEffect": "Grass"},
#         "bite": {"Damage": 60, "Message": " bites the opponent.", "SuperEffect": "Normal"},
#         "ember": {"Damage": 60, "Message": " bites the opponent.", "SuperEffect": "Normal"},
#         "dragon rage": {"Damage": 80, "Message": " hits the opponent with Dragon Rage.", "SuperEffect": "Dragon"},
#         "hydro pump": {"Damage": 110, "Message": " hits the opponent with Hydro Pump.", "SuperEffect": "Water"},
#         "dragon breath": {"Damage": 60, "Message": " hits the opponent with Dragon Breath.", "SuperEffect": "Dragon"},
#         "agility": {"Damage": 0, "Message": " uses Agility and sharply raises its speed.", "SuperEffect": "Psychic"},
#         "thunder wave": {"Damage": 0, "Message": " paralyzes the opponent with Thunder Wave.",
#                          "SuperEffect": "Electric"},
#         "aqua tail": {"Damage": 90, "Message": " hits the opponent with Aqua Tail.", "SuperEffect": "Water"},
#         "ice beam": {"Damage": 90, "Message": " hits the opponent with Ice Beam.", "SuperEffect": "Ice"},
#         "scratch": {"Damage": 40, "Message": " scratches the opponent.", "SuperEffect": "Normal"},
#         "water gun": {"Damage": 40, "Message": " hits the opponent with Water Gun.", "SuperEffect": "Water"},
#         "ice fang": {"Damage": 65, "Message": " bites the opponent with Ice Fang.", "SuperEffect": "Ice"},
#         "waterfall": {"Damage": 80, "Message": " hits the opponent with Waterfall.", "SuperEffect": "Water"},
#         "crunch": {"Damage": 80, "Message": " hits the opponent with Crunch.", "SuperEffect": "Dark"},
#         "superpower": {"Damage": 120, "Message": " hits the opponent with Superpower.", "SuperEffect": "Fighting"},
#         "tackle": {"Damage": 40, "Message": " tackles the opponent.", "SuperEffect": "Normal"},
#         "mud shot": {"Damage": 55, "Message": " hits the opponent with Mud Shot.", "SuperEffect": "Ground"},
#         "mud bomb": {"Damage": 65, "Message": " hits the opponent with Mud Bomb.", "SuperEffect": "Ground"},
#
#         "rock slide": {"Damage": 75, "Message": " hits the opponent with Rock Slide.", "SuperEffect": "Rock"},
#         "smokescreen": {"Damage": 0, "Message": " creates a smokescreen and sharply lowers the opponent's accuracy.",
#                         "SuperEffect": "Normal"},
#         "vine whip": {"Damage": 45, "Message": " hits the opponent with Vine Whip.", "SuperEffect": "Grass"},
#         "poison sting": {"Damage": 15, "Message": " hits the opponent with Poison Sting.", "SuperEffect": "Poison"},
#         "fury attack": {"Damage": 15, "Message": " hits the opponent with a a series of attacks.",
#                         "SuperEffect": "Normal"},
#         "gust": {"Damage": 40, "Message": " whips up a gust!", "SuperEffect": "Fighting"},
#         "quick attack": {"Damage": 40, "Message": " quickly strikes!", "SuperEffect": "Ghost"},
#         "sand attack": {"Damage": 0, "Message": " kicks sand!", "SuperEffect": "Flying"},
#         "wing attack": {"Damage": 60, "Message": " flaps its wings!", "SuperEffect": "Grass"},
#         "sky attack": {"Damage": 140, "Message": " charges up for a turn then swoops down with great force!",
#                        "SuperEffect": "Fighting"},
#         "feather dance": {"Damage": 0, "Message": " dances gracefully, its feathers drifting down around it.",
#                           "SuperEffect": "Fighting"},
#         "hyper fang": {"Damage": 80, "Message": " bites down with hyper fangs!", "SuperEffect": "Psychic"},
#         "super fang": {"Damage": 80, "Message": " bites down with super fangs!", "SuperEffect": "Psychic"},
#         "giant bite": {"Damage": 60, "Message": " takes a huge bite out of its opponent!", "SuperEffect": "Psychic"},
#         "wrap": {"Damage": 15, "Message": " wraps its opponent tightly!", "SuperEffect": "Flying"},
#         "acid shot": {"Damage": 40, "Message": " shoots acid at its opponent!", "SuperEffect": "Grass"},
#         "thunder shock": {"Damage": 40, "Message": " shocks its opponent with electricity!", "SuperEffect": "Water"},
#         "thunderbolt": {"Damage": 90, "Message": " strikes its opponent with a powerful bolt of electricity!",
#                         "SuperEffect": "Water"},
#         "slam": {"Damage": 80, "Message": " slams into its opponent!", "SuperEffect": "Fighting"},
#         "double edge": {"Damage": 120, "Message": " slams into its opponent with reckless abandon!",
#                         "SuperEffect": "Fighting"},
#         "flash": {"Damage": 0, "Message": " blinds its opponent with a bright flash!", "SuperEffect": "Fighting"},
#         "thunder": {"Damage": 110, "Message": " summons a thunderstorm to strike its opponent!",
#                     "SuperEffect": "Water"},
#         "growl": {"Damage": 0, "Message": " growls menacingly.", "SuperEffect": "Normal"},
#         "roar": {"Damage": 0, "Message": " lets out a mighty roar!", "SuperEffect": "Normal"},
#         "bubble": {"Damage": 40, "Message": " blows bubbles at its opponent!", "SuperEffect": "Electric"},
#         "withdraw": {"Damage": 0, "Message": " withdraws into its shell!", "SuperEffect": "Rock"},
#         "bubble beam": {"Damage": 65, "Message": " blasts its opponent with a powerful beam of bubbles!",
#                         "SuperEffect": "Electric"},
#         "screech": {"Damage": 0, "Message": " lets out a piercing screech!", "SuperEffect": "Normal"},
#         "mirror move": {"Damage": 0, "Message": " copies its opponent's last move!", "SuperEffect": "Flying"},
#         "drill peck": {"Damage": 80, "Type": "Flying", "Category": "Physical", "Accuracy": 100,
#                        "Message": " uses Drill Peck!", "SuperEffect": "Grass", "NotEffective": "Steel"},
#         "submission": {"Damage": 80, "Type": "Fighting", "Category": "Physical", "Accuracy": 80,
#                        "Message": " uses Submission!", "SuperEffect": "Normal",
#                        "NotEffective": "Flying, Poison, Bug, Psychic, Fairy"},
#         "low kick": {"Damage": 0, "Type": "Fighting", "Category": "Physical", "Accuracy": 100,
#                      "Message": " uses Low Kick!", "SuperEffect": "Ice, Rock, Steel", "NotEffective": "Ghost"},
#         "seismic toss": {"Damage": 0, "Type": "Fighting", "Category": "Physical", "Accuracy": 100,
#                          "Message": " uses Seismic Toss!", "SuperEffect": "Normal", "NotEffective": "Ghost"},
#         "mega punch": {"Damage": 80, "Type": "Normal", "Category": "Physical", "Accuracy": 85,
#                        "Message": " uses Mega Punch!", "SuperEffect": "Rock, Steel, Ice", "NotEffective": "Ghost"},
#         "mega kick": {"Damage": 120, "Type": "Normal", "Category": "Physical", "Accuracy": 75,
#                       "Message": " uses Mega Kick!", "SuperEffect": "Rock, Steel, Ice", "NotEffective": "Ghost"},
#         "counter": {"Damage": "2x", "Type": "Fighting", "Category": "Physical", "Accuracy": 100,
#                     "Message": " uses Counter!", "SuperEffect": "Normal",
#                     "NotEffective": "Flying, Poison, Bug, Psychic, Fairy"},
#         "strength": {"Damage": 80, "Type": "Normal", "Category": "Physical", "Accuracy": 100,
#                      "Message": " uses Strength!", "SuperEffect": "Rock, Steel, Ice", "NotEffective": "Ghost"},
#         "karate chop": {"Damage": 50, "Type": "Fighting", "Category": "Physical", "Accuracy": 100,
#                         "Message": " uses Karate Chop!", "SuperEffect": "Normal, Rock, Steel, Ice, Dark",
#                         "NotEffective": "Flying, Poison, Bug, Psychic, Fairy"},
#         "fissure": {"Damage": "OHKO", "Type": "Ground", "Category": "Physical", "Accuracy": 30,
#                     "Message": " uses Fissure!", "SuperEffect": "Electric, Fire, Poison, Rock, Steel",
#                     "NotEffective": "Flying"},
#         "dig": {"Damage": 80, "Type": "Ground", "Category": "Physical", "Accuracy": 100,
#                 "Message": " digs underground and uses Dig!", "SuperEffect": "Electric, Fire, Poison, Rock, Steel",
#                 "NotEffective": "Flying"},
#         "sonic boom": {"Damage": 20, "Type": "Normal", "Category": "Special", "Accuracy": 90,
#                        "Message": " uses Sonic Boom!", "SuperEffect": "N/A", "NotEffective": "N/A"},
#         "rock throw": {"Damage": 50, "Type": "Rock", "Category": "Physical", "Accuracy": 90,
#                        "Message": " uses Rock Throw!", "SuperEffect": "Bug, Fire, Flying, Ice",
#                        "NotEffective": "Fighting, Ground, Steel"},
#         "earthquake": {"Damage": 100, "Type": "Ground", "Category": "Physical", "Accuracy": 100,
#                        "PP": 10, "Message": " caused an earthquake!"},
#
#         "fire punch": {"Damage": 75, "Type": "Fire", "Category": "Physical", "Accuracy": 100,
#                        "PP": 15, "Message": " hit with a fiery punch!", "Effect": "Burn", "EffectRate": 10},
#
#         "ice punch": {"Damage": 75, "Type": "Ice", "Category": "Physical", "Accuracy": 100,
#                       "PP": 15, "Message": " hit with an icy punch!", "Effect": "Freeze", "EffectRate": 10},
#
# "thunder punch": {"Damage": 75, "Type": "Electric", "Category": "Physical", "Accuracy": 100, "PP": 15, "Message": "
# hit with an electric punch!", "Effect": "Paralyze", "EffectRate": 10},
#
#         "fly": {"Damage": 90, "Type": "Flying", "Category": "Physical", "Accuracy": 95,
#                 "PP": 15, "Message": " took to the skies and dove down with great force!"},
#         "Spore": {"Damage": 60, "Message": " bites the opponent.", "SuperEffect": "Normal"},
#         "Ancient Power": {"Damage": 60, "Message": " batters the opponent with power from ancient times.",
#                           "SuperEffect": "Rock"},
#         "Teleport": {"Damage": 0, "Message": " disappears instantly, allowing the user to switch out.",
#                      "SuperEffect": "Psychic"},
#         "Confuse Ray": {"Damage": 0, "Message": " confuses the opponent.", "SuperEffect": "Ghost"},
#         "Metronome": {"Damage": 0, "Message": " randomly selects and uses any move in the game.",
#                       "SuperEffect": "Normal"},
#         "Pound": {"Damage": 40, "Message": " pounds the opponent.", "SuperEffect": "Normal"},
#         "Surf": {"Damage": 90, "Message": " washes away the opponent.", "SuperEffect": "Water"},
#         "Lick": {"Damage": 30, "Message": " licks the opponent.", "SuperEffect": "Ghost"},
#         "Poison Powder": {"Damage": 0, "Message": " poisons the opponent.", "SuperEffect": "Poison"},
#         "Sing": {"Damage": 0, "Message": " puts the opponent to sleep with a soothing song.",
#                  "SuperEffect": "Normal"},
#         "Double Kick": {"Damage": 30, "Message": " kicks the opponent twice.", "SuperEffect": "Fighting"},
#         "Dragon Claw": {"Damage": 80, "Message": " slashes the opponent with sharp claws.",
#                         "SuperEffect": "Dragon"},
#         "Ice-Beam": {"Damage": 90, "Message": " freezes the opponent.", "SuperEffect": "Ice"},
#         "Supersonic": {"Damage": 0, "Message": " confuses the opponent with supersonic waves.",
#                        "SuperEffect": "Normal"},
#         "Leech Life": {"Damage": 80, "Message": " drains the opponent's blood, restoring the user's HP.",
#                        "SuperEffect": "Bug"},
#         "Aura Sphere": {"Damage": 80, "Message": " unleashes a sphere of aura.", "SuperEffect": "Fighting"},
#         "Dream Eater": {"Damage": 100, "Message": " eats the opponent's dreams, restoring the user's HP.",
#                         "SuperEffect": "Psychic"},
#         "Recover": {"Damage": 0, "Message": " restores the user's HP.", "SuperEffect": "Normal"},
#         "Blizzard": {"Damage": 110, "Message": " freezes the opponent with a blizzard.", "SuperEffect": "Ice"},
#         "Hyper Beam": {"Damage": 150, "Message": " blasts the opponent with a powerful beam.",
#                        "SuperEffect": "Normal"},
#         "Shadow Force": {"Damage": 120, "Message": " disappears, then strikes the opponent on the next turn.",
#                          "SuperEffect": "Ghost"},
#         "Hypnosis": {"Damage": 0, "Message": " hypnotizes the opponent.", "SuperEffect": "Psychic"},
#         "Peck": {"Damage": 35, "Message": " pecks the opponent.", "SuperEffect": "Flying"},
#         "Thrash": {"Damage": 120, "Message": " thrashes about, becoming uncontrollable.", "SuperEffect": "Normal"},
#         "body-slam": {"Damage": 85, "Message": " slams into the opponent.", "SuperEffect": "Normal"},
#         "disable": {"Damage": 0, "Message": " disables the opponent's last move!", "SuperEffect": "Normal"},
#         "stun spore": {"Damage": 0, "Message": " scatters a cloud of paralyzing powder!", "SuperEffect": "Normal"},
#         "tail whip": {"Damage": 0, "Message": " whips the opponent with its tail!", "SuperEffect": "Normal"},
#         "judgment": {"Damage": 100, "Message": " unleashes its full power!", "SuperEffect": "Normal"},
#         "psybeam": {"Damage": 65, "Message": " attacks with a peculiar ray that may confuse the opponent.",
#                     "SuperEffect": "Psychic"},
#         "iron tail": {"Damage": 100, "Message": " slams the opponent with its steel hard tail.",
#                       "SuperEffect": "Steel"},
#         "focus punch": {"Damage": 150,
#                         "Message": "readies itself and attacks the next turn. This move cannot be selected if the "
#                                    "user is hit before it is used.",
#                         "SuperEffect": "Fighting"}
#
#     }
#     return moves_dict
#
#
# def check_moves():
#     moves = []
#     for move in list(get_moves()):
#         moves.append(move.lower())
#     pokemon_values = []
#     unregistered_moves = set()
#     for pokemon in starter_pokemon().values():
#         pokemon_values.append(pokemon)
#     for pokemon in forest_pokemon().values():
#         pokemon_values.append(pokemon)
#     for pokemon in ocean_pokemon().values():
#         pokemon_values.append(pokemon)
#     for pokemon in mine_pokemon().values():
#         pokemon_values.append(pokemon)
#     for pokemon in plain_pokemon().values():
#         pokemon_values.append(pokemon)
#     for poke_dict in pokemon_values:
#         if poke_dict['Move-One'].lower() not in moves:
#             unregistered_moves.add(poke_dict['Move-One'])
#         if poke_dict['Move-Two'].lower() not in moves:
#             unregistered_moves.add(poke_dict['Move-Two'])
#         if poke_dict['Move-Three'].lower() not in moves:
#             unregistered_moves.add(poke_dict['Move-Three'])
#         if poke_dict['Move-Four'].lower() not in moves:
#             unregistered_moves.add(poke_dict['Move-Four'])
#     print(unregistered_moves)
#
#
# check_moves()
