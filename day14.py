# # Part 1
# import re 

# f = open('day14.txt')
# lines = f.readlines()
# lines = [x.strip('\n') for x in lines]
# lines = [re.findall(r'-?\d+\.?\d*', x) for x in lines]
# lines = [[int(i) for i in line] for line in lines]

# # store rock coords
# rock = []
# for line in lines:
#     i = 0
#     while i in range(len(line)-2):
#         xdif = line[i+2]-line[i]
#         ydif = line[i+3]-line[i+1]
#         isNeg = 1
#         if xdif < 0 or ydif < 0:
#             isNeg = -1
#         for j in range(abs(xdif)):
#             rock.append([line[i]+isNeg*j, line[i+1]])
#         for j in range(abs(ydif)):
#             rock.append([line[i],line[i+1]+isNeg*j])
#         i = i+2
#         if i == len(line)-2:
#             rock.append([line[-2],line[-1]])

# # find min rock y value
# minrock = 0
# for r in rock:
#     if r[1] > minrock:
#         minrock = r[1]

# sandtest = [500,0]
# block = rock
# sandcnt = 0
# while sandtest[1] < minrock:
#     sandtest = [500,0]
#     while sandtest not in block and sandtest[1] < minrock:
#         if [sandtest[0], sandtest[1]+1] not in block:
#             sandtest[1] = sandtest[1]+1
#         elif [sandtest[0]-1, sandtest[1]+1] not in block:
#             sandtest = [sandtest[0]-1, sandtest[1]+1]
#         elif [sandtest[0]+1, sandtest[1]+1] not in block:
#             sandtest = [sandtest[0]+1, sandtest[1]+1]
#         else:
#             block.append(sandtest)
#     sandcnt = sandcnt+1

# print(sandcnt-1)

# Part 2
import re 

f = open('day14.txt')
lines = f.readlines()
lines = [x.strip('\n') for x in lines]
lines = [re.findall(r'-?\d+\.?\d*', x) for x in lines]
lines = [[int(i) for i in line] for line in lines]

# store rock coords
rock = []
for line in lines:
    i = 0
    while i in range(len(line)-2):
        xdif = line[i+2]-line[i]
        ydif = line[i+3]-line[i+1]
        isNeg = 1
        if xdif < 0 or ydif < 0:
            isNeg = -1
        for j in range(abs(xdif)):
            rock.append([line[i]+isNeg*j, line[i+1]])
        for j in range(abs(ydif)):
            rock.append([line[i],line[i+1]+isNeg*j])
        i = i+2
        if i == len(line)-2:
            rock.append([line[-2],line[-1]])

# find min rock y value
minrock = 0
for r in rock:
    if r[1] > minrock:
        minrock = r[1]
floor = minrock + 2
floorlst = []
for i in range(500-floor, 500+floor+1):
    floorlst.append([i,floor])

sandtest = []
block = rock
block.extend(floorlst)
sandcnt = 0
while sandtest != [500,0]:
    sandtest = [500,0]
    while sandtest not in block:
        if [sandtest[0], sandtest[1]+1] not in block:
            sandtest[1] = sandtest[1]+1
        elif [sandtest[0]-1, sandtest[1]+1] not in block:
            sandtest = [sandtest[0]-1, sandtest[1]+1]
        elif [sandtest[0]+1, sandtest[1]+1] not in block:
            sandtest = [sandtest[0]+1, sandtest[1]+1]
        else:
            block.append(sandtest)
    if sandtest == [500,0]:
        sandcnt = sandcnt+1
        break
    sandcnt = sandcnt+1

print(sandcnt)