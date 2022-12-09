with open('../../../Downloads/input.txt', 'r') as f:
    moves = f.read().split('\n')

head_position = [0, 0]
rel_tail_pos = [0, 0]
tail_visited_coords = [[0,0]]

def add_lists(toChange, change):
    toChange = [toChange[0] + change[0], toChange[1] + change[1]]
    return toChange


def move_head(movement):
    global head_position, rel_tail_pos
    head_position = add_lists(head_position, movement)
    rel_tail_pos = add_lists(rel_tail_pos, [-x for x in movement])
    if any([abs(coordinate)>1 for coordinate in rel_tail_pos]):
        move_tail(movement)
    return


def move_tail(movement):
    global rel_tail_pos, tail_visited_coords, head_position
    if rel_tail_pos[0] == 0 or rel_tail_pos[1] == 0:
        rel_tail_pos = add_lists(rel_tail_pos, movement)
    else:
        x, y = rel_tail_pos
        rel_tail_pos = [x - 1 if x > 0 else x + 1, y - 1 if y > 0 else y + 1]  
    tail_visited_coords.append(add_lists(head_position, rel_tail_pos))
    return


switch = {'R': [1,0],
          'L': [-1,0],
          'U': [0,1],
          'D': [0,-1]}

for move in moves:
    direction, amount = move.split(' ')
    for _ in range(int(amount)):
        move_head(switch[direction])

coords = []
for visited in tail_visited_coords:
    if visited not in coords:
        coords.append(visited)
        
print(len(coords))


