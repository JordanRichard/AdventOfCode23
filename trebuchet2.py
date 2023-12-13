with open('input.txt') as fp:

    tally = 0
    keywords = {
        "zero": 0,
        "one":1,
        "two":2,
        "three":3,
        "four":4,
        "five":5,
        "six":6,
        "seven":7,
        "eight":8,
        "nine":9
        }

    #   Build list formatted input data in memory
    linelist = []
    for line in fp.readlines():
        linelist.append(line.strip("\n"))

    #   Iterate each line of input
    for line in linelist:

        first = None
        last = None

        #   Pre-process input data
        for word,val in keywords.items():
            line = line.replace(word,f"{word}{val}{word}")

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
        print(f"{line}\nFIRST[{first}], LAST[{last}], RUNNING TOTAL - {tally}")

        #   reset
        first = None
        last = None

    print(f"FINAL: {tally}")
