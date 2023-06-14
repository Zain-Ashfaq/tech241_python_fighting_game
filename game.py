from random import randint

character_dict = {
    "Sorcerer":{"health":150,"damage":15},
    "Barbarian":{"health":80,"damage":30},
    "Rogue":{"health":120,"damage":25},
    "Necromancer":{"health":20,"damage":65},
    "Druid":{"health":50,"damage":15},

}
def player_name(num):

    if num==1:
        return input("Player 1: what is your name?")
    else:
        return input("Player 2: what is your name?")

def main():
    is_player_ones_turn = True
    player_one_name = player_name(1)
    player_two_name = player_name(2)
    print(player_two_name,player_one_name)




main()