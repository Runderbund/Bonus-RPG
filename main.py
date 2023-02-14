"""
At the moment, this is completely deterministic. Hercules wins every time,
attacks have no range of damage, etc.
I could make it branch, show health remaining, etc., but that's extra, and I'd want
to use classes if I were going to expand the capabilities of this.
"""

import random

def main():
    tell_story()

def make_creatures():
    hercules = {"health":100, "att_power": 25, "attacks":["Punch", "Headbutt", "Kick", "Stern Gaze"]}
    troll = {"health":100, "att_power": 5, "attacks":["Grunt", "Throw Club", "Bash", "Step"], "name":"troll"}
    gryphon = {"health":50, "att_power": 15, "attacks":["Slash", "Kick", "Bite", "Tackle"],"name":"gryphon"}
    rodent_of_unusual_size = {"health":20, "att_power": 3, "attacks":["Bite", "Chew", "Gnaw", "Nibble"], "name":"Rodent of Unusual Size"}
    # I'm assuming it's fine to add a name to the dictionary
    return hercules, troll, gryphon, rodent_of_unusual_size

def battle_monster(hercules, monster):
    while hercules["health"] > 0 and monster["health"] > 0:
        hercules_attack(hercules, monster)
        if monster["health"] > 0:
            monster_attack(hercules, monster)
        
def offer_att_option(hercules):
    print ("\nHercules' attacks:")
    for i, attack in enumerate(hercules["attacks"], 1):
        print(f"{i}: {attack}")
    user_choice = int(input("\nWhich attack should Hercules use? ")) - 1
    return user_choice

def hercules_attack(hercules, monster):
    attack_choice = hercules["attacks"][offer_att_option(hercules)]
    print (f"\nHercules attacks the {monster['name']} with {attack_choice} for {hercules['att_power']} damage!")
        # Why can't I do "...attacks the {monster["name"]} with ..."
    monster["health"] -= hercules['att_power']

def monster_attack(hercules, monster):
    attack_choice = monster["attacks"][random.randint(0, 3)]
    print (f"The {monster['name']} attacks Hercules with {attack_choice} for {monster['att_power']} damage!")
    hercules["health"] -= monster['att_power']

def tell_story():
    hercules, troll, gryphon, rous = make_creatures()
    print ("Behold, the mighty Hercules sets forth on a mighty adventure!")
    
    print ("On his travels throughout the land, Hercules is accosted by a troll!")
    battle_monster(hercules, troll)
    print ("\nThe troll proves no match for Hercules!\n")

    print ("Upon climbing to the top of a mountain, Hercules is suddenly attacked by a flurry of feathers!")
    battle_monster(hercules, gryphon)
    print ("\nThe gryphon too falls under Hercules mighty swings.\n")

    print ("Finally, Hercules passes through the fire swamp, where a shadow lunges at him!")
    battle_monster(hercules, rous)
    print ("\nHercules smashes the rodent and proves why he need fear no creature.\n")

    print ("Victorious, Hercules grabs a gyro, and once again wonders why he put his icebox so far away.")

main()