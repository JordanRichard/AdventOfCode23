'''
    gearratio.py

    Advent of Code Day 3 Part 1.

    Author - Jordan Richard
'''


def check_perimeter(data, lhs_coord, rhs_coord):
    '''
        Checks the perimeter cells of the given number for symbols.

        Returns: True if a symbol is encountered.
    '''
    symbols = ('!','\\','#','$','%','&','(',')','*','+',',','-','/',':',';','<','=',
               '>','?','@','[',']','^','_','`','{','|','}','~')

    #   Case - First row
    if lhs_coord[0] == 0:
        for perimeter_row in range(lhs_coord[0], lhs_coord[0] + 2):

            #   Case - left edge: Skip Left corner to right corner
            if lhs_coord[1] - 1 < 0:
                for perimeter_column in range(lhs_coord[1], rhs_coord[1] + 2):
                    if data[perimeter_row][perimeter_column] in symbols:
                        return True

            #   Case - right edge: From Left corner skip right corner
            elif rhs_coord[1] >= len(data[0]):
                for perimeter_column in range(lhs_coord[1] - 1, rhs_coord[1]):
                    if data[perimeter_row][perimeter_column] in symbols:
                        return True

            #   Default case: circle fully around from corner to corner
            else:
                for perimeter_column in range(lhs_coord[1] - 1, rhs_coord[1] + 2):
                    if data[perimeter_row][perimeter_column] in symbols:
                        return True

    #   Case - last row
    elif lhs_coord[0] == len(data) - 1:
        for perimeter_row in range(lhs_coord[0] - 1, lhs_coord[0] + 1):

            #   Case - left edge: Skip Left corner to right corner
            if lhs_coord[1] - 1 < 0:
                for perimeter_column in range(lhs_coord[1], rhs_coord[1] + 2):
                    if data[perimeter_row][perimeter_column] in symbols:
                        return True

            #   Case - right edge: From Left corner skip right corner
            elif rhs_coord[1] >= len(data[0]):
                for perimeter_column in range(lhs_coord[1] - 1, rhs_coord[1]):
                    if data[perimeter_row][perimeter_column] in symbols:
                        return True

            #   Default case
            else:
                for perimeter_column in range(lhs_coord[1] - 1, rhs_coord[1] + 2):
                    if data[perimeter_row][perimeter_column] in symbols:
                        return True

    else:
        #   Default case: Previous, current, and next rows
        for perimeter_row in range(lhs_coord[0] - 1, lhs_coord[0] + 2):

            #   Case - left edge: Skip Left corner to right corner
            if lhs_coord[1] - 1 < 0:
                for perimeter_column in range(lhs_coord[1], rhs_coord[1] + 2):
                    if data[perimeter_row][perimeter_column] in symbols:
                        return True

            #   Case - right edge: From Left corner skip right corner
            elif rhs_coord[1] == len(data[0]) - 1:
                for perimeter_column in range(lhs_coord[1] - 1, rhs_coord[1]):
                    if data[perimeter_row][perimeter_column] in symbols:
                        return True

            #   Default case: circle fully around from corner to corner
            else:
                for perimeter_column in range(lhs_coord[1] - 1, rhs_coord[1] + 2):
                    if  data[perimeter_row][perimeter_column] in symbols:
                        return True



if __name__ == '__main__':

    input_data = []
    total = 0
    l_marker = None
    r_marker = None
    number_stack = ""

    #   Feed input data into a 2d array
    with open('input.txt', encoding='utf-8') as fp:
        for line in fp.readlines():
            input_data.append(list(line.strip("\n")))

    #   Iterate through the array to find each number
    for ridx,row in enumerate(input_data):
        for cidx, column_value in enumerate(row):

            #   If we found a numer, mark its index
            if column_value.isnumeric():

                #   Mark the LHS coordinate of this number sequence, expand the RHS
                if l_marker is None:

                    #   Check for single digit number
                    if cidx == len(row) -  1 or not row[cidx + 1].isnumeric():
                        number_stack += column_value
                        r_marker = (ridx,cidx)
                        l_marker = r_marker

                        if check_perimeter(input_data, l_marker, r_marker):
                            total += int(number_stack)

                        #   Clear markers
                        number_stack = ""
                        l_marker = None
                        r_marker = None

                    else:
                        l_marker = (ridx,cidx)
                        number_stack += column_value

                #   Check if the next column is non-numeric or right edge. If so, RHS is found.
                else:

                    if cidx == len(row) - 1 or not row[cidx + 1].isnumeric():
                        number_stack += column_value
                        r_marker = (ridx,cidx)

                        if check_perimeter(input_data, l_marker, r_marker):
                            total += int(number_stack)

                        #   Clear markers
                        number_stack = ""
                        l_marker = None
                        r_marker = None

                    #   Else, we are partway through the number, continue building it
                    else:
                        number_stack += column_value

    print(total)
