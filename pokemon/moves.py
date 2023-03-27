
def moves():
    splash = {"Damage": 0, "Message": " splashes around, nothing happens.", "SuperEffect": "Volcano"}
    empty = {"Damage": 0, "Message": " did nothing.", "SuperEffect": "Grass"}
    bite = {"Damage": 60, "Message": " bites the opponent.", "SuperEffect": "Normal"}
    dragon_rage = {"Damage": 80, "Message": " hits the opponent with Dragon Rage.", "SuperEffect": "Dragon"}
    hydro_pump = {"Damage": 110, "Message": " hits the opponent with Hydro Pump.", "SuperEffect": "Water"}
    dragon_breath = {"Damage": 60, "Message": " hits the opponent with Dragon Breath.", "SuperEffect": "Dragon"}
    agility = {"Damage": 0, "Message": " uses Agility and sharply raises its speed.", "SuperEffect": "Psychic"}
    thunder_wave = {"Damage": 0, "Message": " paralyzes the opponent with Thunder Wave.", "SuperEffect": "Electric"}
    aqua_tail = {"Damage": 90, "Message": " hits the opponent with Aqua Tail.", "SuperEffect": "Water"}
    ice_beam = {"Damage": 90, "Message": " hits the opponent with Ice Beam.", "SuperEffect": "Ice"}
    scratch = {"Damage": 40, "Message": " scratches the opponent.", "SuperEffect": "Normal"}
    water_gun = {"Damage": 40, "Message": " hits the opponent with Water Gun.", "SuperEffect": "Water"}
    ice_fang = {"Damage": 65, "Message": " bites the opponent with Ice Fang.", "SuperEffect": "Ice"}
    waterfall = {"Damage": 80, "Message": " hits the opponent with Waterfall.", "SuperEffect": "Water"}
    crunch = {"Damage": 80, "Message": " hits the opponent with Crunch.", "SuperEffect": "Dark"}
    superpower = {"Damage": 120, "Message": " hits the opponent with Superpower.", "SuperEffect": "Fighting"}
    tackle = {"Damage": 40, "Message": " tackles the opponent.", "SuperEffect": "Normal"}
    mud_shot = {"Damage": 55, "Message": " hits the opponent with Mud Shot.", "SuperEffect": "Ground"}
    mud_bomb = {"Damage": 65, "Message": " hits the opponent with Mud Bomb.", "SuperEffect": "Ground"}
    earthquake = {"Damage": 100, "Message": " causes an earthquake and hits the opponent.", "SuperEffect": "Ground"}
    rock_slide = {"Damage": 75, "Message": " hits the opponent with Rock Slide.", "SuperEffect": "Rock"}
    smokescreen = {"Damage": 0, "Message": " creates a smokescreen and sharply lowers the opponent's accuracy.",
                   "SuperEffect": "Normal"}
    vine_whip = {"Damage": 45, "Message": " hits the opponent with Vine Whip.", "SuperEffect": "Grass"}
    poison_sting = {"Damage": 15, "Message": " hits the opponent with Poison Sting.", "SuperEffect": "Poison"}
    fury_attack = {"Damage": 15, "Message": " hits the opponent with a a series of attacks.", "SuperEffect": "Normal"}
    gust = {"Damage": 40, "Message": " whips up a gust!", "SuperEffect": "Fighting"}
    quick_attack = {"Damage": 40, "Message": " quickly strikes!", "SuperEffect": "Ghost"}
    sand_attack = {"Damage": 0, "Message": " kicks sand!", "SuperEffect": "Flying"}
    wing_attack = {"Damage": 60, "Message": " flaps its wings!", "SuperEffect": "Grass"}
    sky_attack = {"Damage": 140, "Message": " charges up for a turn then swoops down with great force!",
                  "SuperEffect": "Fighting"}
    feather_dance = {"Damage": 0, "Message": " dances gracefully, its feathers drifting down around it.",
                     "SuperEffect": "Fighting"}
    hyper_fang = {"Damage": 80, "Message": " bites down with hyper fangs!", "SuperEffect": "Psychic"}
    super_fang = {"Damage": 80, "Message": " bites down with super fangs!", "SuperEffect": "Psychic"}
    giant_bite = {"Damage": 60, "Message": " takes a huge bite out of its opponent!", "SuperEffect": "Psychic"}
    wrap = {"Damage": 15, "Message": " wraps its opponent tightly!", "SuperEffect": "Flying"}
    acid_shot = {"Damage": 40, "Message": " shoots acid at its opponent!", "SuperEffect": "Grass"}
    thunder_shock = {"Damage": 40, "Message": " shocks its opponent with electricity!", "SuperEffect": "Water"}
    thunderbolt = {"Damage": 90, "Message": " strikes its opponent with a powerful bolt of electricity!",
                   "SuperEffect": "Water"}
    slam = {"Damage": 80, "Message": " slams into its opponent!", "SuperEffect": "Fighting"}
    double_edge = {"Damage": 120, "Message": " slams into its opponent with reckless abandon!",
                   "SuperEffect": "Fighting"}
    flash = {"Damage": 0, "Message": " blinds its opponent with a bright flash!", "SuperEffect": "Fighting"}
    thunder = {"Damage": 110, "Message": " summons a thunderstorm to strike its opponent!", "SuperEffect": "Water"}
    growl = {"Damage": 0, "Message": " growls menacingly.", "SuperEffect": "Normal"}
    roar = {"Damage": 0, "Message": " lets out a mighty roar!", "SuperEffect": "Normal"}
    bubble = {"Damage": 40, "Message": " blows bubbles at its opponent!", "SuperEffect": "Electric"}
    withdraw = {"Damage": 0, "Message": " withdraws into its shell!", "SuperEffect": "Rock"}
    bubble_beam = {"Damage": 65, "Message": " blasts its opponent with a powerful beam of bubbles!",
                   "SuperEffect": "Electric"}
    screech = {"Damage": 0, "Message": " lets out a piercing screech!", "SuperEffect": "Normal"}
    hydro_pump = {"Damage": 110, "Message": " blasts its opponent with a powerful jet of water!", "SuperEffect": "Fire"}
    agility = {"Damage": 0, "Message": " speeds up! You have more time to dodge.", "SuperEffect": "Electric"}
    mirror_move = {"Damage": 0, "Message": " copies its opponent's last move!", "SuperEffect": "Flying"}
    drill_peck = {"Damage": 80, "Type": "Flying", "Category": "Physical", "Accuracy": 100,
                  "Message": " uses Drill Peck!", "SuperEffect": "Grass", "NotEffective": "Steel"}
    submission = {"Damage": 80, "Type": "Fighting", "Category": "Physical", "Accuracy": 80,
                  "Message": " uses Submission!", "SuperEffect": "Normal",
                  "NotEffective": "Flying, Poison, Bug, Psychic, Fairy"}
    low_kick = {"Damage": 0, "Type": "Fighting", "Category": "Physical", "Accuracy": 100,
                "Message": " uses Low Kick!", "SuperEffect": "Ice, Rock, Steel", "NotEffective": "Ghost"}
    seismic_toss = {"Damage": 0, "Type": "Fighting", "Category": "Physical", "Accuracy": 100,
                    "Message": " uses Seismic Toss!", "SuperEffect": "Normal", "NotEffective": "Ghost"}
    mega_punch = {"Damage": 80, "Type": "Normal", "Category": "Physical", "Accuracy": 85,
                  "Message": " uses Mega Punch!", "SuperEffect": "Rock, Steel, Ice", "NotEffective": "Ghost"}
    mega_kick = {"Damage": 120, "Type": "Normal", "Category": "Physical", "Accuracy": 75,
                 "Message": " uses Mega Kick!", "SuperEffect": "Rock, Steel, Ice", "NotEffective": "Ghost"}
    counter = {"Damage": "2x", "Type": "Fighting", "Category": "Physical", "Accuracy": 100,
               "Message": " uses Counter!", "SuperEffect": "Normal",
               "NotEffective": "Flying, Poison, Bug, Psychic, Fairy"}
    strength = {"Damage": 80, "Type": "Normal", "Category": "Physical", "Accuracy": 100,
                "Message": " uses Strength!", "SuperEffect": "Rock, Steel, Ice", "NotEffective": "Ghost"}
    karate_chop = {"Damage": 50, "Type": "Fighting", "Category": "Physical", "Accuracy": 100,
                   "Message": " uses Karate Chop!", "SuperEffect": "Normal, Rock, Steel, Ice, Dark",
                   "NotEffective": "Flying, Poison, Bug, Psychic, Fairy"}
    fissure = {"Damage": "OHKO", "Type": "Ground", "Category": "Physical", "Accuracy": 30,
               "Message": " uses Fissure!", "SuperEffect": "Electric, Fire, Poison, Rock, Steel",
               "NotEffective": "Flying"}
    dig = {"Damage": 80, "Type": "Ground", "Category": "Physical", "Accuracy": 100,
           "Message": " digs underground and uses Dig!", "SuperEffect": "Electric, Fire, Poison, Rock, Steel",
           "NotEffective": "Flying"}
    sonic_boom = {"Damage": 20, "Type": "Normal", "Category": "Special", "Accuracy": 90,
                  "Message": " uses Sonic Boom!", "SuperEffect": "N/A", "NotEffective": "N/A"}
    rock_throw = {"Damage": 50, "Type": "Rock", "Category": "Physical", "Accuracy": 90,
                  "Message": " uses Rock Throw!", "SuperEffect": "Bug, Fire, Flying, Ice",
                  "NotEffective": "Fighting, Ground, Steel"}
    earthquake = {"Damage": 100, "Type": "Ground", "Category": "Physical", "Accuracy": 100,
                  "PP": 10, "Message": " caused an earthquake!"}

    fire_punch = {"Damage": 75, "Type": "Fire", "Category": "Physical", "Accuracy": 100,
                  "PP": 15, "Message": " hit with a fiery punch!", "Effect": "Burn", "EffectRate": 10}

    ice_punch = {"Damage": 75, "Type": "Ice", "Category": "Physical", "Accuracy": 100,
                 "PP": 15, "Message": " hit with an icy punch!", "Effect": "Freeze", "EffectRate": 10}

    thunder_punch = {"Damage": 75, "Type": "Electric", "Category": "Physical", "Accuracy": 100,
                     "PP": 15, "Message": " hit with an electric punch!", "Effect": "Paralyze", "EffectRate": 10}

    fly = {"Damage": 90, "Type": "Flying", "Category": "Physical", "Accuracy": 95,
           "PP": 15, "Message": " took to the skies and dove down with great force!"}
    return splash, empty, bite, dragon_rage, dragon_breath, agility, thunder_wave, aqua_tail, ice_beam, \
        scratch, water_gun, ice_fang, waterfall, crunch, superpower, tackle, mud_shot, mud_bomb, earthquake, \
        rock_slide, smokescreen, vine_whip, poison_sting, fury_attack, gust, quick_attack, sand_attack, wing_attack, \
        sky_attack, feather_dance, hyper_fang, super_fang, giant_bite, wrap, acid_shot, thunder_shock, thunderbolt, \
        slam, double_edge, flash, thunder, fire_punch, ice_punch, thunder_punch, fly, rock_throw, sonic_boom, \
        dig, fissure, karate_chop, strength, counter, mega_kick, mega_punch, seismic_toss, mirror_move, submission, \
        low_kick, drill_peck, screech, bubble, bubble_beam, withdraw, roar, growl, agility, earthquake, hydro_pump
