import random

def main():
    hercules, troll, gryphon, rous = make_creatures()
    # print (hercules["health"])


def make_creatures():
    hercules = {"health":100, "att_power": 25, "attacks":["Punch", "Headbutt", "Kick", "Stern Gaze"]}
    troll = {"health":150, "att_power": 5, "attacks":["Grunt", "Throw Club", "Bash", "Step"]}
    gryphon = {"health":50, "att_power": 15, "attacks":["Slash", "Kick", "Bite", "Tackle"]}
    rodent_of_unusual_size = {"health":20, "att_power": 3, "attacks":["Bite", "Chew", "Gnaw", "Nibble"]}
    return hercules, troll, gryphon, rodent_of_unusual_size

def battle_monster(hercules, monster):
    while hercules["health"] > 0 and troll["health"] > 0: #Herc always wins, right now
        att_choice = hercules["attacks"][offer_att_option()]
        print (f"Hercules attacks troll with {att_choice} for 25 damage!")
        troll["health"] -= 25
        if troll["health"] > 0:
            troll_attack = troll["attacks"][random.randint(0, 3)]
            print (f"Troll attacks Hercules with {troll_attack} for 5 damage!")
            hercules["health"] -= 25

def offer_att_option(hercules):
    for i, attack in enumerate(hercules["attacks"], 1):
        print(f"{i}: {attack}")
    user_choice = int(input("Which attack should Hercules use? ")) - 1
    return user_choice

main()