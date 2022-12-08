f = open('day8.txt')
lines = f.readlines()
lines = [x.strip('\n') for x in lines]
grid = []

for i in range(len(lines)):
    grid.append(list(lines[i]))

# # Part 1
# visible = [[0]*len(grid) for i in range(len(grid[0]))]
# for i in range(len(grid)):
#     for j in range(len(grid[0])):
#         if i == 0 or j == 0 or i == len(grid)-1 or j == len(grid[0])-1:
#             visible[i][j] = 1

#         else: 
#             testHeight = grid[i][j]
#             left = grid[i][:j]
#             right = grid[i][j+1:]
#             up = []
#             for k in range(len(grid[:i])):
#                 up.append(grid[:i][k][j])
            
#             down = []
#             for k in range(len(grid[i+1:])):
#                 down.append(grid[i+1:][k][j])

#             if max(right) < testHeight or max(left) < testHeight or max(up) < testHeight or max(down) < testHeight:
#                 visible[i][j] = 1

# sum = 0
# for i in range(len(visible)):
#     for j in range(len(visible[0])):
#         sum = sum + visible[i][j]

# print(sum)

# Part 2
score = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        testHeight = grid[i][j]
        left = grid[i][:j]
        left.reverse()
        right = grid[i][j+1:]
        up = []
        for k in range(len(grid[:i])):
            up.append(grid[:i][k][j])
        up.reverse()
        down = []
        for k in range(len(grid[i+1:])):
            down.append(grid[i+1:][k][j])
        upscore = 0
        downscore = 0
        leftscore = 0
        rightscore = 0

        for u in up:
            if u < testHeight:
                upscore = upscore + 1
            elif u >= testHeight:
                upscore = upscore + 1
                break
            else:
                break
        
        for u in down:
            if u < testHeight:
                downscore = downscore + 1
            elif u >= testHeight:
                downscore = downscore + 1
                break
            else:
                break

        for u in left:
            if u < testHeight:
                leftscore = leftscore + 1
            elif u >= testHeight:
                leftscore = leftscore + 1
                break
            else:
                break

        for u in right:
            if u < testHeight:
                rightscore = rightscore + 1
            elif u >= testHeight:
                rightscore = rightscore + 1
                break
            else:
                break

        testScore = upscore*downscore*leftscore*rightscore
        if testScore > score:
            score = testScore

print(score)
