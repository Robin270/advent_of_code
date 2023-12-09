import aoc_utils
from math import lcm

# Init
data = {}
with open("input.in", "r") as input_data:
    instructions = input_data.readlines(2)[0].strip()
    for i in input_data.readlines():
        if i=="\n": continue
        i = i.strip().split(" = ")
        i[1] = i[1][1:-1:].split(", ")
        data[i[0]] = {"L": i[1][0], "R": i[1][1]}

# Part 1
part_1 = 0
current1 = "AAA"
while current1 != "ZZZ":
    for i in instructions:
        if current1 != "ZZZ": current1 = data[current1][i]; part_1 += 1
        else: break

# Part 2
part_2 = 0
current2 = [i for i in data.keys() if i[-1] == "A"]
cycles = []
for c in current2:
    cycle = 0
    while c[-1] != "Z":
        cycle += 1
        for i in instructions:
            if c[-1] != "Z": c = data[c][i]
            else: break
    cycles.append(cycle*len(instructions))
part_2 = lcm(*cycles)

# Results
aoc_utils.print_results(part_1, part_2)
