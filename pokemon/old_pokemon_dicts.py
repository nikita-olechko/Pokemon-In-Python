import json


def starter_pokemon_dict() -> dict:
    starter_dict = {
        'bulbasaur': {'Evolution-One': 'Bulbasaur', 'Evolution-Two': 'Ivysaur', 'Evolution-Three': 'Venusaur',
                      'Class': 'Forest', 'Current HP': 100, 'Move-One': 'Tackle', 'Move-Two': 'Vine Whip',
                      'Move-Three': '', 'Move-Four': '', 'Location': 'Starter'},
        'ivysaur': {'Evolution-One': 'Bulbasaur', 'Evolution-Two': 'Ivysaur', 'Evolution-Three': 'Venusaur',
                    'Class': 'Forest', 'Current HP': 150, 'Move-One': 'Tackle', 'Move-Two': 'Vine Whip',
                    'Move-Three': 'Earthquake', 'Move-Four': '', 'Location': 'Starter'},
        'venusaur': {'Evolution-One': 'Bulbasaur', 'Evolution-Two': 'Ivysaur', 'Evolution-Three': 'Venusaur',
                     'Class': 'Forest', 'Current HP': 200, 'Move-One': 'Tackle', 'Move-Two': 'Vine Whip',
                     'Move-Three': 'Earthquake', 'Move-Four': 'Hyper Beam', 'Location': 'Starter'},
        'charmander': {'Evolution-One': 'Charmander', 'Evolution-Two': 'Charmeleon', 'Evolution-Three': 'Charizard',
                       'Class': 'Plain', 'Current HP': 100, 'Move-One': 'Scratch', 'Move-Two': 'Ember',
                       'Move-Three': '',
                       'Move-Four': '', 'Location': 'Starter'},
        'charmeleon': {'Evolution-One': 'Charmander', 'Evolution-Two': 'Charmeleon', 'Evolution-Three': 'Charizard',
                       'Class': 'Plain', 'Current HP': 150, 'Move-One': 'Scratch', 'Move-Two': 'Ember',
                       'Move-Three': 'Earthquake', 'Move-Four': '', 'Location': 'Starter'},
        'charizard': {'Evolution-One': 'Charmander', 'Evolution-Two': 'Charmeleon', 'Evolution-Three': 'Charizard',
                      'Class': 'Plain', 'Current HP': 200, 'Move-One': 'Scratch', 'Move-Two': 'Ember',
                      'Move-Three': 'Earthquake', 'Move-Four': 'Hyper Beam', 'Location': 'Starter'},
        'squirtle': {'Evolution-One': 'Squirtle', 'Evolution-Two': 'Wartortle', 'Evolution-Three': 'Blastoise',
                     'Class': 'Water', 'Current HP': 100, 'Move-One': 'Tackle', 'Move-Two': 'Water Gun',
                     'Move-Three': '',
                     'Move-Four': '', 'Location': 'Starter'},
        'wartortle': {'Evolution-One': 'Squirtle', 'Evolution-Two': 'Wartortle', 'Evolution-Three': 'Blastoise',
                      'Class': 'Water', 'Current HP': 150, 'Move-One': 'Tackle', 'Move-Two': 'Water Gun',
                      'Move-Three': 'Earthquake', 'Move-Four': '', 'Location': 'Starter'},
        'blastoise': {'Evolution-One': 'Squirtle', 'Evolution-Two': 'Wartortle', 'Evolution-Three': 'Blastoise',
                      'Class': 'Water', 'Current HP': 200, 'Move-One': 'Tackle', 'Move-Two': 'Water Gun',
                      'Move-Three': 'Earthquake', 'Move-Four': 'Hyper Beam', 'Location': 'Starter'}}
    return starter_dict


