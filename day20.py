f = open('day20test.txt')
order = f.readlines()
order = [x.strip('\n') for x in order]
order = [int(x) for x in order]
mod = len(order)

# create dictionary with order as key and index as value
index = {}
for i in range(len(order)):
    index[order[i]].append(i)

print