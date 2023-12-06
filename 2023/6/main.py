import aoc_utils, re

# Init
data = aoc_utils.import_rows()
records = dict()
times = re.sub("Time: ", "", re.sub(" +", " ", data[0])).split(" ")
distances = re.sub("Distance: ", "", re.sub(" +", " ", data[1])).split(" ")
for i in range(0, len(times)): records[int(times[i])] = int(distances[i])

# Part 1
part_1 = 1
def race(duration: int, results: dict, options: int = 0) -> int:
    for hold in range(1, duration): options = options+1 if hold*(duration-hold) > results[duration] else options
    return options
for i in records.keys(): part_1 *= race(i, records)

# Part 2
new_record = {int("".join(map(str, records.keys()))): int("".join(map(str, records.values())))}
part_2 = race(*new_record.keys(), new_record)

# Results
aoc_utils.print_results(part_1, part_2)