def forest_pokemon() -> dict:
    forest_dict = {
        'caterpie': {'Evolution-One': 'Caterpie', 'Evolution-Two': 'Metapod', 'Evolution-Three': 'Butterfree',
                     'Class': 'Forest', 'Current HP': 30, 'Move-One': 'Tackle', 'Move-Two': '', 'Move-Three': '',
                     'Move-Four': '', 'Location': 'Forest'},
        'metapod': {'Evolution-One': 'Caterpie', 'Evolution-Two': 'Metapod', 'Evolution-Three': 'Butterfree',
                    'Class': 'Forest', 'Current HP': 30, 'Move-One': 'Tackle', 'Move-Two': 'Fury Attack',
                    'Move-Three': '',
                    'Move-Four': '', 'Location': 'Forest'},
        'butterfree': {'Evolution-One': 'Caterpie', 'Evolution-Two': 'Metapod', 'Evolution-Three': 'Butterfree',
                       'Class': 'Forest', 'Current HP': 30, 'Move-One': 'Tackle', 'Move-Two': 'Fury Attack',
                       'Move-Three': 'Sky Attack',
                       'Move-Four': '', 'Location': 'Forest'},
        'weedle': {'Evolution-One': 'Weedle', 'Evolution-Two': 'Kakuna', 'Evolution-Three': 'Beedrill',
                   'Class': 'Forest',
                   'Current HP': 50, 'Move-One': 'Poison Sting', 'Move-Two': '', 'Move-Three': '', 'Move-Four': '',
                   'Location': 'Forest'},
        'kakuna': {'Evolution-One': 'Weedle', 'Evolution-Two': 'Kakuna', 'Evolution-Three': 'Beedrill',
                   'Class': 'Forest',
                   'Current HP': 50, 'Move-One': 'Poison Sting', 'Move-Two': 'Agility', 'Move-Three': '', 'Move-Four': '',
                   'Location': 'Forest'},
        'beedrill': {'Evolution-One': 'Weedle', 'Evolution-Two': 'Kakuna', 'Evolution-Three': 'Beedrill',
                     'Class': 'Forest', 'Current HP': 100, 'Move-One': 'Poison Sting', 'Move-Two': 'Agility',
                     'Move-Three': 'Fury Attack', 'Move-Four': '', 'Location': 'Forest'},
        'pidgey': {'Evolution-One': 'Pidgey', 'Evolution-Two': 'Pidgeotto', 'Evolution-Three': 'Pidgeot',
                   'Class': 'Forest', 'Current HP': 30, 'Move-One': 'Tackle', 'Move-Two': 'Gust', 'Move-Three': '',
                   'Move-Four': '', 'Location': 'Forest'},
        'pidgeotto': {'Evolution-One': 'Pidgey', 'Evolution-Two': 'Pidgeotto', 'Evolution-Three': 'Pidgeot',
                      'Class': 'Forest', 'Current HP': 50, 'Move-One': 'Gust', 'Move-Two': 'Quick Attack',
                      'Move-Three': 'Sand Attack', 'Move-Four': '', 'Location': 'Forest'},
        'pidgeot': {'Evolution-One': 'Pidgey', 'Evolution-Two': 'Pidgeotto', 'Evolution-Three': 'Pidgeot',
                    'Class': 'Forest', 'Current HP': 100, 'Move-One': 'Wing Attack', 'Move-Two': 'Sky Attack',
                    'Move-Three': 'Feather Dance', 'Move-Four': 'Agility', 'Location': 'Forest'},
        'rattata': {'Evolution-One': 'Rattata', 'Evolution-Two': 'Raticate', 'Evolution-Three': '', 'Class': 'Forest',
                    'Current HP': 50, 'Move-One': 'Tackle', 'Move-Two': '', 'Move-Three': '', 'Move-Four': '',
                    'Location': 'Forest'},
        'raticate': {'Evolution-One': 'Rattata', 'Evolution-Two': 'Raticate', 'Evolution-Three': '', 'Class': 'Forest',
                     'Current HP': 100, 'Move-One': 'Hyper Fang', 'Move-Two': 'Super Fang', 'Move-Three': 'Giant Bite',
                     'Move-Four': '', 'Location': 'Forest'},
        'ekans': {'Evolution-One': 'Ekans', 'Evolution-Two': 'Arbok', 'Evolution-Three': '', 'Class': 'Forest',
                  'Current HP': 30, 'Move-One': 'Wrap', 'Move-Two': 'Poison Sting', 'Move-Three': '', 'Move-Four': '',
                  'Location': 'Forest'},
        'arbok': {'Evolution-One': 'Ekans', 'Evolution-Two': 'Arbok', 'Evolution-Three': '', 'Class': 'Forest',
                  'Current HP': 80, 'Move-One': 'Wrap', 'Move-Two': 'Poison Sting', 'Move-Three': 'Acid Shot',
                  'Move-Four': '', 'Location': 'Forest'},
        'pikachu': {'Evolution-One': 'Pichu', 'Evolution-Two': 'Pikachu', 'Evolution-Three': 'Raichu',
                    'Class': 'Forest',
                    'Current HP': 50, 'Move-One': 'Quick Attack', 'Move-Two': 'Thunderbolt', 'Move-Three': 'Iron Tail',
                    'Move-Four': '', 'Location': 'Forest'},
        'raichu': {'Evolution-One': 'Pichu', 'Evolution-Two': 'Pikachu', 'Evolution-Three': 'Raichu', 'Class': 'Forest',
                   'Current HP': 100, 'Move-One': 'Quick Attack', 'Move-Two': 'Thunderbolt', 'Move-Three': 'Iron Tail',
                   'Move-Four': 'Focus Punch', 'Location': 'Forest'},
        'nidoranf': {'Evolution-One': 'Nidoran♀', 'Evolution-Two': 'Nidorina', 'Evolution-Three': 'Nidoqueen',
                     'Class': 'Forest', 'Current HP': 30, 'Move-One': 'Scratch', 'Move-Two': 'Double Kick',
                     'Move-Three': '', 'Move-Four': '', 'Location': 'Forest'},
        'nidorina': {'Evolution-One': 'Nidoran♀', 'Evolution-Two': 'Nidorina', 'Evolution-Three': 'Nidoqueen',
                     'Class': 'Forest', 'Current HP': 50, 'Move-One': 'Scratch', 'Move-Two': 'Double Kick',
                     'Move-Three': 'Poison Sting', 'Move-Four': '', 'Location': 'Forest'},
        'nidoqueen': {'Evolution-One': 'Nidoran♀', 'Evolution-Two': 'Nidorina', 'Evolution-Three': 'Nidoqueen',
                      'Class': 'Forest', 'Current HP': 100, 'Move-One': 'Scratch', 'Move-Two': 'Double Kick',
                      'Move-Three': 'Poison Sting', 'Move-Four': 'Body Slam', 'Location': 'Forest'},
        'nidoranm': {'Evolution-One': 'Nidoran♂', 'Evolution-Two': 'Nidorino', 'Evolution-Three': 'Nidoking',
                     'Class': 'Forest', 'Current HP': 30, 'Move-One': 'Peck', 'Move-Two': 'Double Kick',
                     'Move-Three': '',
                     'Move-Four': '', 'Location': 'Forest'},
        'nidorino': {'Evolution-One': 'Nidoran♂', 'Evolution-Two': 'Nidorino', 'Evolution-Three': 'Nidoking',
                     'Class': 'Forest', 'Current HP': 50, 'Move-One': 'Peck', 'Move-Two': 'Double Kick',
                     'Move-Three': 'Poison Sting', 'Move-Four': '', 'Location': 'Forest'},
        'nidoking': {'Evolution-One': 'Nidoran♂', 'Evolution-Two': 'Nidorino', 'Evolution-Three': 'Nidoking',
                     'Class': 'Forest', 'Current HP': 100, 'Move-One': 'Peck', 'Move-Two': 'Double Kick',
                     'Move-Three': 'Poison Sting', 'Move-Four': 'Thrash', 'Location': 'Forest'},
        'paras': {'Evolution-One': 'Paras', 'Evolution-Two': 'Parasect', 'Evolution-Three': '', 'Class': 'Forest',
                  'Current HP': 30, 'Move-One': 'Scratch', 'Move-Two': 'Stun Spore', 'Move-Three': '', 'Move-Four': '',
                  'Location': 'Forest'},
        'parasect': {'Evolution-One': 'Paras', 'Evolution-Two': 'Parasect', 'Evolution-Three': '', 'Class': 'Forest',
                     'Current HP': 50, 'Move-One': 'Scratch', 'Move-Two': 'Stun Spore', 'Move-Three': 'Spore',
                     'Move-Four': '', 'Location': 'Forest'},
        'venonat': {'Evolution-One': 'Venonat', 'Evolution-Two': 'Venomoth', 'Evolution-Three': '', 'Class': 'Mine',
                    'Current HP': 30, 'Move-One': 'Tackle', 'Move-Two': 'Disable', 'Move-Three': '', 'Move-Four': '',
                    'Location': 'Forest'},
        'venomoth': {'Evolution-One': 'Venonat', 'Evolution-Two': 'Venomoth', 'Evolution-Three': '', 'Class': 'Mine',
                     'Current HP': 60, 'Move-One': 'Tackle', 'Move-Two': 'Disable', 'Move-Three': 'Poison Powder',
                     'Move-Four': '', 'Location': 'Forest'},
        'diglett': {'Evolution-One': 'Diglett', 'Evolution-Two': 'Dugtrio', 'Evolution-Three': '', 'Class': 'Mine',
                    'Current HP': 40, 'Move-One': 'Scratch', 'Move-Two': 'Growl', 'Move-Three': '', 'Move-Four': '',
                    'Location': 'Forest'},
        'dugtrio': {'Evolution-One': 'Diglett', 'Evolution-Two': 'Dugtrio', 'Evolution-Three': '', 'Class': 'Mine',
                    'Current HP': 80, 'Move-One': 'Scratch', 'Move-Two': 'Growl', 'Move-Three': 'Dig', 'Move-Four': '',
                    'Location': 'Forest'}}
    return forest_dict


