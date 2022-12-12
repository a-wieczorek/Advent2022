import re
from copy import deepcopy

with open('inputs//day11-input.txt', 'r') as f:
    input = f.read().split('\n\n')
    input = [lines.split('\n') for lines in input]

MONKEYS = []
divisionFactors = {}


class Item():
    value: int
    whoCanDivide = dict()
    rests = dict()

    def __init__(self, x):
        self.value = x
        aDict = {}
        # for rests
        aSecondDict = {}
        for key in divisionFactors:
            if x % divisionFactors[key] == 0:
                aDict[key] = True
                aSecondDict[key] = 0
                continue
            aDict[key] = False
            aSecondDict[key] = x % divisionFactors[key]
        self.whoCanDivide = deepcopy(aDict)
        self.rests = deepcopy(aSecondDict)

    def add(self, addition):
        for key in divisionFactors:
            self.rests[key] = (self.rests[key] + addition) % divisionFactors[key]
            if self.rests[key] == 0:
                self.whoCanDivide[key] = True
                continue
            self.whoCanDivide[key] = False

    def multiply(self, multiplier):
        for key in divisionFactors:
            if multiplier == 'old':
                multiplier = self.rests[key]
            self.rests[key] = (self.rests[key] * int(multiplier)) % divisionFactors[key]
            if self.rests[key] == 0:
                self.whoCanDivide[key] = True
                continue
            self.whoCanDivide[key] = False


class Monkey():
    number = int
    startingItems = [int]
    factors = []
    division = int
    throwsTo = dict()
    inspected = 0

    def __init__(self, lines: list):
        self.number = int(re.search('[0-9]+', lines[0]).group())
        # self.startingItems = [Item(int(item)) for item in re.findall('[0-9]+', lines[1])]
        self.factors = lines[2].split('= ')[1].split(' ')
        self.division = int(re.search('[0-9]+', lines[3]).group())
        firstMonkey = int(re.search('[0-9]+', lines[4]).group())
        secondMonkey = int(re.search('[0-9]+', lines[5]).group())
        self.throwsTo = {True: firstMonkey, False: secondMonkey}
        # print(self.throwsTo)

    def catch(self, item: Item) -> None:
        self.startingItems.append(item)
        # print(f'Caught item, new list: {self.startingItems}')

    def throw(self, item: Item, monkey) -> None:
        monkey.catch(item)

    def inspect(self, item: Item) -> Item:
        # print(f'Inspecting {item}')
        self.inspected += 1
        _, sign, secondNum = self.factors
        if sign == '+':
            item.add(int(secondNum))
        else:
            item.multiply(secondNum)
        # print(f"After inspection: {newValue}")
        # newValue = newValue//3
        # print(f"After division: {newValue}")
        return item

    def round(self) -> None:
        global MONKEYS
        for _ in range(len(self.startingItems)):
            # print(f'Taking item {self.startingItems[0]}')
            currentItem = self.inspect(self.startingItems.pop(0))
            condition = currentItem.whoCanDivide[self.number]
            # print(f'Throwing {currentItem} to monkey {self.throwsTo[condition]}')
            self.throw(currentItem, MONKEYS[self.throwsTo[condition]])


for lines in input:
    # print(f'Initing {monkey[0]}')
    monkey = Monkey(lines)
    divisionFactors[monkey.number] = monkey.division
    MONKEYS.append(monkey)

items = []
for lines in input:
    items.append([Item(int(item)) for item in re.findall('[0-9]+', lines[1])])

for monkey in MONKEYS:
    monkey.startingItems = items.pop(0)

rounds = 10000
inspections = []
for i in range(rounds):
    print(f'Round {i + 1}')
    for monkey in MONKEYS:
        monkey.round()
        if i == rounds - 1:
            inspections.append(monkey.inspected)
print(inspections)
print(sorted(inspections, reverse=True)[0] * sorted(inspections, reverse=True)[1])



