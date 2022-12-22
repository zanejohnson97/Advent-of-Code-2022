# # Part 1

# import re 

# def wraparound(curheading, curloctest):
#     if curheading == 'E':
#         curloctest[1] = 0
#     elif curheading == 'S':
#         curloctest[0] = 0
#     elif curheading == 'W':
#         curloctest[1] = len(map[0])-1
#     else:
#         curloctest[0] = len(map)-1

#     return curloctest

# def getcoords(curloctest):
#     x = curloctest[1]
#     y = curloctest[0]

#     return x, y

# def advance(curloc, directions, curheading):
#     curloctest = [curloc[0]+directions[curheading][0], curloc[1]+directions[curheading][1]]

#     return curloctest

# def indexExists(list, x, y):
#     if x < 0 or y < 0:
#         return False
#     try:
#         list[y][x]
#         return True
#     except IndexError:
#         return False

# f = open('day22map.txt')
# map = f.readlines()
# map = [x.strip('\n') for x in map]
# map = [list(x) for x in map]

# f = open('day22dir.txt')
# direcs = f.readlines()
# direcs = [x.strip('\n') for x in direcs]
# dnum = [re.findall(r'-?\d+\.?\d*', x) for x in direcs][0]
# dnum = [int(num) for num in dnum]
# dturnraw = list(direcs[0])
# dturn = []
# for i in range(len(dturnraw)):
#     try: 
#         int(dturnraw[i])
#     except:
#         dturn.append(dturnraw[i])

# # get max width of map
# max = 0
# for line in map:
#     length = len(line)
#     if length > max:
#         max = length

# # fill in map with empty spaces to make algorithm work
# for line in map:
#     length = len(line)
#     if length < max:
#         dif = max-length
#         while dif > 0:
#             line.append(' ')
#             dif = dif-1

# # find start coords
# for i in range(len(map[0])):
#     if map[0][i] == '.':
#         curloc = [0, i]
#         break

# R = ['N', 'E', 'S', 'W']
# L = ['N', 'W', 'S', 'E']
# directions = {'N':[-1, 0], 'S':[1, 0], 'E':[0, 1], 'W':[0, -1]}
# curheading = 'E'

# # run through each set of instructions
# for i in range(len(dnum)):
    
#     # step current location until a wall is hit or complete total number of steps
#     for j in range(dnum[i]):
#         # step forward test location and do checks
#         curloctest = advance(curloc, directions, curheading)
#         x, y = getcoords(curloctest)

#         # if still on map
#         if indexExists(map, x, y):
#             # if test is a wall, break out of loop and dont update curloc
#             if map[y][x] == '#':
#                 break
            
#             # if test is empty space, continue until it is not empty space or an edge to wrap around
#             elif map[y][x] == ' ':
#                 while map[y][x] == ' ':
#                     curloctest = advance(curloctest, directions, curheading)
#                     x, y = getcoords(curloctest)

#                     # if new test spot is outside map, wrap around
#                     if indexExists(map, x, y) == False:
#                         curloctest = wraparound(curheading, curloctest)
#                         x, y = getcoords(curloctest)

#                 # once a not empty space is reached, test space and see what to do
#                 if map[y][x] == '#':
#                     break
                
#                 # regular advance. Save test as new current loc
#                 else:
#                     curloc = curloctest

#             # regular advance. Save test as new current loc
#             else:
#                 curloc = curloctest


#         # if not on map, wrap around and try the wrapped position
#         else:
#             curloctest = wraparound(curheading, curloctest)
#             x, y = getcoords(curloctest)

#             # if test is a wall, break out of loop and dont update curloc
#             if map[y][x] == '#':
#                 break

#             # if test is empty space, continue until it is not empty space
#             elif map[y][x] == ' ':
#                 while map[y][x] == ' ':
#                     curloctest = advance(curloctest, directions, curheading)
#                     x, y = getcoords(curloctest)

#                 # once a not empty space is reached, test space and see what to do
#                 if map[y][x] == '#':
#                     break
                
#                 # regular advance. Save test as new current loc
#                 else:
#                     curloc = curloctest
    
#     # change direction unelss its the end, then break out of loop
#     try:
#         if dturn[i] == 'R':
#             headingindex = R.index(curheading)
#             if headingindex == 3:
#                 headingindex = 0
#             else:
#                 headingindex = headingindex + 1
#             curheading = R[headingindex]
#         else:
#             headingindex = L.index(curheading)
#             if headingindex == 3:
#                 headingindex = 0
#             else:
#                 headingindex = headingindex + 1   
#             curheading = L[headingindex]
#     except:
#         break

