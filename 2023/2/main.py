import aoc_utils
from math import prod

# Init
data = aoc_utils.import_rows()
max_colors = {"red": 12, "green": 13, "blue": 14}

# Part 1 & Part 2
part_1 = 0
part_2 = 0

for row in data:
    row = row.split(": ")
    row[0] = int(row[0].split(" ")[1])
    row[1] = row[1].split("; ")
    for i, j in enumerate(row[1]):
        row[1][i] = j.split(", ")
        for k, h in enumerate(row[1][i]):
            row[1][i][k] = h.split(" ")

    possible = True
    globals_colors = {"red": 0, "green": 0, "blue": 0}
    for a in row[1]:
        local_colors = {"red": 0, "green": 0, "blue": 0}
        for b in a:
            local_colors[b[1]] = int(b[0])
        for x in local_colors:
            globals_colors[x] = local_colors[x] if local_colors[x] > globals_colors[x] else globals_colors[x]
            if local_colors[x] > max_colors[x]: possible = False
    part_2 += prod(globals_colors.values())
    if possible: part_1 += row[0]

# Results
aoc_utils.print_results(part_1, part_2)
