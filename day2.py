f = open('day2.txt')
lines = f.readlines()
lines = [x.strip('\n') for x in lines]
sum = 0

for i in range(len(lines)):
    roundsum = 0
    # wdl 3=lose, 2=draw, 1=win
    wdl = 0
    # points for win, draw, and lose
    if lines[i][2] == 'X':
        roundsum = roundsum+0
        wdl = 3

    elif lines[i][2] == 'Y':
        roundsum = roundsum+3
        wdl = 2

    else:
        roundsum = roundsum+6
        wdl = 1

    # points for each sign tossed out there yuh
    # rock
    if lines[i][0] == 'A' and wdl == 2 or lines[i][0] == 'B' and wdl == 3 or lines[i][0] == 'C' and wdl == 1:
        roundsum = roundsum + 1

    # paper
    elif lines[i][0] == 'A' and wdl == 1 or lines[i][0] == 'B' and wdl == 2 or lines[i][0] == 'C' and wdl == 3:
        roundsum = roundsum + 2

    # scissors
    if lines[i][0] == 'A' and wdl == 3 or lines[i][0] == 'B' and wdl == 1 or lines[i][0] == 'C' and wdl == 2:
        roundsum = roundsum + 3

    print(roundsum)
    # add up all the points from this round to the total sum      
    sum = sum+roundsum

print(sum)