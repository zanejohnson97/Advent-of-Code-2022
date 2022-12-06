f = open('day6.txt')
str = f.read()
lst = list(str)

# # part 1
# marker = False
# i=4
# while marker == False:
#     testlst = lst[i-4:i]
#     if len(testlst) == len(set(testlst)):
#         marker = True
#     else:
#         i = i+1

# print(i)

# part 2
marker = False
i=14
while marker == False:
    testlst = lst[i-14:i]
    if len(testlst) == len(set(testlst)):
        marker = True
    else:
        i = i+1

print(i)