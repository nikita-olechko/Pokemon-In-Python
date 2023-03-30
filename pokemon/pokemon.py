def starter_pokemon() -> dict:
    starter_dict = {
        "bulbasaur": {'Evolution-One': 'Bulbasaur', 'Evolution-Two': 'Ivysaur', 'Evolution-Three': 'Venusaur',
                      'Class': 'Forest', 'Current HP': 50, 'Move-One': 'Tackle', 'Move-Two': 'Vine Whip',
                      'Move-Three': '',
                      'Move-Four': ''},

        "charmander": {'Evolution-One': 'Charmander', 'Evolution-Two': 'Charmeleon', 'Evolution-Three': 'Charizard',
                       'Class': 'Plain', 'Current HP': 50, 'Move-One': 'Scratch', 'Move-Two': 'Ember', 'Move-Three': '',
                       'Move-Four': ''},

        "squirtle": {'Evolution-One': 'Squirtle', 'Evolution-Two': 'Wartortle', 'Evolution-Three': 'Blastoise',
                     'Class': 'Water', 'Current HP': 50, 'Move-One': 'Tackle', 'Move-Two': 'Water Gun',
                     'Move-Three': '',
                     'Move-Four': ''}}
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
                   'Current HP': 200,
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
