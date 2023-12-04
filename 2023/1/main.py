import aoc_utils, regex
from typing import Final

# Init
data = aoc_utils.import_rows()
WORD_NUMBERS: Final[dict[str, str]] = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

# Part 1 & Part 2
part_1, part_2 = 0, 0

for row in data:
    digits = ""
    for i in row:
        if i.isnumeric(): digits += i
    if digits: part_1 += int(digits[0] + digits[-1])
    digits = ""
    matches = [i for i in regex.finditer("|".join(list(WORD_NUMBERS.keys())), row, overlapped=True)]
    for i, j in enumerate(row):
        if j.isnumeric(): digits += j; continue
        for m in matches:
            if m.span()[0] == i: digits += WORD_NUMBERS[m.group()]
    part_2 += int(digits[0] + digits[-1])

# Results
aoc_utils.print_results(part_1, part_2)
