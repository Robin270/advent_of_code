import aoc_utils

# Init
data = [[int(j) for j in i.split(" ")] for i in aoc_utils.import_rows()]

# Part 1 & Part 2
part_1, part_2 = 0, 0
for k in range(0, 2):
    for row in data:
        if k == 1: row.reverse()
        extrapolated = 0
        diffs = [row]
        diff_source = row
        while True:
            diff = []
            for i in range(0, len(diff_source)-1): diff.append(diff_source[i+1]-diff_source[i])
            if set(diff) == {0}: break
            diff_source = diff
            diffs.append(diff)
        for i in diffs: extrapolated += i[-1]
        if k == 0: part_1 += extrapolated
        else: part_2 += extrapolated

# Results
aoc_utils.print_results(part_1, part_2)
