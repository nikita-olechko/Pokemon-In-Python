
"""
['Splash', '', 'Bite', 'Dragon Rage', 'Hydro Pump', 'Dragon Breath', 'Agility', 'Thunder Wave', 'Aqua Tail',
'Ice Beam', 'Scratch', 'Water Gun', 'Ice Fang', 'Waterfall', 'Crunch', 'Superpower', 'Tackle', 'Mud Shot',
'Mud Bomb', 'Earthquake', 'Rock Slide', 'SmokeScreen', 'Agility', 'Vine Whip', 'Poison Sting', 'Agility',
'Fury Attack', 'Focus Energy', 'Gust', 'Quick Attack', 'Sand Attack', 'Wing Attack', 'Sky Attack', 'Feather Dance',
'Hyper Fang', 'Super Fang', 'Giant Bite', 'Wrap', 'Acid Shot', 'Thunder Shock', 'Thunderbolt', 'Slam', 'Double-Edge',
'Flash', 'Thunder', 'Growl', 'Roar', 'Bubble', 'Bubble Beam', 'Screech', 'Hydro Pump', 'Agility',
'Mirror Move', 'Drill Peck', 'Submission', 'Low Kick', 'Seismic Toss', 'Mega Punch', 'Mega Kick', 'Counter',
'Strength', 'Karate Chop', 'Fissure', 'Dig', 'Sonic Boom',
'Rock Throw', 'Earthquake', 'Fire Punch', 'Ice Punch', 'Thunder Punch', 'Fly']
"""

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

