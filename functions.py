from random import randint
from copy import deepcopy
number_of_boats = 5
grid = [['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
        [1, '', '', '', '', '', '', '', ''],
        [2, '', '', '', '', '', '', '', ''],
        [3, '', '', '', '', '', '', '', ''],
        [4, '', '', '', '', '', '', '', ''],
        [5, '', '', '', '', '', '', '', ''],
        [6, '', '', '', '', '', '', '', ''],
        [7, '', '', '', '', '', '', '', ''],
        [8, '', '', '', '', '', '', '', ''], ]
reference = "ABCDEFGH"


def menu():
    print("Please enter a number")
    print("""				1 for a new game \n
				2 to resume your game \n
				3 to see the instructions \n
				4 to quit""")
    decision = input()
    if decision == "1":
        new_game()
    elif decision == "2":
        resume_game()
    elif decision == "3":
        instructions()
    else:
        return None


def instructions():
    instructions = open("instructions.txt", "r")
    print(instructions.read())
    instructions.close()


def new_game():
    player_grid = deepcopy(grid)
    computer_grid = deepcopy(grid)
    display_grid(player_grid)
    hm_grid = deepcopy(grid)
    display_grid(hm_grid)
    player_hits = 0
    computer_hits = 0
    player_turn = True
    player_targetted = []
    computer_targetted = []
    game_data = [player_grid, computer_grid, player_turn, hm_grid,
                 player_hits, computer_hits, player_targetted, computer_targetted]

    i = 0
    while i < number_of_boats:
        print(
            f"Please enter the coordinates of boat number {i + 1} in the format A1")
        coordinates = input()
        if player_grid[int(coordinates[1])][reference.index(coordinates[0]) + 1] == '':
            player_grid[int(coordinates[1])][reference.index(
                coordinates[0]) + 1] = 'B'
            display_grid(player_grid)
            i += 1
        else:
            print("Please enter unused coordinates")

    j = 0
    while j < number_of_boats:
        random_num = randint(1, 8)
        random_letter = randint(1, 8)
        if computer_grid[random_letter][random_num] == '':
            computer_grid[random_letter][random_num] = 'B'
            j += 1
    play_game(game_data)


def play_game(game_data):
    hm_grid = game_data[3]
    display_grid(hm_grid)
    player_hits = game_data[4]
    computer_hits = game_data[5]
    player_turn = game_data[2]
    player_targetted = game_data[6]
    computer_targetted = game_data[7]
    player_grid = game_data[0]
    computer_grid = game_data[1]

    save_game(game_data)

    while player_hits < 5 and computer_hits < 5:
        if player_turn == True:
            print("Enter target coordinates in the format A1")
            target = input()
            while target in player_targetted:
                print("Please enter unused coordinates")
                target = input()

            player_targetted.append(target)

            if computer_grid[int(target[1])][reference.index(target[0]) + 1] == 'B':
                hm_grid[int(target[1])][reference.index(target[0]) + 1] = 'H'
                player_hits += 1
                display_grid(hm_grid)
                print("Hit!")
            else:
                hm_grid[int(target[1])][reference.index(target[0]) + 1] = 'M'
                display_grid(hm_grid)

            player_turn = False

        else:
            random_num = randint(1, 8)
            random_letter = randint(1, 8)
            target = str(random_num) + str(random_letter)

            while target in computer_targetted:
                random_num = randint(1, 8)
                random_letter = randint(1, 8)
                target = str(random_num) + str(random_letter)

            player_targetted.append(target)

            if player_grid[random_num][random_letter] == 'B':
                computer_hits += 1
                print("One of your ships has been destroyed!")

            player_turn = True
            save_game(game_data)

    if player_hits == 5:
        print("You win!")
    else:
        print("You lose")


def resume_game():
    game_data = []
    vars = open("vars.txt", "r")

    for variable in vars:
        game_data.append(variable)

    vars.close()

    play_game(game_data)


def save_game(game_data):
    vars = open("vars.txt", "w")

    for variable in game_data:
        vars.write(variable)
        vars.write("\n")

    vars.close()


def display_grid(grid):
    for row in grid:
        print(row)
