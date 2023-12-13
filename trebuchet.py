with open('input.txt') as fp:
    
    tally = 0
    first = None
    last = None

    #   Each line of input
    for line in fp.readlines():

        #   Each character in this line
        for char in line:

            #   If we found a number
            if char.isnumeric():

                #   If first number is not yet reached
                if first is None:
                    first = char
                    last = char

                #   Continue re-setting last as we reach more numbers
                else: 
                    last = char

        tally += int(f"{first}{last}")
        print(f"FIRST[{first}], LAST[{last}], RUNNING TOTAL - {tally}")

        #   reset
        first = None
        last = None

    print(f"FINAL: {tally}")
