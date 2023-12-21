def check_winners(input):
    '''
        Checks for occurences of winning numbers in a line of input.

        Returns:    The value of this line based on winning number occurences.
    '''
    score = 0

    for i in input[1]:
        if i in input[0]:
            if score == 0:
                score = 1
            else:
                score *= 2

    return score


if __name__ == '__main__':

    input_data = []
    total = 0

    #   Feed input data into a 2d array
    with open('input.txt', encoding='utf-8') as fp:
        for line in fp.readlines():
            split = (line.strip("\n")).split(":")
            formatted = split[1].split(" | ")


            a = (formatted[0].split(),formatted[1].split())
            input_data.append(a)


    for line in input_data:
        total += check_winners(line)

    print(total)
