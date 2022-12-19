# # Part 1
# import re 

# f = open('day15.txt')
# lines = f.readlines()
# lines = [x.strip('\n') for x in lines]
# lines = [re.findall(r'-?\d+\.?\d*', x) for x in lines]
# lines = [[int(i) for i in line] for line in lines]

# mandist = []
# sensors = []
# # maxx, maxy = -9999999999, -9999999999
# # minx, miny = 9999999999, 9999999999
# for i in range(len(lines)):
#     x1 = lines[i][0]
#     x2 = lines[i][2]
#     y1 = lines[i][1]
#     y2 = lines[i][3]

#     # minxtemp = min(x1, x2)
#     # if minxtemp < minx:
#     #     minx = minxtemp

#     # maxxtemp = max(x1, x2)
#     # if maxxtemp > maxx:
#     #     maxx = maxxtemp

#     # minytemp = min(y1, y2)
#     # if minytemp < miny:
#     #     miny = minytemp

#     # maxytemp = max(y1, y2)
#     # if maxytemp > maxy:
#     #     maxy = maxytemp

#     xdif = abs(x2-x1)
#     ydif = abs(y2-y1)
#     mandisttemp = xdif + ydif
#     mandist.append(mandisttemp)

#     sensors.append([x1,y1])

# seen = []
# # loop for each sensor point
# for i in range(len(mandist)):
#     if 2000000 in range(sensors[i][1] - mandist[i], sensors[i][1] + mandist[i]):

#         # loop for iterating the horizontal layers of the diamond
#         for j in range(0, mandist[i]+1):
#             y = sensors[i][1]+mandist[i]-j

#             # loop for including all the vertial components of the horizontal
#             # layer
#             if y == 2000000:
#                 k = 0
#                 while k <= j:
#                     x = sensors[i][0]+k
#                     # if x not in seen:
#                     #     seen.append(x)
#                     seen.append(x)
#                     x = sensors[i][0]-k
#                     # if x not in seen:
#                     #     seen.append(x)
#                     seen.append(x)
#                     k = k+1
    
#         # other side of the diamond:
#         for j in range(0, mandist[i]+1):
#             y = sensors[i][1]-mandist[i]+j

#             # loop for including all the vertial components of the horizontal
#             # layer
#             if y == 2000000:
#                 k = 0
#                 while k <= j:
#                     x = sensors[i][0]+k
#                     # if x not in seen:
#                     #     seen.append(x)
#                     seen.append(x)
#                     x = sensors[i][0]-k
#                     # if x not in seen:
#                     #     seen.append(x)
#                     seen.append(x)
#                     k = k+1

# # make sure we dont count sensor positions and beacon positions
# for i in range(len(lines)):
#     j = 0
#     while j < len(lines[i]):
#         x = lines[i][j]
#         y = lines[i][j+1]
#         j = j+2
#         if y == 2000000:
#             seen.remove(x)

# seen = set(seen)
# sum = len(seen)

# print(sum)

# Part 2
import re 

f = open('day15.txt')
lines = f.readlines()
lines = [x.strip('\n') for x in lines]
lines = [re.findall(r'-?\d+\.?\d*', x) for x in lines]
lines = [[int(i) for i in line] for line in lines]

mandist = []
sensors = []
for i in range(len(lines)):
    x1 = lines[i][0]
    x2 = lines[i][2]
    y1 = lines[i][1]
    y2 = lines[i][3]

    xdif = abs(x2-x1)
    ydif = abs(y2-y1)
    mandisttemp = xdif + ydif
    mandist.append(mandisttemp)

    sensors.append([x1,y1])

seen = []
# loop for each sensor point
for i in range(len(mandist)):

    # loop for iterating the horizontal layers of the diamond
    for j in range(0, mandist[i]+1):
        y = sensors[i][1]+mandist[i]-j

        # loop for including all the vertial components of the horizontal
        # layer
        if y >= 0 and y <= 4000000:
            k = 0
            while k <= j:
                x = sensors[i][0]+k
                if x >= 0 and x <= 4000000:
                    seen.append((x,y))
                x = sensors[i][0]-k
                if x >= 0 and x <= 4000000:
                    seen.append((x,y))
                k = k+1

    # other side of the diamond:
    for j in range(0, mandist[i]+1):
        y = sensors[i][1]-mandist[i]+j

        # loop for including all the vertial components of the horizontal
        # layer
        if y >= 0 and y <= 4000000:
            k = 0
            while k <= j:
                x = sensors[i][0]+k
                if x >= 0 and x <= 4000000:
                    seen.append((x,y))
                x = sensors[i][0]-k
                if x >= 0 and x <= 4000000:
                    seen.append((x,y))
                k = k+1

seen = set(seen)
sum = len(seen)

print(sum)