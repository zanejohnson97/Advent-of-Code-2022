f = open('day3.txt')
lines = f.readlines()
lines = [x.strip('\n') for x in lines]
sum=0

# Part 1 loop
# for i in range(len(lines)):
#     halfItems=int(len(lines[i])/2)
#     comp1 = lines[i][0:halfItems]
#     comp2 = lines[i][halfItems:]
#     chars = list(comp1)
#     for char in chars:
#         truth = char in comp2
#         if truth:
#             if ord(char) < 91:  # uppercase
#                 sum = sum + ord(char)-38
#             else:  # lowercase
#                 sum = sum + ord(char)-96

#             break

# Part 2 loop
i=0
while i < len(lines):
    elf1 = lines[i]
    elf2 = lines[i+1]
    elf3 = lines[i+2]
    chars1 = list(elf1)
    for char in chars1:
        truth = char in elf2
        if truth:
            truth = char in elf3
            if truth:
                if ord(char) < 91:  # uppercase
                    sum = sum + ord(char)-38
                else:  # lowercase
                    sum = sum + ord(char)-96

                break
    i=i+3

print(sum)