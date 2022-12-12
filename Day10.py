with open('inputs//day10-input.txt', 'r') as f:
    commands = f.read().split('\n')

class CPU:
    screen = []
    x = 1
    sprite = [0, 1, 2]
    cycle = 0
    chosen_strengths = []
    checkpointsPart1 = []
    checkpointsPart2 = []

    def __init__(self):
        for i in range(6):
            self.checkpointsPart1.append(20 + (i * 40))
            self.checkpointsPart2.append((i+1) * 40)
            self.screen.append(['']*40)

    def update_register(self, value: int):
        self.x += value
        self.sprite = [self.x-1, self.x, self.x+1]

    def add_cycle(self):
        self.cycle += 1
        self.draw_pixel()
        if self.cycle in self.checkpointsPart1:
            self.chosen_strengths.append(self.x * self.checkpointsPart1.pop(0))

    def noop(self):
        self.add_cycle()

    def addx(self, value: int):
        self.add_cycle()
        self.add_cycle()
        self.update_register(value)

    def signal_strengths(self) -> int:
        return sum(self.chosen_strengths)

    def draw_pixel(self):
        drawPos = self.cycle-1
        for checkpoint in self.checkpointsPart2:
            if drawPos < checkpoint:
                screenLine = self.checkpointsPart2.index(checkpoint)
                drawPos = drawPos - (checkpoint-40) if checkpoint != self.checkpointsPart2[0] else drawPos
                break
        sign = '.'
        if drawPos in self.sprite:
            sign = '#'
        self.screen[screenLine][drawPos] = sign

    def screen_string(self):
        aString = ''
        for screenLine in self.screen:
            aString = aString + ''.join(screenLine) + '\n'
        return aString

cpuUnit = CPU()
for i in range(len(commands)):
    if commands[i].startswith('addx'):
        cpuUnit.addx(int(commands[i].split(' ')[1]))
        continue
    cpuUnit.noop()

print(f"Part 1: {cpuUnit.signal_strengths()}")
print(f"Part 2: \n{cpuUnit.screen_string()}")

