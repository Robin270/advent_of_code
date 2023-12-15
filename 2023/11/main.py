import aoc_utils

# Init
data = [[i for i in row] for row in aoc_utils.import_rows()]

# Part 1 & Part 2
exclude = [[], []]
for index, i in enumerate(data):
    if index in exclude[0]: continue
    if not "#" in i: data.insert(index+1, i); exclude[0].append(index+1)
index = -1
while index < len(data[0])-1:
    index += 1
    if index in exclude[1]: continue
    is_empty = True
    for row in range(0, len(data)):
        if data[row][index] == "#": is_empty = False; break
    if not is_empty: continue
    for row in range(0, len(data)): data[row].insert(index+1, ".")
    exclude[1].append(index+1)
counter = 1
for row, i in enumerate(data):
    for index, j in enumerate(i):
        if j == "#": data[row][index] = str(counter); counter += 1
galaxies, distances = {}, [{}, {}]
for row, i in enumerate(data):
    for index, j in enumerate(i):
        if j.isdigit():
            num, next = j, 1
            while index+next < len(data[row]) and data[row][index+next].isdigit(): num += data[row][index+next]
            galaxies[int(num)] = (index, row)
for galaxy in range(1, counter):
    for pair in range(galaxy+1, counter): distances[0][(galaxy, pair)] = abs(galaxies[galaxy][0]-galaxies[pair][0])+abs(galaxies[galaxy][1]-galaxies[pair][1])
part_1 = sum(distances[0].values())
for galaxy in range(1, counter):
    for pair in range(galaxy+1, counter):
        base_dist = abs(galaxies[galaxy][0]-galaxies[pair][0])+abs(galaxies[galaxy][1]-galaxies[pair][1])
        adj_dist = 0
        for e, i in enumerate(exclude):
            for j in i:
                if e == 0:
                    r = range(galaxies[galaxy][1], galaxies[pair][1])
                    if len(r) == 0: r = range(galaxies[pair][1], galaxies[galaxy][1])
                    if j-1 in r: adj_dist += 999998
                elif e == 1:
                    r = range(galaxies[galaxy][0], galaxies[pair][0])
                    if len(r) == 0: r = range(galaxies[pair][0], galaxies[galaxy][0])
                    if j-1 in r: adj_dist += 999998
        distances[1][(galaxy, pair)] = base_dist + adj_dist
part_2 = sum(distances[1].values())

# Results
aoc_utils.print_results(part_1, part_2)
