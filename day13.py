# # Part 1
# import json

# def check(leftlist, rightlist):
#     inOrder = True
#     # iterate through left list to make comparisons to right list
#     for j in range(len(leftlist)):

#         # if left list is a list, grab just the element to compare
#         if isinstance(leftlist, list):
#             left = leftlist[j]
#         else:
#             left = leftlist

#         # if right runs out of indices -> out of order
#         try:
#             # if right list is a list, grab just the element to compare
#             if isinstance(rightlist, list):
#                 right = rightlist[j]
#             else:
#                 right = rightlist
#         except:
#             inOrder = False
#             break
        
#         # if left is an int and right is a list, make left a list to 
#         # compare and vice versa
#         if isinstance(left, int) and isinstance(right, list):
#             left = [left]
#         if isinstance(right, int) and isinstance(left, list):
#             right = [right]

#         try:
#             # actual comparisons 
#             if left == right:
#                 inOrder = True
#             elif left < right:
#                 inOrder = True
#                 break
            
#             # means that left is greater than right and is out of order
#             else:
#                 inOrder = False
#                 break
#         except:
#             isOrderRec = check(left,right)
#             return isOrderRec

#     return inOrder
    
# # read in file
# f = open('day13.txt')
# lines = f.readlines()
# lines = [x.strip('\n') for x in lines]

# # make master list of all lines in input
# lst = []
# for line in lines:
#     if len(line) == 0:
#         del(line)
#     else:
#         lst.append(json.loads(line))

# i = 0
# ind = []
# # walk down the list in pairs
# while i < len(lst):
#     leftlist = lst[i]
#     rightlist = lst[i+1]
#     # function to check if the pair is in order
#     inOrder = check(leftlist, rightlist)
#     if inOrder == True:
#         ind.append(int(i/2)+1)
#     i = i+2

# # add up indices that are in order and print sum
# sum = 0
# for indy in ind:
#     sum = sum + indy
# print(sum)           

import json

def check(leftlist, rightlist):
    inOrder = True
    # iterate through left list to make comparisons to right list
    for j in range(len(leftlist)):

        # if left list is a list, grab just the element to compare
        if isinstance(leftlist, list):
            left = leftlist[j]
        else:
            left = leftlist

        # if right runs out of indices -> out of order
        try:
            # if right list is a list, grab just the element to compare
            if isinstance(rightlist, list):
                right = rightlist[j]
            else:
                right = rightlist
        except:
            inOrder = False
            break
        
        # if left is an int and right is a list, make left a list to 
        # compare and vice versa
        if isinstance(left, int) and isinstance(right, list):
            left = [left]
        if isinstance(right, int) and isinstance(left, list):
            right = [right]

        try:
            # actual comparisons 
            if left == right:
                inOrder = None
            elif left < right:
                inOrder = True
                break
            
            # means that left is greater than right and is out of order
            else:
                inOrder = False
                break
        except:
            inOrderRec = check(left,right)
            if inOrderRec == None:
                continue
            else:
                return inOrderRec

    return inOrder
    
# read in file
f = open('day13.txt')
lines = f.readlines()
lines = [x.strip('\n') for x in lines]

# make master list of all lines in input
lst = []
for line in lines:
    if len(line) == 0:
        del(line)
    else:
        lst.append(json.loads(line))

i = 0
orglst = [[[2]],[[6]]]
# walk down the list in pairs
while i < len(lst):
    leftlist = lst[i]

    # compare current leftlist to each packet in organized list and 
    # place it where it needs to be
    for j in range(len(orglst)):
        rightlist = orglst[j]
        # function to check if the pair is in order
        inOrder = check(leftlist, rightlist)
        # if the leftlist is less than the list it is being compared to in the 
        # organized list, add it in right in front of it.
        if inOrder == True:
            orglst.insert(j, leftlist)
            break
        # if the leftlist is greater than everything looked at so far, add it 
        # to the end of the organized list
        if inOrder == False and j == len(orglst)-1:
            orglst.append(leftlist)
            break
    i = i+1

for packet in orglst:
    print(packet)

# find dividers and print product
for i in range(len(orglst)):
    if orglst[i] == [[2]]:
        divider1 = i+1
    if orglst[i] == [[6]]:
        divider2 = i+1

print(divider1)
print(divider2)
print(divider1*divider2)