# if curheading == 'E':
#     dirvalue = 0
# elif curheading == 'S':
#     dirvalue = 1
# elif curheading == 'W':
#     dirvalue = 2
# else:
#     dirvalue = 3
# password = 1000*(curloc[0]+1) + 4*(curloc[1]+1) + dirvalue
# print(password)

# Part 2
import re 

def wraparound(curheading, curloctest):
    if curheading == 'E':
        curloctest[1] = 0
    elif curheading == 'S':
        curloctest[0] = 0
    elif curheading == 'W':
        curloctest[1] = len(map[0])-1
    else:
        curloctest[0] = len(map)-1

    return curloctest

def getcoords(curloctest):
    x = curloctest[1]
    y = curloctest[0]

    return x, y

def advance(curloc, directions, curheading):
    curloctest = [curloc[0]+directions[curheading][0], curloc[1]+directions[curheading][1]]

    return curloctest

def indexExists(list, x, y):
    if x < 0 or y < 0:
        return False
    try:
        list[y][x]
        return True
    except IndexError:
        return False

f = open('day22map.txt')
map = f.readlines()
map = [x.strip('\n') for x in map]
map = [list(x) for x in map]

f = open('day22dir.txt')
direcs = f.readlines()
direcs = [x.strip('\n') for x in direcs]
dnum = [re.findall(r'-?\d+\.?\d*', x) for x in direcs][0]
dnum = [int(num) for num in dnum]
dturnraw = list(direcs[0])
dturn = []
for i in range(len(dturnraw)):
    try: 
        int(dturnraw[i])
    except:
        dturn.append(dturnraw[i])

# get max width of map
max = 0
for line in map:
    length = len(line)
    if length > max:
        max = length

# fill in map with empty spaces to make algorithm work
for line in map:
    length = len(line)
    if length < max:
        dif = max-length
        while dif > 0:
            line.append(' ')
            dif = dif-1

# find start coords
for i in range(len(map[0])):
    if map[0][i] == '.':
        curloc = [0, i]
        break

R = ['N', 'E', 'S', 'W']
L = ['N', 'W', 'S', 'E']
directions = {'N':[-1, 0], 'S':[1, 0], 'E':[0, 1], 'W':[0, -1]}
curheading = 'E'

# run through each set of instructions
for i in range(len(dnum)):
    
    # step current location until a wall is hit or complete total number of steps
    for j in range(dnum[i]):
        # step forward test location and do checks
        curloctest = advance(curloc, directions, curheading)
        x, y = getcoords(curloctest)

        # if still on map
        if indexExists(map, x, y):
            # if test is a wall, break out of loop and dont update curloc
            if map[y][x] == '#':
                break
            
            # if test is empty space, continue until it is not empty space or an edge to wrap around
            elif map[y][x] == ' ':
                while map[y][x] == ' ':
                    curloctest = advance(curloctest, directions, curheading)
                    x, y = getcoords(curloctest)

                    # if new test spot is outside map, wrap around
                    if indexExists(map, x, y) == False:
                        curloctest = wraparound(curheading, curloctest)
                        x, y = getcoords(curloctest)

                # once a not empty space is reached, test space and see what to do
                if map[y][x] == '#':
                    break
                
                # regular advance. Save test as new current loc
                else:
                    curloc = curloctest

            # regular advance. Save test as new current loc
            else:
                curloc = curloctest


        # if not on map, wrap around and try the wrapped position
        else:
            curloctest = wraparound(curheading, curloctest)
            x, y = getcoords(curloctest)

            # if test is a wall, break out of loop and dont update curloc
            if map[y][x] == '#':
                break

            # if test is empty space, continue until it is not empty space
            elif map[y][x] == ' ':
                while map[y][x] == ' ':
                    curloctest = advance(curloctest, directions, curheading)
                    x, y = getcoords(curloctest)

                # once a not empty space is reached, test space and see what to do
                if map[y][x] == '#':
                    break
                
                # regular advance. Save test as new current loc
                else:
                    curloc = curloctest
    
    # change direction unelss its the end, then break out of loop
    try:
        if dturn[i] == 'R':
            headingindex = R.index(curheading)
            if headingindex == 3:
                headingindex = 0
            else:
                headingindex = headingindex + 1
            curheading = R[headingindex]
        else:
            headingindex = L.index(curheading)
            if headingindex == 3:
                headingindex = 0
            else:
                headingindex = headingindex + 1   
            curheading = L[headingindex]
    except:
        break

if curheading == 'E':
    dirvalue = 0
elif curheading == 'S':
    dirvalue = 1
elif curheading == 'W':
    dirvalue = 2
else:
    dirvalue = 3
password = 1000*(curloc[0]+1) + 4*(curloc[1]+1) + dirvalue
print(password)
