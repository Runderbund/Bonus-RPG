import random

def main():
    hercules, troll, gryphon, rous = make_creatures()
    battle_monster(hercules, troll)
    # print (hercules["health"])


def make_creatures():
    hercules = {"health":100, "att_power": 125, "attacks":["Punch", "Headbutt", "Kick", "Stern Gaze"]}
    troll = {"health":150, "att_power": 5, "attacks":["Grunt", "Throw Club", "Bash", "Step"]}
    gryphon = {"health":50, "att_power": 15, "attacks":["Slash", "Kick", "Bite", "Tackle"]}
    rodent_of_unusual_size = {"health":20, "att_power": 3, "attacks":["Bite", "Chew", "Gnaw", "Nibble"]}
    return hercules, troll, gryphon, rodent_of_unusual_size

def battle_monster(hercules, monster):
    while hercules["health"] > 0 and monster["health"] > 0: #Herc always wins, right now
        hercules_attack(hercules, monster)
        monster_attack(hercules, monster)
        

def offer_att_option(hercules):
    print ("\nHercules' attacks:")
    for i, attack in enumerate(hercules["attacks"], 1):
        print(f"{i}: {attack}")
    user_choice = int(input("Which attack should Hercules use? ")) - 1
    return user_choice

def hercules_attack(hercules, monster):
    att_choice = hercules["attacks"][offer_att_option(hercules)]
    att_power = hercules["att_power"]
    print (f"\nHercules attacks monster with {att_choice} for {att_power} damage!")
    # Not sure how to print dict name without overcomplicating this.
        # Leaving generic "monster" for now
    monster["health"] -= att_power

def monster_attack(hercules, monster):
    if monster["health"] > 0:
        attack_choice = monster["attacks"][random.randint(0, 3)]
        att_power = monster["att_power"]
        print (f"Monster attacks Hercules with {attack_choice} for {att_power} damage!")
        hercules["health"] -= att_power
    else:
        print ("Hercules has defeated the monster!")

main()