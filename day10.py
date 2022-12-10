import re

f = open('day10.txt')
lines = f.readlines()
lines = [x.strip('\n') for x in lines]

# # Part 1
# x = 1
# tic = 0
# sum = 0
# for line in lines:
#     if line == 'noop':
#         tic = tic + 1
#         if (tic-20)%40 == 0 and tic <= 220:
#             sum = sum + tic*x
#     else:
#         regChange = int(re.findall(r'-?\d+\.?\d*', line)[0])
#         for i in range(2):
#             tic = tic + 1
#             if (tic-20)%40 == 0 and tic <= 220:
#                 sum = sum + tic*x
#         x = x + regChange
# print(sum)

# Part 2
x = 1
tic = 0
screen = ['.']*40
masterScreen = []
for line in lines:
    if line == 'noop':
        if tic == x or tic == x-1 or tic == x+1:
            screen[tic] = '#'
        tic = tic + 1
        if tic%40 == 0:
            masterScreen.append(screen)
            screen = ['.']*40
            tic = 0

    else:
        regChange = int(re.findall(r'-?\d+\.?\d*', line)[0])
        for i in range(2):
            if tic == x or tic == x-1 or tic == x+1:
                screen[tic] = '#'
            tic = tic + 1
            if tic%40 == 0:
                masterScreen.append(screen)
                screen = ['.']*40
                tic = 0
        x = x + regChange

for x in masterScreen:
    wee = ''
    for y in x:
        wee = wee+y
    print(wee)
    # print('\n')