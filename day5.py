import re

f = open('day5a.txt')
lines = f.readlines()
lines = [x.strip('\n') for x in lines]

f = open('day5b.txt')
boxes = [['R','N','P','G'],['T','J','B','L','C','S','V','H'],['T','D','B','M','N','L'],['R','V','P','S','B'],['G','C','Q','S','W','M','V','H'],
['W','Q','S','C','D','B','J'],['F','Q','L'],['W','M','H','T','D','L','F','V'],['L','P','B','V','M','J','F']]

for i in range(len(lines)):
    s = [int(x) for x in re.findall(r'-?\d+\.?\d*', lines[i])]
    s[1] = s[1]-1
    s[2] = s[2]-1
    
    movBox = boxes[s[1]][-s[0]:]
    boxes[s[2]] = boxes[s[2]] + movBox
    del boxes[s[1]][-s[0]:]

word = ''
for i in range(len(boxes)):
    word = word+boxes[i][-1]

print(word)