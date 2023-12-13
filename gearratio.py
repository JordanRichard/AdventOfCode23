with open('input.txt') as fp:

    powers = []

    #   Feed input data into a 2d array
    for line in fp.readlines():
        powers.append(list(line.strip("\n")))



for ridx,row in enumerate(powers):
    print(row)
 
    #   Reset L/R markers for new row
    l_marker = None
    r_marker = None

    for cidx,column in enumerate(row):

        #   If we found a numer, mark its index
        if column.isnumeric():

            #   Mark the LHS coordinate of this number sequence, else mark/expand the RHS
            if l_marker is None:
                pass

            else:
                #   Check if the next column is empty (.) or non-numeric. If so, RHS is found. (Then, check for adjacent symbols)
                pass



        #   Edge case - first row
        if ridx == 0:
            pass

        #   Edge case - last row
        if ridx == len(powers) + 1:
            pass