def boss_battle_pokemon():
    boss_dict = {'arceus': {'Evolution-One': 'Arceus', 'Class': 'Legendary', 'Current HP': 400, 'Move-One': 'Judgment',
                            'Move-Two': 'Recover', 'Move-Three': 'Hyper Beam', 'Move-Four': 'Earthquake',
                            'Location': 'Volcano'}}
    return boss_dict


def mine_pokemon():
    pokemon = {'zubat': {'Evolution-One': 'Zubat', 'Evolution-Two': 'Golbat', 'Evolution-Three': '', 'Class': 'Mine',
                         'Current HP': 40, 'Move-One': 'Leech Life', 'Move-Two': 'Supersonic', 'Move-Three': '',
                         'Move-Four': '', 'Location': 'Mine'},
               'golbat': {'Evolution-One': 'Zubat', 'Evolution-Two': 'Golbat', 'Evolution-Three': '', 'Class': 'Mine',
                          'Current HP': 80, 'Move-One': 'Leech Life', 'Move-Two': 'Supersonic',
                          'Move-Three': 'Wing Attack', 'Move-Four': '', 'Location': 'Mine'},
               'onix': {'Evolution-One': 'Onix', 'Evolution-Two': 'Steelix', 'Evolution-Three': '', 'Class': 'Cave',
                        'Current HP': 60, 'Move-One': 'Rock Throw', 'Move-Two': 'Tackle', 'Move-Three': '',
                        'Move-Four': '', 'Location': 'Mine'},
               'steelix': {'Evolution-One': 'Onix', 'Evolution-Two': 'Steelix', 'Evolution-Three': '', 'Class': 'Cave',
                           'Current HP': 100, 'Move-One': 'Iron Tail', 'Move-Two': 'Earthquake',
                           'Move-Three': 'Crunch', 'Move-Four': 'Dragon Breath', 'Location': 'Mine'},
               'gastly': {'Evolution-One': 'Gastly', 'Evolution-Two': 'Haunter', 'Evolution-Three': 'Gengar',
                          'Class': 'Ghost', 'Current HP': 30, 'Move-One': 'Lick', 'Move-Two': 'Hypnosis',
                          'Move-Three': 'Dream Eater', 'Move-Four': '', 'Location': 'Mine'},
               'haunter': {'Evolution-One': 'Gastly', 'Evolution-Two': 'Haunter', 'Evolution-Three': 'Gengar',
                           'Class': 'Ghost', 'Current HP': 50, 'Move-One': 'Lick', 'Move-Two': 'Hypnosis',
                           'Move-Three': 'Dream Eater', 'Move-Four': '', 'Location': 'Mine'},
               'gengar': {'Evolution-One': 'Gastly', 'Evolution-Two': 'Haunter', 'Evolution-Three': 'Gengar',
                          'Class': 'Ghost', 'Current HP': 80, 'Move-One': 'Lick', 'Move-Two': 'Hypnosis',
                          'Move-Three': 'Dream Eater', 'Move-Four': '', 'Location': 'Mine'},
               'abra': {'Evolution-One': 'Abra', 'Evolution-Two': 'Kadabra', 'Evolution-Three': 'Alakazam',
                        'Class': 'Psychic', 'Current HP': 30, 'Move-One': 'Teleport', 'Move-Two': 'Psybeam',
                        'Move-Three': 'Recover', 'Move-Four': '', 'Location': 'Mine'},
               'kadabra': {'Evolution-One': 'Abra', 'Evolution-Two': 'Kadabra', 'Evolution-Three': 'Alakazam',
                           'Class': 'Psychic', 'Current HP': 50, 'Move-One': 'Teleport', 'Move-Two': 'Psybeam',
                           'Move-Three': 'Recover', 'Move-Four': '', 'Location': 'Mine'},
               'alakazam': {'Evolution-One': 'Abra', 'Evolution-Two': 'Kadabra', 'Evolution-Three': 'Alakazam',
                            'Class': 'Psychic', 'Current HP': 30, 'Move-One': 'Teleport', 'Move-Two': 'Psybeam',
                            'Move-Three': 'Recover', 'Move-Four': '', 'Location': 'Mine'},
               'giratina': {'Evolution-One': 'Giratina', 'Evolution-Two': '', 'Evolution-Three': '',
                            'Class': 'Legendary', 'Current HP': 200, 'Move-One': 'Dragon Claw',
                            'Move-Two': 'Shadow Force', 'Move-Three': 'Aura Sphere', 'Move-Four': 'Hyper Beam',
                            'Location': 'Mine'}}
    return pokemon


