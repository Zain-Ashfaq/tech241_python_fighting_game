import random

character_dict = {
    "Sorcerer":{"health":150,"damage":15},
    "Barbarian":{"health":80,"damage":30},
    "Rogue":{"health":120,"damage":25},
    "Necromancer":{"health":20,"damage":65},
    "Druid":{"health":50,"damage":15},

}
character_list_num=len(character_dict)
def player_name(num):

    if num==1:
        return input("Player 1: what is your name?")
    else:
        return input("Player 2: what is your name?")
def rand_character():
    random_character = random.choice(list(character_dict.keys()))

    random_character_stats = character_dict[random_character]
    char_list=[random_character,random_character_stats]

    # print("Random character:", random_character)
    # print("Health:", random_character_stats["health"])
    # print("Damage:", random_character_stats["damage"])

    return char_list

def print_character(char_list):
    character_name = char_list[0]
    character_stats = char_list[1]

    print("Character:", character_name)
    for stat, value in character_stats.items():
        print(f"{stat}: {value}")



def main():


    is_player_ones_turn = True
    # player_one_name = player_name(1)
    # player_two_name = player_name(2)
    # print(player_two_name,player_one_name)
    player_one_character=rand_character()
    player_two_character=rand_character()
    print("player one is:")
    print_character(player_one_character)
    print("\nplayer two is:")
    print_character(player_two_character)








main()