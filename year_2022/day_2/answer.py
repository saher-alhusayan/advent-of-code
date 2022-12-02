from input_data import rounds

# PREP DATA
rounds_ = rounds.split('\n')
list_of_rounds = [item.split(' ') for item in rounds_]

# PART 1
def determiine_if_player_two_wins(list_of_rounds: list[str]) -> bool:

    player_one = list_of_rounds[0]
    player_two = list_of_rounds[1]

    if player_one == "A" and player_two == "X":
        return 3 + 1

    if player_one == "A" and player_two == "Y":
        return 6 + 2

    if player_one == "A" and player_two == "Z":
        return 0 + 3
    
    if player_one == "B" and player_two == "X":
        return 0 + 1

    if player_one == "B" and player_two == "Y":
        return 3 + 2

    if player_one == "B" and player_two == "Z":
        return 6 + 3
    
    if player_one == "C" and player_two == "X":
        return 6 + 1

    if player_one == "C" and player_two == "Y":
        return 0 + 2

    if player_one == "C" and player_two == "Z":
        return 3 + 3

outcome = list(map(determiine_if_player_two_wins, list_of_rounds))

print(sum(outcome))

# PART 2
