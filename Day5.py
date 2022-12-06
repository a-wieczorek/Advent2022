import re

with open('inputs//day5-input.txt', 'r') as f:
        input = f.read()
input = input.split('\n')

crates = input[:8]
instructions = input[10:]

crateMatrix = []
cols = 9
for row in crates:
    crateRow = []
    for i in range(cols):
        i = i+1
        if len(row)>=3:
            item = row[:3]
            if len(row)>4:
                row = row[4:]
        item = item.replace(' ', '').replace('[', '').replace(']', '')
        crateRow.append(item)
    crateMatrix.append(crateRow)

instrInNums = []
for instruction in instructions:
    instrInNums.append(re.findall(r'\d+', instruction))

crateMatrix = [[crateMatrix[j][i] for j in range(len(crateMatrix))] for i in range(len(crateMatrix[0]))]
for row in crateMatrix:
    for i in range(50):
        row.insert(0, '')

for instruction in instrInNums:
    print(instructions[instrInNums.index(instruction)])
    takenItems = []
    howMany = int(instruction[0])
    fromWhere = int(instruction[1]) - 1
    toWhere = int(instruction[2]) - 1
    for i in range(len(crateMatrix[fromWhere])):
        if crateMatrix[fromWhere][i] != '':
            for j in range(howMany):
                takenItems.append(crateMatrix[fromWhere][i+j])
                crateMatrix[fromWhere][i+j] = ''
            break

    if all(item == '' for item in crateMatrix[toWhere]):
        i = len(crateMatrix[toWhere])
        for j in range(howMany):
                crateMatrix[toWhere][i-1-j] = takenItems.pop(-1) #pop(0) for star 1
    else:
        for i in range(len(crateMatrix[toWhere])):
            if crateMatrix[toWhere][i] != '':
                for j in range(howMany):
                    crateMatrix[toWhere][i-1-j] = takenItems.pop(-1) #pop(0) for star 1
                break

for row in crateMatrix:
    print(list(filter(lambda a: a != '', row)))

for row in crateMatrix:
    for item in row:
        if item:
            print(item)
            break