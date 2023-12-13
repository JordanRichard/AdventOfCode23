with open('input.txt') as fp:


    #   Build list formatted input data in memory
    linelist = []
    data = {}
    valid = []
    maxes= {'red': 12,'green': 13,'blue': 14}

    for i in range(1,101):
        valid.append(i)

    for line in fp.readlines():
        newline = (line.strip("\n")).split(": ")
        data[newline[0].replace("Game ","")] = newline[1]

    #   For each game
    for game_id, game_data in data.items():

        game_data = game_data.split("; ")

        #   For each round in each game
        for game_round in game_data:

            game_round = game_round.split(", ")
            round_totals = {'red':0,'green':0,'blue':0}

            #   For each "draw" in each round
            for round_contents in game_round:
                round_contents = round_contents.split(" ")

                #   Add this draw to the round count
                round_totals[round_contents[1]] += int(round_contents[0])

                #   check if max is exceeded
                if int(round_totals[round_contents[1]]) > maxes[round_contents[1]]:
                    if int(game_id) in valid:
                        valid.remove(int(game_id))
                    break

    print(sum(valid))
    