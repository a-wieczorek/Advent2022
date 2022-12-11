with open('inputs//day9-input.txt', 'r') as f:
    moves = f.read().split('\n')

positions = []
tail_visited_coords = []

def add_lists(toChange, change):
    toChange = [toChange[0] + change[0], toChange[1] + change[1]]
    return toChange


def move_main(movement):
    global positions
    positions[0] = add_lists(positions[0], movement)
    for i in range(1, len(positions)):
        rel_tail_pos = add_lists(positions[i], [-coord for coord in positions[i-1]])
        if any([abs(coordinate)>1 for coordinate in rel_tail_pos]):
            move_follower(movement, rel_tail_pos, i)
    return


def move_follower(movement, rel_tail_pos, i):
    global tail_visited_coords, positions
    x, y = rel_tail_pos
    if x!= 0:
        x = x - 1 if x > 0 else x + 1
    if y != 0:
        y = y - 1 if y > 0 else y + 1
    rel_tail_pos = [x, y]
    positions[i] = add_lists(positions[i-1], rel_tail_pos)
    if i == len(positions)-1:
        tail_visited_coords.append(positions[i])
    return


def main(knots):
    global tail_visited_coords, positions
    switch = {'R': [1,0],
              'L': [-1,0],
              'U': [0,1],
              'D': [0,-1]}

    tail_visited_coords = [[0,0]]
    positions = [[0,0]]*knots
    
    for move in moves:
        direction, amount = move.split(' ')
        for _ in range(int(amount)):
            move_main(switch[direction])

    coords = []
    for visited in tail_visited_coords:
        if visited not in coords:
            coords.append(visited)
            
    print(len(coords))

#part_one
main(2)
#part_two
main(10)

