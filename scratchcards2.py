def check_winners(input):
    '''
        Checks for occurences of winning numbers in a line of input.

        Returns:    The value of this line based on winning number occurences.
    '''
    score = 0
    per_ticket_winners = {}
    ticket_counts = []

    #   Pre-process input data to find winning occurences for original tickets
    for idx,input_line in enumerate(input):
        linescore = 0
        for i in input_line[1]:
            if i in input_line[0]:
                linescore += 1
        score += linescore
        per_ticket_winners[idx] = linescore
        ticket_counts.append(1)

    #   For each card
    for idx, card in enumerate(ticket_counts):

        #   Repeat for however many copies of this card we have
        for i in range(per_ticket_winners[idx] + 1):
            if i > 0:
                ticket_counts[idx + i] += 1 * card

    return sum(ticket_counts)


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

    print(check_winners(input_data))
