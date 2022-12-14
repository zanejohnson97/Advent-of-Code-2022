import re
import math

f = open('day11.txt')
lines = f.readlines()
lines = [x.strip('\n') for x in lines]

class Monke:
    def __init__(self, name, items, operation, test, t, f, inspect):
        self.name = name
        self.items = items
        self.operation = operation
        self.test = test
        self.t = t
        self.f = f
        self.inspect = inspect

# # Part 1
# i = 0
# monkeys = []
# while i in range(len(lines)):
#     name = lines[i][:-1]
#     items = re.findall(r'-?\d+\.?\d*', lines[i+1])
#     operation  = lines[i+2][23:]
#     test = int(re.findall(r'-?\d+\.?\d*', lines[i+3])[0])
#     t = int(re.findall(r'-?\d+\.?\d*', lines[i+4])[0])
#     f = int(re.findall(r'-?\d+\.?\d*', lines[i+5])[0])
#     inspect = 0
#     monkeys.append(Monke(name, items, operation, test, t, f, inspect))
#     i = i+7

# for i in range(20):
#     for monkey in monkeys:
#         for item in monkey.items:
#             monkey.inspect = monkey.inspect + 1
#             old = item
#             if monkey.operation.find('old') == -1:
#                 execute = 'item = '+old+ monkey.operation
#             else:
#                 execute = 'item = '+old+'*'+old
#             exec(execute)
#             item = math.floor(item/3)
#             if item%monkey.test == 0:
#                 item = str(item)
#                 monkeys[monkey.t].items.append(item)
#                 monkey.items = monkey.items[1:]
#             else:
#                 item = str(item)
#                 monkeys[monkey.f].items.append(item)
#                 monkey.items = monkey.items[1:]

# inspections = []
# for monkey in monkeys:
#     inspections.append(monkey.inspect)

# inspections.sort()
# mnkybsns = inspections[-1]*inspections[-2]
# print(mnkybsns)

# Part 2
i = 0
monkeys = []
while i in range(len(lines)):
    name = lines[i][:-1]
    items = re.findall(r'-?\d+\.?\d*', lines[i+1])
    operation  = lines[i+2][23:]
    test = int(re.findall(r'-?\d+\.?\d*', lines[i+3])[0])
    t = int(re.findall(r'-?\d+\.?\d*', lines[i+4])[0])
    f = int(re.findall(r'-?\d+\.?\d*', lines[i+5])[0])
    inspect = 0
    monkeys.append(Monke(name, items, operation, test, t, f, inspect))
    i = i+7

mod = 1
for monkey in monkeys:
    mod = monkey.test*mod

for i in range(10000):
    for monkey in monkeys:
        for item in monkey.items:
            monkey.inspect = monkey.inspect + 1
            old = item
            if monkey.operation.find('old') == -1:
                execute = 'item = '+old+ monkey.operation
            else:
                execute = 'item = '+old+'*'+old
            exec(execute)
            item = item%mod
            if item%monkey.test == 0: # this needs to change
                item = str(item)
                monkeys[monkey.t].items.append(item)
                monkey.items = monkey.items[1:]
            else:
                item = str(item)
                monkeys[monkey.f].items.append(item)
                monkey.items = monkey.items[1:]

inspections = []
for monkey in monkeys:
    inspections.append(monkey.inspect)

inspections.sort()
mnkybsns = inspections[-1]*inspections[-2]
print(mnkybsns)