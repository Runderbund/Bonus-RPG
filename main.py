import random

def main():
    hercules, troll, gryphon, rous = make_creatures()
    tell_story(hercules, troll, gryphon, rous)

def make_creatures():
    hercules = {"health":100, "att_power": 25, "attacks":["Punch", "Headbutt", "Kick", "Stern Gaze"]}
    troll = {"health":100, "att_power": 5, "attacks":["Grunt", "Throw Club", "Bash", "Step"], "name":"troll"}
    gryphon = {"health":50, "att_power": 15, "attacks":["Slash", "Kick", "Bite", "Tackle"],"name":"gryphon"}
    rodent_of_unusual_size = {"health":20, "att_power": 3, "attacks":["Bite", "Chew", "Gnaw", "Nibble"], "name":"Rodent of Unusual size"}
    # I'm assuming it's fine to add a name to the dictionary
    return hercules, troll, gryphon, rodent_of_unusual_size

def battle_monster(hercules, monster):
    while hercules["health"] > 0 and monster["health"] > 0: #Herc always wins, right now
        hercules_attack(hercules, monster)
        monster_attack(hercules, monster)
        
def offer_att_option(hercules):
    print ("\nHercules' attacks:")
    for i, attack in enumerate(hercules["attacks"], 1):
        print(f"{i}: {attack}")
    user_choice = int(input("\nWhich attack should Hercules use? ")) - 1
    return user_choice

def hercules_attack(hercules, monster):
    att_choice = hercules["attacks"][offer_att_option(hercules)]
    att_power = hercules["att_power"]
    monster_name = monster["name"]
    print (f"\nHercules attacks {monster_name} with {att_choice} for {att_power} damage!")
    # Why can't I do "...attacks {monster["name"]} with ..."
    monster["health"] -= att_power

def monster_attack(hercules, monster):
    monster_name = monster["name"]
    att_power = monster["att_power"]
    if monster["health"] > 0:
        attack_choice = monster["attacks"][random.randint(0, 3)]
        print (f"The {monster_name} attacks Hercules with {attack_choice} for {att_power} damage!")
        hercules["health"] -= att_power

def tell_story(hercules, troll, gryphon, rous):
    print ("Behold, the mighty Hercules sets forth on a mighty adventure!")
    
    print ("On his travels throughout the land, Hercules is accosted by a troll!")
    battle_monster(hercules, troll)
    print ("\nThe troll proves no match for Hercules!\n")

    print ("Upon climbing to the top of a mountain, Hercules is suddenly attacked by a flurry of feathers!")
    battle_monster(hercules, gryphon)
    print ("\nThe gryphon too falls under Hercules mighty swings.\n")


    print ("Finally, Hercules passes through the fire swamp, where a shadow lunges at him!")
    battle_monster(hercules, rous)
    print ("\nHercules smashes the rodent and proves yet again that he fears no creature.\n")
    print ("Victorious, Hercules grabs a burrito, and once again wonders why he put his fridge so far away.")

main()