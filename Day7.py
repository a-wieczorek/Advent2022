with open('inputs//day7-input.txt', 'r') as f:
    input = f.read()

def ls(path: str, content: list, structure: dict):
    keys = path.split('#')
    temp = structure
    for key in keys:
        temp = temp[key]
    for value in content:
        if value.startswith('dir'):
            temp[value] = {'name': value[4:], 'files': []}
        else:
            temp['files'].append(value)
    temp['files_size'] = sum([int(x.split(' ')[0]) for x in temp['files']])
    return structure


def get_sizes(sizes, aDict):
    for key in aDict:
        if key.startswith('dir') and 'folder_size' not in aDict[key]:
            get_sizes(sizes, aDict[key])
    folder_size = sum([aDict[a]['folder_size'] for a in aDict if a.startswith('dir')]) + aDict['files_size']
    aDict['folder_size'] = folder_size
    sizes.append([aDict['name'], aDict['folder_size']])


structure = {'dir /': {'name': '/', 'files': []}}
dirSizes = {}
path = 'dir /'

commands = []
file_lists = []
files = []
for line in input.split('\n'):
    if not line.startswith('$'):
        files.append(line)
    else:
        if len(files) > 0:
            file_lists.append(files)
            files = []
        commands.append(line[2:])
    if line == input.split('\n')[-1] and len(files)>0:
        file_lists.append(files)

for command in commands[1:]:
    if command.startswith('cd'):
        if command.split(' ')[1] != '..':
            path = f"{path}#dir {command.split(' ')[1]}"
        else:
            path = '#'.join(path.split('#')[:-1])
    else:
        structure = ls(path, file_lists.pop(0), structure)

sizes = []
get_sizes(sizes, structure['dir /'])

print(sum([x[1] for x in sizes if x[1] <= 100000]))

totalSpace = 70000000
requiredSpace = 30000000
mustDelete = requiredSpace - (totalSpace - structure['dir /']['folder_size'])

smallestDiff = 100000000000

for folder in sizes:
    current = folder[1]-mustDelete
    if current >= 0 and current < smallestDiff:
        smallestDiff = current
        smallestDir = folder[1]

print(smallestDir)





        
