with open('input.txt') as fp:

    powers = []
    sum = 0

    #   Feed input data into a 2d array
    for line in fp.readlines():
        powers.append(list(line.strip("\n")))



for ridx,row in enumerate(powers):
    print(row)
 
    #   Reset L/R markers / number stack for new row
    l_marker = None
    r_marker = None
    number_stack = ""

    for cidx, column_value in enumerate(row):

        #   If we found a numer, mark its index
        if column_value.isnumeric():

            #   Mark the LHS coordinate of this number sequence, else mark/expand the RHS
            if l_marker is None:
                l_marker = (ridx,cidx)
                number_stack += column_value

            else:
                #   Check if the next column is empty (.) or non-numeric. If so, RHS is found. (Then, check for adjacent symbols)
                if cidx + 1 < len(row) and not row[cidx + 1].isnumeric():
                    number_stack += column_value
                    print(f"End of this number reached: {number_stack}")

                    #   Clear the stack
                    number_stack = ""


                #   Else, we are partway through the number, continue building it
                else:
                    number_stack += column_value

                pass



        #   Edge case - first row
        if ridx == 0:
            pass

        #   Edge case - last row
        if ridx == len(powers) + 1:
            pass