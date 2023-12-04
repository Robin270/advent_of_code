import aoc_utils
from math import prod

# Init
data = aoc_utils.import_rows()

# Part 1 & Part 2
part_1, part_2 = 0, 0

visited = []
for y, row in enumerate(data):
    for x, i in enumerate(row):
        gear_adj = []
        if not i.isdigit() and i != ".":
            neighbours = aoc_utils.get_neighbours(x, y, data, True, True)
            for n in neighbours:
                if data[n[1]][n[0]].isdigit() and (n[0], n[1]) not in visited:
                    visited.append((n[0], n[1]))
                    side_digits = [["", 1], ["", 1]]
                    while n[0] >= side_digits[0][1] and data[n[1]][n[0]-side_digits[0][1]].isdigit() and (n[0]-side_digits[0][1], n[1]) not in visited:
                        side_digits[0][0] += data[n[1]][n[0]-side_digits[0][1]]
                        visited.append((n[0]-side_digits[0][1], n[1]))
                        side_digits[0][1] += 1
                    while n[0]+side_digits[1][1] < len(data[n[1]]) and data[n[1]][n[0]+side_digits[1][1]].isdigit() and (n[0]+side_digits[1][1], n[1]) not in visited:
                        side_digits[1][0] += data[n[1]][n[0]+side_digits[1][1]]
                        visited.append((n[0]+side_digits[1][1], n[1]))
                        side_digits[1][1] += 1
                    if i == "*": gear_adj.append(int(side_digits[0][0][::-1]+data[n[1]][n[0]]+side_digits[1][0]))
                    part_1 += int(side_digits[0][0][::-1]+data[n[1]][n[0]]+side_digits[1][0])
            if len(gear_adj) == 2: part_2 += prod(gear_adj)

# Results
aoc_utils.print_results(part_1, part_2)
