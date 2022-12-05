import re

f = open('day4.txt')
lines = f.readlines()
lines = [x.strip('\n') for x in lines]
numpairs=0

# # Part 1 loop
# for i in range(len(lines)):
#     s = [int(x) for x in re.findall(r'-?\d+\.?\d*', lines[i])]
#     s = [abs(x) for x in s]
#     if s[0] >= s[2] and s[0] <= s[3] and s[1] <= s[3]:
#         numpairs = numpairs+1
#     elif s[2] >= s[0] and s[2] <= s[1] and s[3] <= s[1]:
#         numpairs = numpairs+1

# print(numpairs)
    
# Part 2 loop
for i in range(len(lines)):
    s = [int(x) for x in re.findall(r'-?\d+\.?\d*', lines[i])]
    s = [abs(x) for x in s]
    if s[1] >= s[2] and s[0] <= s[2]:
        numpairs = numpairs+1
    elif s[3] >= s[0] and s[2] <= s[0]:
        numpairs = numpairs+1

print(numpairs)   