def ocean_pokemon():
    pokemon = {
        'magikarp': {'Evolution-One': 'Magikarp', 'Evolution-Two': 'Gyarados', 'Evolution-Three': '', 'Class': 'Water',
                     'Current HP': 50, 'Move-One': 'Splash', 'Move-Two': '', 'Move-Three': '', 'Move-Four': '',
                     'Location': 'Ocean'},
        'gyarados': {'Evolution-One': 'Magikarp', 'Evolution-Two': 'Gyarados', 'Evolution-Three': '', 'Class': 'Water',
                     'Current HP': 150, 'Move-One': 'Bite', 'Move-Two': 'Dragon Rage', 'Move-Three': 'Hydro Pump',
                     'Move-Four': '', 'Location': 'Ocean'},
        'dratini': {'Evolution-One': 'Dratini', 'Evolution-Two': 'Dragonair', 'Evolution-Three': 'Dragonite',
                    'Class': 'Dragon', 'Current HP': 50, 'Move-One': 'Dragon Breath', 'Move-Two': 'Agility',
                    'Move-Three': '', 'Move-Four': '', 'Location': 'Ocean'},
        'dragonair': {'Evolution-One': 'Dratini', 'Evolution-Two': 'Dragonair', 'Evolution-Three': 'Dragonite',
                      'Class': 'Dragon', 'Current HP': 80, 'Move-One': 'Dragon Breath', 'Move-Two': 'Thunder Wave',
                      'Move-Three': 'Aqua Tail', 'Move-Four': 'Ice Beam', 'Location': 'Ocean'},
        'dragonite': {'Evolution-One': 'Dratini', 'Evolution-Two': 'Dragonair', 'Evolution-Three': 'Dragonite',
                      'Class': 'Dragon', 'Current HP': 130, 'Move-One': 'Dragon Claw', 'Move-Two': 'Fly',
                      'Move-Three': 'Hyper Beam', 'Move-Four': 'Thunder Punch', 'Location': 'Ocean'},
        'totodile': {'Evolution-One': 'Totodile', 'Evolution-Two': 'Croconaw', 'Evolution-Three': 'Feraligatr',
                     'Class': 'Water', 'Current HP': 40, 'Move-One': 'Scratch', 'Move-Two': 'Water Gun',
                     'Move-Three': '',
                     'Move-Four': '', 'Location': 'Ocean'},
        'croconaw': {'Evolution-One': 'Totodile', 'Evolution-Two': 'Croconaw', 'Evolution-Three': 'Feraligatr',
                     'Class': 'Water', 'Current HP': 60, 'Move-One': 'Bite', 'Move-Two': 'Aqua Tail', 'Move-Three': '',
                     'Move-Four': '', 'Location': 'Ocean'},
        'feraligatr': {'Evolution-One': 'Totodile', 'Evolution-Two': 'Croconaw', 'Evolution-Three': 'Feraligatr',
                       'Class': 'Water', 'Current HP': 80, 'Move-One': 'Ice Fang', 'Move-Two': 'Waterfall',
                       'Move-Three': 'Crunch', 'Move-Four': 'Superpower', 'Location': 'Ocean'},
        'mudkip': {'Evolution-One': 'Mudkip', 'Evolution-Two': 'Marshtomp', 'Evolution-Three': 'Swampert',
                   'Class': 'Water', 'Current HP': 30, 'Move-One': 'Tackle', 'Move-Two': 'Water Gun', 'Move-Three': '',
                   'Move-Four': '', 'Location': 'Ocean'},
        'marshtomp': {'Evolution-One': 'Mudkip', 'Evolution-Two': 'Marshtomp', 'Evolution-Three': 'Swampert',
                      'Class': 'Water', 'Current HP': 50, 'Move-One': 'Mud Shot', 'Move-Two': 'Water Gun',
                      'Move-Three': 'Mud Bomb', 'Move-Four': '', 'Location': 'Ocean'},
        'swampert': {'Evolution-One': 'Mudkip', 'Evolution-Two': 'Marshtomp', 'Evolution-Three': 'Swampert',
                     'Class': 'Water', 'Current HP': 80, 'Move-One': 'Hydro Pump', 'Move-Two': 'Earthquake',
                     'Move-Three': 'Ice Punch', 'Move-Four': 'Rock Slide', 'Location': 'Ocean'},
        'seadra': {'Evolution-One': 'Horsea', 'Evolution-Two': 'Seadra', 'Evolution-Three': 'Kingdra', 'Class': 'Water',
                   'Current HP': 50, 'Move-One': 'Water Gun', 'Move-Two': 'Agility', 'Move-Three': 'SmokeScreen',
                   'Move-Four': 'Waterfall', 'Location': 'Ocean'},
        'kingdra': {'Evolution-One': 'Horsea', 'Evolution-Two': 'Seadra', 'Evolution-Three': 'Kingdra',
                    'Class': 'Water',
                    'Current HP': 80, 'Move-One': 'Water Gun', 'Move-Two': 'Agility', 'Move-Three': 'SmokeScreen',
                    'Move-Four': 'Waterfall', 'Location': 'Ocean'},
        'horsea': {'Evolution-One': 'Horsea', 'Evolution-Two': 'Seadra', 'Evolution-Three': 'Kingdra', 'Class': 'Water',
                   'Current HP': 50, 'Move-One': 'Water Gun', 'Move-Two': 'Agility', 'Move-Three': 'SmokeScreen',
                   'Move-Four': 'Ice-Beam', 'Location': 'Ocean'},
        'psyduck': {'Evolution-One': 'Psyduck', 'Evolution-Two': 'Golduck', 'Evolution-Three': '', 'Class': 'Ocean',
                    'Current HP': 50, 'Move-One': 'Scratch', 'Move-Two': 'Tail Whip', 'Move-Three': '', 'Move-Four': '',
                    'Location': 'Ocean'},
        'golduck': {'Evolution-One': 'Psyduck', 'Evolution-Two': 'Golduck', 'Evolution-Three': '', 'Class': 'Ocean',
                    'Current HP': 80, 'Move-One': 'Scratch', 'Move-Two': 'Tail Whip', 'Move-Three': 'Water Gun',
                    'Move-Four': '', 'Location': 'Ocean'},
        'articuno': {'Evolution-One': 'Articuno', 'Evolution-Two': '', 'Evolution-Three': '', 'Class': 'Legendary',
                     'Current HP': 200, 'Move-One': 'Ice Beam', 'Move-Two': 'Blizzard', 'Move-Three': 'Fly',
                     'Move-Four': '', 'Location': 'Ocean'},
        'kyogre': {'Evolution-One': 'Kyogre', 'Class': 'Legendary', 'Current HP': 250, 'Move-One': 'Waterfall',
                   'Move-Two': 'Thunder', 'Move-Three': 'Ice Beam', 'Move-Four': 'Surf', 'Location': 'Ocean'}}

    return pokemon


