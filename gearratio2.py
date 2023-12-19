'''
    gearratio.py

    Advent of Code Day 3 Part 2.

    Author - Jordan Richard
'''

def build_number(data, coords):
    '''
        Given a set of coordinates containing a numeric value, build the whole number.
    '''
    row = coords[0]
    left = coords[1]
    right = coords[1]

    #   Scan to the left to find the left edge of the number
    while left > 0 and data[row][left - 1].isnumeric():
        left -= 1

    #   Scan right to find the right edge
    while right < len(data[0]) - 1 and data[row][right + 1].isnumeric():
        right += 1

    num = ""
    for i in range(left, right + 1):
        num += data[row][i]

    return(num)


def check_perimeter(data, row, col):
    '''
        Checks the perimeter cells of the given cell for gear numbers and returns 
        their product if exactly two found.

        Returns: The product of exactly two edge "gear numbers" if encountered, otherwise 0.
    '''

    reading = False
    coords = ()
    clist = []

    product = 0

    #   Case - First row
    if row == 0:
        for i in range(row, row + 2):

            #   Case - left edge: Skip Left corner to right corner
            if row - 1 < 0:
                for j in range(col, col + 2):
                    if  data[i][j].isnumeric():
                        #   On last indexes
                        if j == col + 1:
                            coords = (i,j)
                            clist.append(coords)
                            reading = False
                        else:
                            reading = True
                            coords = (i,j)

                    #Reached end of this number
                    elif reading:
                        clist.append(coords)
                        reading = False

            #   Case - right edge: From Left corner skip right corner
            elif col >= len(data[0]):
                if  data[i][j].isnumeric():
                    #   On last indexes
                    if i == row + 1 and j == col:
                        coords = (i,j)
                        clist.append(coords)
                        reading = False
                    else:
                        reading = True
                        coords = (i,j)

                #Reached end of this number
                elif reading:
                    clist.append(coords)
                    reading = False

            #   Default case: circle fully around from corner to corner
            else:
                for j in range(col - 1, col + 2):
                    if  data[i][j].isnumeric():
                        #   On last indexes
                        if j == col + 1:
                            coords = (i,j)
                            clist.append(coords)
                            reading = False
                        else:
                            reading = True
                            coords = (i,j)

                    #Reached end of this number
                    elif reading:
                        clist.append(coords)
                        reading = False

    #   Case - last row
    elif row == len(data) - 1:
        for i in range(row - 1, row + 1):

            #   Case - left edge: Skip Left corner to right corner
            if row - 1 < 0:
                for j in range(col, col + 2):
                    if  data[i][j].isnumeric():
                        #   On last indexes
                        if j == col + 1:
                            coords = (i,j)
                            clist.append(coords)
                            reading = False
                        else:
                            reading = True
                            coords = (i,j)

                    #Reached end of this number
                    elif reading:
                        clist.append(coords)
                        reading = False

            #   Case - right edge: From Left corner skip right corner
            elif col >= len(data[0]):
                for j in range(col - 1, col):
                    if  data[i][j].isnumeric():
                        #   On last indexes
                        if i == row + 1 and j == col:
                            coords = (i,j)
                            clist.append(coords)
                            reading = False
                        else:
                            reading = True
                            coords = (i,j)

                    #Reached end of this number
                    elif reading:
                        clist.append(coords)
                        reading = False

            #   Default case
            else:
                for j in range(col - 1, col + 2):
                    if  data[i][j].isnumeric():
                        #   On last indexes
                        if j == col + 1:
                            coords = (i,j)
                            clist.append(coords)
                            reading = False
                        else:
                            reading = True
                            coords = (i,j)

                    #Reached end of this number
                    elif reading:
                        clist.append(coords)
                        reading = False

    else:
        #   Default case: Previous, current, and next rows
        for i in range(row - 1, row + 2):

            #   Case - left edge: Skip Left corner to right corner
            if row - 1 < 0:
                for j in range(col, col + 2):
                    if  data[i][j].isnumeric():
                        #   On last indexes
                        if j == col + 1:
                            coords = (i,j)
                            clist.append(coords)
                            reading = False
                        else:
                            reading = True
                            coords = (i,j)

                    #Reached end of this number
                    elif reading:
                        clist.append(coords)
                        reading = False

            #   Case - right edge: From Left corner skip right corner
            elif col == len(data[0]) - 1:
                for j in range(col - 1, col):

                    if  data[i][j].isnumeric():
                        #   On last indexes
                        if i == row + 1 and j == col:
                            coords = (i,j)
                            clist.append(coords)
                            reading = False
                        else:
                            reading = True
                            coords = (i,j)

                    #Reached end of this number
                    elif reading:
                        clist.append(coords)
                        reading = False

            #   Default case: circle fully around from corner to corner
            else:
                for j in range(col - 1, col + 2):

                    if  data[i][j].isnumeric():
                        #   On last indexes
                        if j == col + 1:
                            coords = (i,j)
                            clist.append(coords)
                            reading = False
                        else:
                            reading = True
                            coords = (i,j)

                    #Reached end of this number
                    elif reading:
                        clist.append(coords)
                        reading = False

        #   If exactly two part numbers are found
        if len(clist) == 2:
            a = build_number(data,clist[0])
            b = build_number(data,clist[1])
            product = int(a) * int(b)
            print(product)
            return product

        else:
            print(0)
            return 0


if __name__ == '__main__':

    input_data = []
    total = 0

    #   Feed input data into a 2d array
    with open('input.txt', encoding='utf-8') as fp:
        for line in fp.readlines():
            input_data.append(list(line.strip("\n")))

    #   Iterate through the array to find a * symbol (gear)
    for ridx,row in enumerate(input_data):
        for cidx, column_value in enumerate(row):

            #   If we found a gear, check its perimeter for part numbers
            if column_value == '*':
                total += check_perimeter(input_data, ridx, cidx)

    print(total)
