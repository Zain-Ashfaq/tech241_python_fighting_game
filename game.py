from random import randint


characters = [
    {"name": "Sorcerer", "health": 100, "damage": [10, 25]},
    {"name": "Barbarian", "health": 150, "damage": [5, 15]},
    {"name": "Rogue", "health": 80, "damage": [15, 20]},
    {"name": "Necromancer", "health": 120, "damage": [10, 20]},
    {"name": "Druid", "health": 90, "damage": [15, 25]}
]


def select_character(player_num):
    # Let the player select a character
    if player_num == 1:
        player_name = input("Player 1, enter your name: ")
        print(f"{player_name}, select your character:")
    else:
        player_name = input("Player 2, enter your name: ")
        print(f"{player_name}, select your character:")

    choice = None
    while not choice:
        for i in range(len(characters)):
            character = characters[i]
            print(
                f"{i + 1}. {character['name']} (Health: {character['health']}, Damage: {character['damage'][0]}-{character['damage'][1]})")

        choice = int(input("Enter the number of your choice: "))

        if 1 <= choice <= len(characters):
            return {"player_name": player_name, "character": characters[choice - 1]}
        else:
            print("Invalid choice. Please try again.")
            choice = None


def fight(player1, player2):
    print(player1," SIUUUU")

    print(
        f"{player1['player_name']} ({player1['character']['name']}) and {player2['player_name']} ({player2['character']['name']}) are fighting!")

    # get the health and damage values for each player
    player1_health = player1['character']['health']
    player1_damage = player1['character']['damage']
    player2_health = player2['character']['health']
    player2_damage = player2['character']['damage']


    while player1_health > 0 and player2_health > 0:


        input("Press Enter to continue...")
        player1_attack = randint(player1_damage[0], player1_damage[1])
        player2_health -= player1_attack
        print(
            f"{player1['player_name']} ({player1['character']['name']}) attacks {player2['player_name']} ({player2['character']['name']}) for {player1_attack} damage. {player2['player_name']}'s health: {player2_health}")

        # check if player 2 is dead
        if player2_health <= 0:
            print(f"{player2['player_name']} ({player2['character']['name']}) is dead")
            break


        input("Press any key to continue")
        player2_attack = randint(player2_damage[0], player2_damage[1])
        player1_health -= player2_attack
        print(
            f"{player2['player_name']} ({player2['character']['name']}) attacks {player1['player_name']} ({player1['character']['name']}) for {player2_attack} damage. {player1['player_name']}'s health: {player1_health}")


        if player1_health <= 0:
            print(f"{player1['player_name']} ({player1['character']['name']}) is dead")

    if player1_health < 0:
        player1_health = 0
    if player2_health < 0:
        player2_health = 0
    # determine who won
    if player1_health > player2_health:
        print(f"The winner is {player1['player_name']} ({player1['character']['name']})")
    else:
        print(f"The winner is {player2['player_name']} ({player2['character']['name']})")


# main game loop
def main():
    while True:
        print("Choose your fighters")
        player1 = select_character(1)
        player2 = select_character(2)
        fight(player1, player2)

        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != "y":
            break


main()