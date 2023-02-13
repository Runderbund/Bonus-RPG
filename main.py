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

def battle_troll():
    pass

main()