import re

with open('inputs//day11-input.txt', 'r') as f:
    input = f.read().split('\n\n')
    input = [lines.split('\n') for lines in input]

MONKEYS = []

        
class Monkey():
    startingItems = [int]
    factors = []
    division = int
    throwsTo = dict()
    inspected = 0
    
    def __init__(self, lines: list):
        self.startingItems = [int(item) for item in re.findall('[0-9]+', lines[1])]
        self.factors = lines[2].split('= ')[1].split(' ')
        self.division = int(re.search('[0-9]+', lines[3]).group())
        firstMonkey = int(re.search('[0-9]+', lines[4]).group())
        secondMonkey = int(re.search('[0-9]+', lines[5]).group())
        self.throwsTo = {True: firstMonkey, False: secondMonkey}
        #print(self.throwsTo)

    def catch(self, item: int) -> None:
        self.startingItems.append(item)
        #print(f'Caught item, new list: {self.startingItems}')

    def throw(self, item, monkey) -> None:
        monkey.catch(item)
    
    def inspect(self, item: int) -> int:
        #print(f'Inspecting {item}')
        self.inspected += 1
        firstNum, sign, secondNum = self.factors
        firstNum = int(item) if firstNum == 'old' else int(firstNum)
        secondNum = int(item) if secondNum == 'old' else int(secondNum)
        if sign == '+':
            newValue = firstNum + secondNum
        else:
            newValue = firstNum * secondNum
        #print(f"After inspection: {newValue}")
        newValue = newValue//3
        #print(f"After division: {newValue}")
        return newValue

    def round(self) -> None:
        global MONKEYS
        for _ in range(len(self.startingItems)):
            #print(f'Taking item {self.startingItems[0]}')
            currentItem = self.inspect(self.startingItems.pop(0))
            condition = currentItem%self.division == 0
            #print(f'Throwing {currentItem} to monkey {self.throwsTo[condition]}')
            self.throw(currentItem, MONKEYS[self.throwsTo[condition]])
            
for monkey in input:
    #print(f'Initing {monkey[0]}')
    MONKEYS.append(Monkey(monkey))

#for monkey in MONKEYS:
    #print(monkey.throwsTo)
    #print(monkey.startingItems)

rounds = 20
inspections = []
for i in range(rounds):
    #print(f'Round {i+1}')
    for monkey in MONKEYS:
        monkey.round()
        if i == rounds-1:
            inspections.append(monkey.inspected)
print(inspections)
print(sorted(inspections, reverse=True)[0] * sorted(inspections, reverse=True)[1])
            

        
