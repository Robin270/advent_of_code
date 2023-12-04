import aoc_utils, re

# Init
data = aoc_utils.import_rows()

# Part 1 & Part 2
part_1, part_2 = 0, 0
copies = dict()

for row, i in enumerate(data):
    data[row] = re.sub("Card( |[0-9]){2,4}: {1,2}", "", data[row])
    data[row] = re.sub(" {2}", " ", data[row])
    data[row] = data[row].split(" | ")
    for index, j in enumerate(data[row]):
        data[row][index] = j.split(" ")
        for index2, k in enumerate(data[row][index]): data[row][index][index2] = int(k)
        data[row][index] = set(data[row][index])
    won = len(data[row][0].intersection(data[row][1]))
    if won > 0:
        part_1 += 2**(won-1)
        instances = copies[row+1]+1 if row+1 in copies.keys() else 1
        for a in range(1, won+1): copies[row+1+a] = copies[row+1+a]+instances if row+1+a in copies.keys() else instances
part_2 = len(data)+sum(copies.values())

# Result
aoc_utils.print_results(part_1, part_2)
