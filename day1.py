f = open('day1.txt')
lines = f.readlines()
lines = [x.strip('\n') for x in lines]
sums=[]
sum=0
x=0

for i in range(len(lines)):
    if lines[i]:
        lines[i] = int(lines[i])
        sum = sum+lines[i]
    else:
        sums.append(sum)
        x=x+1
        sum=0 

sums.sort()
topthree = sums[-1]+sums[-2]+sums[-3]
print(topthree)