def volcano_pokemon():
    pokemon = {
        'rapidash': {'Evolution-One': 'Ponyta', 'Evolution-Two': 'Rapidash', 'Evolution-Three': '', 'Class': 'Field',
                     'Current HP': 40, 'Move-One': 'Ember', 'Move-Two': 'Stomp', 'Move-Three': 'Double Edge',
                     'Move-Four': 'Agility', 'Location': 'Volcano'},
        'ponyta': {'Evolution-One': 'Ponyta', 'Evolution-Two': 'Rapidash', 'Evolution-Three': '', 'Class': 'Field',
                   'Current HP': 80, 'Move-One': 'Ember', 'Move-Two': 'Tackle', 'Move-Three': 'Double Edge',
                   'Move-Four': '', 'Location': 'Volcano'},
        'chimchar': {'Evolution-One': 'Chimchar', 'Evolution-Two': 'Monferno', 'Evolution-Three': 'Infernape',
                     'Class': 'Mountain', 'Current HP': 30, 'Move-One': 'Scratch', 'Move-Two': 'Ember',
                     'Move-Three': 'Agility', 'Move-Four': '', 'Location': 'Volcano'},
        'monferno': {'Evolution-One': 'Chimchar', 'Evolution-Two': 'Monferno', 'Evolution-Three': 'Infernape',
                     'Class': 'Mountain', 'Current HP': 60, 'Move-One': 'Mach Punch', 'Move-Two': 'Flame Wheel',
                     'Move-Three': 'Taunt', 'Move-Four': 'Fury Swipes', 'Location': 'Volcano'},
        'infernape': {'Evolution-One': 'Chimchar', 'Evolution-Two': 'Monferno', 'Evolution-Three': 'Infernape',
                      'Class': 'Mountain', 'Current HP': 90, 'Move-One': 'Close Combat', 'Move-Two': 'Flare Blitz',
                      'Move-Three': 'Thunder Punch', 'Move-Four': 'Acrobatics', 'Location': 'Volcano'},
        'magby': {'Evolution-One': 'Magby', 'Evolution-Two': 'Magmar', 'Evolution-Three': 'Magmortar', 'Class': 'Fire',
                  'Current HP': 30, 'Move-One': 'Ember', 'Move-Two': 'Agility', 'Move-Three': 'SmokeScreen',
                  'Move-Four': 'Fire Punch', 'Location': 'Volcano'},
        'magmar': {'Evolution-One': 'Magby', 'Evolution-Two': 'Magmar', 'Evolution-Three': 'Magmortar', 'Class': 'Fire',
                   'Current HP': 50, 'Move-One': 'Ember', 'Move-Two': 'Agility', 'Move-Three': 'SmokeScreen',
                   'Move-Four': 'Fire Punch', 'Location': 'Volcano'},
        'magmortar': {'Evolution-One': 'Magby', 'Evolution-Two': 'Magmar', 'Evolution-Three': 'Magmortar',
                      'Class': 'Fire',
                      'Current HP': 80, 'Move-One': 'Ember', 'Move-Two': 'Agility', 'Move-Three': 'SmokeScreen',
                      'Move-Four': 'Fire Punch', 'Location': 'Volcano'},
        'moltres': {'Evolution-One': 'Moltres', 'Evolution-Two': '', 'Evolution-Three': '', 'Class': 'Legendary',
                    'Current HP': 200, 'Move-One': 'Drill Peck', 'Move-Two': 'Flamethrower', 'Move-Three': 'Fly',
                    'Move-Four': '', 'Location': 'Volcano'}}
    return pokemon


