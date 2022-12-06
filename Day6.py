with open('inputs//day6-input.txt', 'r') as f:
    input = f.read()

def solve(length):
    marker = input[:length]
    chain = input[length:]
    for character in chain:
        checker = []
        for signal in marker:
            sub = list(marker)
            sub.remove(signal)
            if signal not in sub:
                checker.append(True)
                continue
            checker.append(False)
        if all(checker):
            print(marker)
            print(input.find(marker)+len(marker))
            break
        else:
            marker = marker[1:] + character

solve(4)
solve(14)