import re

f = open('day7.txt')
lines = f.readlines()
lines = [x.strip('\n') for x in lines]
directoryDict = {}
cd = ''

i=0
while i < len(lines):
    if lines[i] == '$ ls':
        i = i+1
        try:
            while '$' not in lines[i]:
                if 'dir' in lines[i]:
                    directoryDict[cd+lines[i][4:]+'/'] = {'parent':cd}
                    i = i+1 
                else:
                    size = re.findall(r'-?\d+\.?\d*', lines[i])
                    spaceIndex = lines[i].find(' ')
                    filename = cd+lines[i][spaceIndex+1:]
                    if filename == '/a/e/i':
                        a = 1+1
                    directoryDict[filename] = {'size':int(size[0]), 'parent': cd}
                    i = i+1
        except:
            break


    elif lines[i].strip() == '$ cd ..':
        cd = directoryDict[cd]['parent']
        i = i+1

    elif lines[i].strip() == '$ cd /':
        cd = '/'
        i = i+1

    else: # '$ cd to specific directory'
        cd = cd+lines[i][5:]+'/'
        i = i+1

sizeDict = {'/':0}
for key in directoryDict:
    if 'size' in directoryDict[key]:
        size = directoryDict[key]['size']
        parent = directoryDict[key]['parent']
        while parent != '':
            sizeDict[parent] = sizeDict[parent]+directoryDict[key]['size']
            if parent == '/':
                break
            parent = directoryDict[parent]['parent']


    else:
        sizeDict[key] = 0

# Part 1
# sum = 0
# for key in sizeDict:
#     if sizeDict[key] <= 100000:
#         sum = sum + sizeDict[key]

# Part 2
unused = 70000000-sizeDict['/']
minSize = 30000000-unused
lst = []
i = 0
for key in sizeDict:
    lst.append(sizeDict[key])
lst.sort()

for i in range(len(lst)):
    if lst[i] >= minSize:
        print(lst[i])
        break

print(sum)