def plains_pokemon():
    pokemon = {'sandshrew': {'Evolution-One': 'Sandshrew', 'Evolution-Two': 'Sandslash', 'Evolution-Three': '',
                             'Class': 'Plain',
                             'Current HP': 30, 'Move-One': 'Scratch', 'Move-Two': 'Dig', 'Move-Three': 'Poison Sting',
                             'Move-Four': '', 'Location': 'Plain'},
               'sandslash': {'Evolution-One': 'Sandshrew', 'Evolution-Two': 'Sandslash', 'Evolution-Three': '',
                             'Class': 'Plain',
                             'Current HP': 60, 'Move-One': 'Scratch', 'Move-Two': 'Dig', 'Move-Three': 'Poison Sting',
                             'Move-Four': 'Rock Slide', 'Location': 'Plain'},
               'clefairy': {'Evolution-One': 'Clefairy', 'Evolution-Two': 'Clefable', 'Evolution-Three': '',
                            'Class': 'Plain',
                            'Current HP': 30, 'Move-One': 'Pound', 'Move-Two': 'Sing', 'Move-Three': '',
                            'Move-Four': '',
                            'Location': 'Plain'},
               'clefable': {'Evolution-One': 'Clefairy', 'Evolution-Two': 'Clefable', 'Evolution-Three': '',
                            'Class': 'Plain',
                            'Current HP': 60, 'Move-One': 'Pound', 'Move-Two': 'Sing', 'Move-Three': 'Metronome',
                            'Move-Four': '',
                            'Location': 'Plain'},
               'vulpix': {'Evolution-One': 'Vulpix', 'Evolution-Two': 'Ninetales', 'Evolution-Three': '',
                          'Class': 'Plain',
                          'Current HP': 40, 'Move-One': 'Ember', 'Move-Two': 'Quick Attack', 'Move-Three': '',
                          'Move-Four': '',
                          'Location': 'Plain'},
               'ninetales': {'Evolution-One': 'Vulpix', 'Evolution-Two': 'Ninetales', 'Evolution-Three': '',
                             'Class': 'Plain',
                             'Current HP': 80, 'Move-One': 'Ember', 'Move-Two': 'Quick Attack',
                             'Move-Three': 'Confuse Ray',
                             'Move-Four': '', 'Location': 'Plain'},
               'jigglypuff': {'Evolution-One': 'Jigglypuff', 'Evolution-Two': 'Wigglytuff', 'Evolution-Three': '',
                              'Class': 'Plain', 'Current HP': 25, 'Move-One': 'Pound', 'Move-Two': 'Sing',
                              'Move-Three': '',
                              'Move-Four': '', 'Location': 'Plain'},
               'wigglytuff': {'Evolution-One': 'Jigglypuff', 'Evolution-Two': 'Wigglytuff', 'Evolution-Three': '',
                              'Class': 'Plain', 'Current HP': 50, 'Move-One': 'Pound', 'Move-Two': 'Sing',
                              'Move-Three': 'Body Slam', 'Move-Four': '', 'Location': 'Plain'},
               'meowth': {'Evolution-One': 'Meowth', 'Evolution-Two': 'Persian', 'Evolution-Three': '',
                          'Class': 'Plain',
                          'Current HP': 30, 'Move-One': 'Scratch', 'Move-Two': 'Growl', 'Move-Three': '',
                          'Move-Four': '',
                          'Location': 'Plain'},
               'persian': {'Evolution-One': 'Meowth', 'Evolution-Two': 'Persian', 'Evolution-Three': '',
                           'Class': 'Plain',
                           'Current HP': 50, 'Move-One': 'Scratch', 'Move-Two': 'Growl', 'Move-Three': 'Bite',
                           'Move-Four': '',
                           'Location': 'Plain'},
               'dragonite': {'Evolution-One': 'Dratini', 'Evolution-Two': 'Dragonair', 'Evolution-Three': 'Dragonite',
                             'Class': 'Dragon', 'Current HP': 130, 'Move-One': 'Dragon Claw', 'Move-Two': 'Fly',
                             'Move-Three': 'Hyper Beam', 'Move-Four': 'Thunder Punch', 'Location': 'Plain'},
               'aerodactyl': {'Evolution-One': 'Aerodactyl', 'Evolution-Two': '', 'Evolution-Three': '',
                              'Class': 'Rock',
                              'Current HP': 130, 'Move-One': 'Ancient Power', 'Move-Two': 'Wing Attack',
                              'Move-Three': 'Bite',
                              'Move-Four': 'Crunch', 'Location': 'Plain'},
               'zapdos': {'Evolution-One': 'Zapdos', 'Evolution-Two': '', 'Evolution-Three': '', 'Class': 'Legendary',
                          'Current HP': 200, 'Move-One': 'Thunderbolt', 'Move-Two': 'Thunder', 'Move-Three': 'Fly',
                          'Move-Four': '', 'Location': 'Plain'}}
    return pokemon


