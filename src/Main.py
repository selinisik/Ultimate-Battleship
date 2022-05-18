
# Ultimate Battleships

def print_ships_to_be_placed():
    print("Ships to be placed:", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Ships to be placed: ")


# elem expected to be a single list element of a primitive type.
def print_single_element(elem):
    print(str(elem), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write(str(elem) + " ")


def print_empty_line():
    print()
    if FILE_OUTPUT_FLAG:
        f.write("\n")


# n expected to be str or int.
def print_player_turn_to_place(n):
    print("It is Player {}'s turn to place their ships.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to place their ships.\n".format(n))


def print_to_place_ships():
    print("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) : \n")
        # There is a \n because we want the board to start printing on the next line.


def print_incorrect_input_format():
    print("Input is in incorrect format, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Input is in incorrect format, please try again.\n")


def print_incorrect_coordinates():
    print("Incorrect coordinates given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect coordinates given, please try again.\n")


def print_incorrect_ship_name():
    print("Incorrect ship name given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect ship name given, please try again.\n")


def print_incorrect_orientation():
    print("Incorrect orientation given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect orientation given, please try again.\n")


# ship expected to be str.
def print_ship_is_already_placed(ship):
    print(ship, "is already placed, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " is already placed, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_outside(ship):
    print(ship, "cannot be placed outside the board, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed outside the board, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_occupied(ship):
    print(ship, "cannot be placed to an already occupied space, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed to an already occupied space, please try again.\n")


def print_confirm_placement():
    print("Confirm placement Y/N :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Confirm placement Y/N : \n")


# n expected to be str or int.
def print_player_turn_to_strike(n):
    print("It is Player {}'s turn to strike.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to strike.\n".format(n))


def print_choose_target_coordinates():
    print("Choose target coordinates :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Choose target coordinates : ")


def print_miss():
    print("Miss.")
    if FILE_OUTPUT_FLAG:
        f.write("Miss.\n")


# n expected to be str or int.
def print_type_done_to_yield(n):
    print("Type done to yield your turn to player {} :".format(n), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Type done to yield your turn to player {} : \n".format(n))


def print_tile_already_struck():
    print("That tile has already been struck. Choose another target.")
    if FILE_OUTPUT_FLAG:
        f.write("That tile has already been struck. Choose another target.\n")


def print_hit():
    print("Hit!")
    if FILE_OUTPUT_FLAG:
        f.write("Hit!\n")


# n expected to be str or int.
def print_player_won(n):
    print("Player {} has won!".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("Player {} has won!\n".format(n))


def print_thanks_for_playing():
    print("Thanks for playing.")
    if FILE_OUTPUT_FLAG:
        f.write("Thanks for playing.\n")


# my_list expected to be a 3-dimensional list, formed from two 2-dimensional lists containing the boards of each player.
def print_3d_list(my_list):
    first_d = len(my_list[0])
    for row_ind in range(first_d):
        second_d = len(my_list[0][row_ind])
        print("{:<2}".format(row_ind+1), end=' ')
        for col_ind in range(second_d):
            print(my_list[0][row_ind][col_ind], end=' ')
        print("\t\t\t", end='')
        print("{:<2}".format(row_ind+1), end=' ')
        for col_ind in range(second_d):
            print(my_list[1][row_ind][col_ind], end=' ')
        print()
    print("", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\t\t", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\nPlayer 1\t\t\t\t\t\tPlayer 2")
    print()

    if FILE_OUTPUT_FLAG:
        first_d = len(my_list[0])
        for row_ind in range(first_d):
            second_d = len(my_list[0][row_ind])
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[0][row_ind][col_ind] + " ")
            f.write("\t\t\t")
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[1][row_ind][col_ind] + " ")
            f.write("\n")
        f.write("   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\t\t   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\nPlayer 1\t\t\t\t\t\tPlayer 2\n")
        f.write("\n")


def print_rules():
    print("Welcome to Ultimate Battleships")
    print("This is a game for 2 people, to be played on two 10x10 boards.")
    print("There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).")
    print("First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.")
    print("Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.")
    print("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.")
    print("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.")
    print("Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.")
    print("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.")
    print("The last player to have an unsunk ship wins.")
    print("Have fun!")
    print()

    if FILE_OUTPUT_FLAG:
        f.write("Welcome to Ultimate Battleships\n")
        f.write("This is a game for 2 people, to be played on two 10x10 boards.\n")
        f.write(
            "There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).\n")
        f.write(
            "First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.\n")
        f.write(
            "Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.\n")
        f.write("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.\n")
        f.write("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.\n")
        f.write(
            "Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.\n")
        f.write("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.\n")
        f.write("The last player to have an unsunk ship wins.\n")
        f.write("Have fun!\n")
        f.write("\n")


# Create the game
board_size = 10
f = open('UltimateBattleships.txt', 'w')
FILE_OUTPUT_FLAG = True  # You can change this to True to also output to a file so that you can check your outputs with diff.

print_rules()

# Remember to use list comprehensions at all possible times.
# If we see you populate a list that could be done with list comprehensions using for loops, append/extend/insert etc. you will lose points.

# Make sure to put comments in your code explaining your approach and the execution.

# We defined all the functions above for your use so that you can focus only on your code and not the formatting.
# You need to call them in your code to use them of course.

# If you have questions related to this homework, direct them to utku.bozdogan@boun.edu.tr please.

# Do not wait until the last day or two to start doing this homework, it requires serious effort.

try:  # The entire code is in this try block, if there ever is an error during execution, we can safely close the file.
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    #Board that where all operations made
    main_board = [[["-" for x in range(board_size)] for i in range(board_size)],
                  [["-" for x in range(board_size)] for i in range(board_size)]]
    #Board that which is visible to the other player
    hit_board = [[["-" for x in range(board_size)] for i in range(board_size)],
                 [["-" for x in range(board_size)] for i in range(board_size)]]
    #Name of the ships
    ship_names = ["carrier", "battleship", "cruiser", "submarine", "destroyer"]
    #Sizes of the ships
    ship_sizes = {"carrier": 5, "battleship": 4, "cruiser": 3, "submarine": 3, "destroyer": 2}
    #List of unplaced ships for each player
    ship_list = [["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"],
                 ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]]

    game_continues = True
    current_player = 1
    turn = 0
    num_of_hits = {"1":0,"2":0}
    #Placement of ships occurs in this loop
    while turn < 2:
        while len(ship_list[turn]) != 0:
            if turn == 0:
                print_3d_list([main_board[0], hit_board[1]])
            else:
                print_3d_list([hit_board[0], main_board[1]])
            print_ships_to_be_placed()
            for ship in ship_list[turn]:
                print_single_element(ship)
            print_empty_line()
            print_player_turn_to_place(turn+1)
            print_to_place_ships()
            inp = input().split()
            x_coordinate = 0
            y_coordinate = 0
            # Checks the length of input
            if len(inp) != 4:
                print_incorrect_input_format()
                continue
            # Checks if the input type is correct
            try:
                x_coordinate = int(inp[1])
                y_coordinate = int(inp[2])
            except:
                print_incorrect_input_format()
                continue
            # Checks if the coordinates are valid
            if x_coordinate > 10 or y_coordinate > 10 or x_coordinate <= 0 or y_coordinate <= 0:
                print_incorrect_coordinates()
                continue
            # Checks if the ship name is valid
            if inp[0].lower() in ship_names:
                pass
            else:
                print_incorrect_ship_name()
                continue
            # Checks if the ship is used
            if inp[0].lower().capitalize() not in ship_list[turn]:
                print_ship_is_already_placed(inp[0].lower().capitalize())
            #Checks if the direction is valid
            if inp[3].lower() in ("h", "v"):
                pass
            else:
                print_incorrect_orientation()
                continue
            #Places the ships
            if inp[0].lower().capitalize() in ship_list[turn]:
                ship_name = inp[0].lower()
                place_the_ship = True
                ship_len = ship_sizes[ship_name]
                length = 0
                if inp[3] == "h":
                    # Checks if the ship will be out of board
                    if x_coordinate + ship_len - 1 > 10:
                        print_ship_cannot_be_placed_outside(ship_name.capitalize())
                        place_the_ship = False
                        continue
                    for i in range(ship_len):
                        # Checks if the place is occupied
                        if main_board[turn][y_coordinate - 1][x_coordinate - 1 + i] != "-":
                            print_ship_cannot_be_placed_occupied(ship_name.capitalize())
                            place_the_ship = False
                            break
                    # Places the ship
                    while place_the_ship:
                        if length == ship_len:
                            break
                        main_board[turn][y_coordinate - 1][x_coordinate - 1 + length] = "#"
                        length += 1
                else:
                    if y_coordinate + ship_len - 1 > 10:
                        print_ship_cannot_be_placed_outside(ship_name.capitalize())
                        place_the_ship = False
                        continue

                    for i in range(ship_len):
                        if main_board[turn][y_coordinate - 1 + i][x_coordinate - 1] != "-":
                            print_ship_cannot_be_placed_occupied(ship_name.capitalize())
                            place_the_ship = False
                            break
                    while place_the_ship:
                        if length == ship_len:
                            break
                        main_board[turn][y_coordinate - 1 + length][x_coordinate - 1] = "#"
                        length += 1
                if place_the_ship:
                    ship_list[turn].remove(ship_name.capitalize())
        # Prints the boards
        if turn == 0:
            print_3d_list([main_board[0], hit_board[1]])
        else:
            print_3d_list([hit_board[0], main_board[1]])

        a = True
        while a:
            print_confirm_placement()
            ans = input().lower()
            if ans == "n":
                for i in range(board_size):
                    for j in range(board_size):
                        main_board[turn][i][j] = "-"
                ship_list[turn] = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
                a = False
            elif ans == "y":
                turn += 1
                a = False
            else:
                pass
    # The loop which the game is played
    while game_continues:
        x_coordinate = 0
        y_coordinate = 0
        if current_player == 1:
            print_3d_list([main_board[0], hit_board[1]])
        else:
            print_3d_list([hit_board[0], main_board[1]])
        print_player_turn_to_strike(current_player)
        print_choose_target_coordinates()
        inp = input().split()
        # Checks if the inputs are valid
        try:
            x_coordinate = int(inp[0])
            y_coordinate = int(inp[1])
        except:
            print_incorrect_input_format()
            continue
        # Checks if the inputs are in board
        if not (0 < x_coordinate < 11 and 0 < y_coordinate < 11):
            print_incorrect_coordinates()
            continue
        # Checks if the point has been shot
        if main_board[2-current_player][y_coordinate-1][x_coordinate-1] == "O" or main_board[2-current_player][y_coordinate-1][x_coordinate-1] == "!":
            print_tile_already_struck()
            continue
        # Shots the point
        if main_board[2-current_player][y_coordinate-1][x_coordinate-1] == "-":
            main_board[2 - current_player][y_coordinate - 1][x_coordinate - 1] = "O"
            hit_board[2 - current_player][y_coordinate - 1][x_coordinate - 1] = "O"
            print_miss()
            ps = True
            while(ps):
                print_type_done_to_yield(3-current_player)
                inpp = input()
                if inpp.lower() == "done":
                    ps = False
                    current_player = 3 - current_player
            continue
        # Shoots the point
        if main_board[2 - current_player][y_coordinate - 1][x_coordinate - 1] == "#":
            main_board[2 - current_player][y_coordinate - 1][x_coordinate - 1] = "!"
            hit_board[2 - current_player][y_coordinate - 1][x_coordinate - 1] = "!"
            num_of_hits[str(current_player)] +=1
            print_hit()
        # Checks if all the ships have been shot
        if num_of_hits[str(current_player)] == 17:
            game_continues = False
    print_3d_list(main_board)
    print_player_won(current_player)
    print_thanks_for_playing()

    # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
except:
    f.close()

