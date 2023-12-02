import aoc_utils
from pathlib import Path

# Init
data = aoc_utils.import_rows(Path(__file__).stem)
max_red = 12
max_green = 13
max_blue = 14

# Part 1 & Part 2
part_1 = 0
part_2 = 0

for row in data:
    row = row.split(": ")
    row[0] = row[0].split(" ")[1]
    row[1] = row[1].split("; ")
    for i, j in enumerate(row[1]):
        row[1][i] = j.split(", ")
        for k, h in enumerate(row[1][i]):
            row[1][i][k] = h.split(" ")
    possible = True
    global_red = 0
    global_green = 0
    global_blue = 0
    for a in row[1]:
        local_red = 0
        local_blue = 0
        local_green = 0
        for b in a:
            if b[1] == "red": local_red += int(b[0])
            elif b[1] == "green": local_green += int(b[0])
            elif b[1] == "blue": local_blue += int(b[0])
        if local_red > global_red: global_red = local_red
        if local_green > global_green: global_green = local_green
        if local_blue > global_blue: global_blue = local_blue
        if local_red > max_red or local_green > max_green or local_blue > max_blue: possible = False
    part_2 += global_red*global_green*global_blue
    if possible: part_1 += int(row[0])

# Results
aoc_utils.print_results(part_1, part_2)