import json

from moves import get_moves


# def dump_dict(func, file):
#     with open(file, "w") as json_file:
#         json.dump(func, json_file)
#
#
# dump_dict(get_moves(), "moves.json")
# dump_dict(mine_pokemon(), "../json_data/mine_pokemon.json")
# dump_dict(ocean_pokemon(), "../json_data/ocean_pokemon.json")
# dump_dict(starter_pokemon_dict(), "../json_data/starter_pokemon.json")
# dump_dict(volcano_pokemon(), "../json_data/volcano_pokemon.json")


def check_moves():
    moves = []
    for move in list(get_moves()):
        moves.append(move.lower())
    pokemon_values = []
    unregistered_moves = set()
    for pokemon in starter_pokemon_dict().values():
        pokemon_values.append(pokemon)
    for pokemon in forest_pokemon().values():
        pokemon_values.append(pokemon)
    for pokemon in ocean_pokemon().values():
        pokemon_values.append(pokemon)
    for pokemon in mine_pokemon().values():
        pokemon_values.append(pokemon)
    for pokemon in plains_pokemon().values():
        pokemon_values.append(pokemon)
    for pokemon in volcano_pokemon().values():
        pokemon_values.append(pokemon)
    for poke_dict in pokemon_values:
        if poke_dict['Move-One'].lower() not in moves:
            unregistered_moves.add(poke_dict['Move-One'])
        if poke_dict['Move-Two'].lower() not in moves:
            unregistered_moves.add(poke_dict['Move-Two'])
        if poke_dict['Move-Three'].lower() not in moves:
            unregistered_moves.add(poke_dict['Move-Three'])
        if poke_dict['Move-Four'].lower() not in moves:
            unregistered_moves.add(poke_dict['Move-Four'])
    print(unregistered_moves)


# check_moves()




