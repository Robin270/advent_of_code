import aoc_utils, re

# Init
data = aoc_utils.import_rows("\n\n")

# Part 1
part_1 = []
seeds1 = [int(s) for s in data[0][7::].split(" ")]
maps = []
for index, value in enumerate(data):
    if index == 0: continue
    m = re.sub("^.*:\n", "", value, 1).split("\n")
    for p, s in enumerate(m): m[p] = [int(r) for r in s.split(" ")]
    maps.append(m)
for seed in seeds1:
    for step in range(0, 7):
        for d in maps[step]:
            if seed >= d[1] and seed < d[1]+d[2]: seed = d[0]+(seed-d[1]); break
    part_1.append(seed)
part_1 = min(part_1)

# Part 2 (semi-bruteforce – execution time cca. 15 seconds)
s, seeds2, part_2 = 0, [], []
while s < len(seeds1): seeds2.append(range(seeds1[s], seeds1[s]+seeds1[s+1])); s += 2
locations = maps[-1]
locations.sort(key=lambda x: x[0])
candidate = 0
def reverse_mapping(candidate: int) -> bool:
    for step in range(6, -1, -1):
        for d in maps[step]:
            if candidate >= d[0] and candidate < d[0]+d[2]: candidate = d[1] + (candidate - d[0]); break
    for seed in seeds2:
        if candidate in seed: return True
    return False
while True:
    if not reverse_mapping(candidate): candidate+=1
    else: part_2 = candidate; break

# Result
aoc_utils.print_results(part_1, part_2)
