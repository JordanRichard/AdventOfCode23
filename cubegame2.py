with open('input.txt') as fp:


    #   Build list formatted input data in memory
    linelist = []
    data = {}
    powers = []


    for line in fp.readlines():
        newline = (line.strip("\n")).split(": ")
        data[newline[0].replace("Game ","")] = newline[1]

    #   For each game
    for game_id, game_data in data.items():

        game_data = game_data.split("; ")

        #   Set new minimums for this game
        game_minimums = {'red':0,'green':0,'blue':0}


        #   For each round in each game
        for game_round in game_data:

            game_round = game_round.split(", ")
            round_totals = {'red':0,'green':0,'blue':0}

            #   For each "draw" in each round
            for round_contents in game_round:
                round_contents = round_contents.split(" ")

                #   Add this draw to the round count
                round_totals[round_contents[1]] += int(round_contents[0])

                #   Update color minimum if we found a new lower number
                if int(round_totals[round_contents[1]]) > game_minimums[round_contents[1]]:
                    game_minimums[round_contents[1]] = int(round_totals[round_contents[1]])

        #   Add the power of this game to the list
        powers.append(game_minimums['red'] * game_minimums['blue'] * game_minimums['green'])

    print(sum(powers))
    