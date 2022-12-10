import re

f = open('day9.txt')
lines = f.readlines()
lines = [x.strip('\n') for x in lines]

# # Part 1
# H = [0,0]
# T = [0,0]
# tailLoc = [[0,0]]

# for i in range(len(lines)):
#     moves = int(re.findall(r'-?\d+\.?\d*', lines[i])[0])

#     # Moves to the right
#     if lines[i][0] == 'R':
#         for j in range(moves):
#             T = list(T)
#             H[0] = H[0]+1
#             if abs(H[0]-T[0]) > 1 and H[1]-T[1] == 0:  # does T need to move?
#                 T[0] = T[0]+1
#                 if T not in tailLoc:
#                     tailLoc.append(T)

#             elif abs(H[0]-T[0]) > 1 and abs(H[1]-T[1]) == 1:
#                 T[0] = T[0]+1
#                 if H[1]-T[1] > 0:
#                     T[1] = T[1]+1
#                 else:
#                     T[1] = T[1]-1

#                 if T not in tailLoc:
#                     tailLoc.append(T)

#     # Moves to the left
#     elif lines[i][0] == 'L':
#         for j in range(moves):
#             T = list(T)
#             H[0] = H[0]-1
#             if abs(H[0]-T[0]) > 1 and H[1]-T[1] == 0:
#                 T[0] = T[0]-1
#                 if T not in tailLoc:
#                     tailLoc.append(T)

#             elif abs(H[0]-T[0]) > 1 and abs(H[1]-T[1]) == 1:
#                 T[0] = T[0]-1
#                 if H[1]-T[1] > 0:
#                     T[1] = T[1]+1
#                 else:
#                     T[1] = T[1]-1

#                 if T not in tailLoc:
#                     tailLoc.append(T)

#     # Moves to the up
#     elif lines[i][0] == 'U':
#         for j in range(moves):
#             T = list(T)
#             H[1] = H[1]+1
#             if H[0]-T[0] == 0 and abs(H[1]-T[1]) > 1:  # does T need to move?
#                 T[1] = T[1]+1
#                 if T not in tailLoc:
#                     tailLoc.append(T)

#             elif abs(H[0]-T[0]) == 1 and abs(H[1]-T[1]) > 1:
#                 T[1] = T[1]+1
#                 if H[0]-T[0] > 0:
#                     T[0] = T[0]+1
#                 else:
#                     T[0] = T[0]-1

#                 if T not in tailLoc:
#                     tailLoc.append(T)

#     # Moves to the down
#     else:
#         for j in range(moves):
#             T = list(T)
#             H[1] = H[1]-1
#             if H[0]-T[0] == 0 and abs(H[1]-T[1]) > 1:  # does T need to move?
#                 T[1] = T[1]-1
#                 if T not in tailLoc:
#                     tailLoc.append(T)

#             elif abs(H[0]-T[0]) == 1 and abs(H[1]-T[1]) > 1:
#                 T[1] = T[1]-1
#                 if H[0]-T[0] > 0:
#                     T[0] = T[0]+1
#                 else:
#                     T[0] = T[0]-1

#                 if T not in tailLoc:
#                     tailLoc.append(T)


# uniquePos = len(tailLoc)
# print(uniquePos)

# Part 2
T = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
tailLoc = [[0,0]]

for i in range(len(lines)):
    moves = int(re.findall(r'-?\d+\.?\d*', lines[i])[0])
    for j in range(moves):
        if lines[i][0] == 'R':
            T[0][0] = T[0][0]+1
        elif lines[i][0] == 'L':
            T[0][0] = T[0][0]-1
        elif lines[i][0] == 'U':
            T[0][1] = T[0][1]+1
        else:
            T[0][1] = T[0][1]-1

        k = 1
        while k in range(len(T)):
            T[k] = list(T[k])
            # decide to move or not
            if abs(T[k][0]-T[k-1][0]) < 2 and abs(T[k][1]-T[k-1][1]) < 2:
                k = k+1
            else:
                xdif = T[k-1][0]-T[k][0]
                ydif = T[k-1][1]-T[k][1]

                if xdif == 2:
                    T[k][0] = T[k][0] + 1
                    if ydif == 1:
                        T[k][1] = T[k][1] + 1
                    elif ydif == -1:
                        T[k][1] = T[k][1] - 1

                elif xdif == -2:
                    T[k][0] = T[k][0] - 1
                    if ydif == 1:
                        T[k][1] = T[k][1] + 1
                    elif ydif == -1:
                        T[k][1] = T[k][1] - 1

                elif ydif == 2:
                    T[k][1] = T[k][1] + 1
                    if xdif == 1:
                        T[k][0] = T[k][0] + 1
                    elif xdif == -1:
                        T[k][0] = T[k][0] - 1

                elif ydif == -2:
                    T[k][1] = T[k][1] - 1
                    if xdif == 1:
                        T[k][0] = T[k][0] + 1
                    elif xdif == -1:
                        T[k][0] = T[k][0] - 1

                k = k+1
                if T[9] not in tailLoc:
                    tailLoc.append(T[9])

uniquePos = len(tailLoc)
print(uniquePos)