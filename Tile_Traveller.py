# Unnar Sigurðsson

# Variables
position = "a"
error_not_valid_messasge = "Not a valid direction!"
error_code = 0


# Movement function
def movement(a_str):
    global error_code
    if error_code == 0:
        if a_str == "a":
            print("You can travel: (N)orth.")
        elif a_str == "b":
            print("You can travel: (N)orth.")
        elif a_str == "c":
            print("You can travel: (N)orth.")
        elif a_str == "d":
            print("You can travel: (N)orth or (E)ast or (S)outh.")
        elif a_str == "e":
            print("You can travel: (S)outh or (W)est.")
        elif a_str == "f":
            print("You can travel: (N)orth or (S)outh.")
        elif a_str == "g":
            print("You can travel: (E)ast or (S)outh.")
        elif a_str == "h":
            print("You can travel: (E)ast or (W)est.")
        elif a_str == "i":
            print("You can travel: (S)outh or (W)est.")
    elif error_code == 1:
        error_code = 0

    return


# Movement_input function
def movement_input():
    a_str = str(input("Direction: "))
    return a_str


# Tiles
def tiletraveller(player_choice, position):
    global error_code

    # The grid:
    # g h i
    # d e f
    # a b c 

    a = "nN"
    b = "nN"
    d_a, d_b, d_c = "nN", "sS", "eE"
    e_a, e_b = "sS", "wW"
    f_a, f_b = "nN", "sS"
    g_a, g_b = "sS", "eE"
    h_a, h_b = "eE", "wW"
    i_a, i_b = "sS", "wW"

    
    if position == "a":                             # a liður
        if a.count(player_choice) >= 1:
            position = "d"
            return position
        else:
            print(error_not_valid_messasge)
            error_code = 1
    if position == "d":                             # d liður
        if d_a.count(player_choice) >= 1:
            position = "g"
            return position
        elif d_b.count(player_choice) >= 1:
            position = "a"
            return position
        elif d_c.count(player_choice) >= 1:
            position = "e"
            return position
        else:
            print(error_not_valid_messasge)
            error_code = 1
    if position == "g":                             # g liður
        if g_a.count(player_choice) >= 1:
            position = "d"
            return position
        elif g_b.count(player_choice) >= 1:
            position = "h"
            return position
        else:
            print(error_not_valid_messasge)
            error_code = 1
    if position == "h":                             # h liður
        if h_a.count(player_choice) >= 1:
            position = "i"
            return position
        elif h_b.count(player_choice) >= 1:
            position = "g"
            return position
        else:
            print(error_not_valid_messasge)
            error_code = 1
    if position == "i":                             # i liður
        if i_a.count(player_choice) >= 1:
            position = "f"
            return position
        elif i_b.count(player_choice) >= 1:
            position = "h"
            return position
        else:
            print(error_not_valid_messasge)
            error_code = 1
    if position == "f":                             # f liður
        if f_a.count(player_choice) >= 1:
            position = "i"
            return position
        elif f_b.count(player_choice) >= 1:
            position = "c"
            return position
        else:
            print(error_not_valid_messasge)
            error_code = 1
    if position == "b":                             # b liður
        if b.count(player_choice) >= 1:
            position = "e"
            return position
        else:
            print(error_not_valid_messasge)
            error_code = 1
    if position == "e":                             # e liður
        if e_a.count(player_choice) >= 1:
            position = "b"
            return position
        elif e_b.count(player_choice) >= 1:
            position = "d"
            return position
        else:
            print(error_not_valid_messasge)
            error_code = 1
 
    return position



while True:
    movement(position)
    a_input = movement_input()
    position = tiletraveller(a_input, position)
    if position == "c":
        print("Victory!")
        break
    






