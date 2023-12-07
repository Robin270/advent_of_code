import aoc_utils
from typing import Final

# Init
data = []
with open("input.in", "r") as input_data:
    while True:
        row = input_data.readline().strip().split(" ")
        if row == [""]: break
        data.append({"cards": row[0], "bid": int(row[1])})
data2 = data.copy()
CARDS: Final[list[str]] = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
CARDS2: Final[list[str]] = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
HAND_TYPES: Final[list[str]] = ["five of a kind", "four of a kind", "full house", "three of a kind", "two pair", "one pair", "high card"]

# Part 1
part_1 = 0
for index, i in enumerate(data):
    cards_count = dict()
    for c in i["cards"]:
        if c not in cards_count.keys(): cards_count[c] = 1
        else: cards_count[c] += 1
    cards_sum = list(cards_count.values())
    cards_sum.sort(reverse=True)
    match cards_sum:
        case [5]: hand_type = HAND_TYPES[0]
        case [4, 1]: hand_type = HAND_TYPES[1]
        case [3, 2]: hand_type = HAND_TYPES[2]
        case [3, 1, 1]: hand_type = HAND_TYPES[3]
        case [2, 2, 1]: hand_type = HAND_TYPES[4]
        case [2, 1, 1, 1]: hand_type = HAND_TYPES[5]
        case [1, 1, 1, 1, 1]: hand_type = HAND_TYPES[6]
    i["type"] = hand_type
    data[index] = i
data.sort(key=lambda hand: (HAND_TYPES.index(hand["type"]), *[CARDS.index(c) for c in hand["cards"]]))
data.reverse()
for index, i in enumerate(data): part_1 += i["bid"]*(index+1)

# Part 2
part_2 = 0
for index, i in enumerate(data2):
    cards_count = dict()
    jokers = 0
    for c in i["cards"]:
        if c=="J": jokers+=1; continue
        elif c not in cards_count.keys(): cards_count[c] = 1
        else: cards_count[c] += 1
    cards_count2 = list(cards_count.items())
    cards_count2.sort(key=lambda x: (-x[1], CARDS2.index(x[0])))
    cards_sum = [x[1] for x in cards_count2]
    cards_sum.sort(reverse=True)
    if cards_sum == []: cards_sum = [jokers]
    else: cards_sum[0] += jokers
    match cards_sum:
        case [5]: hand_type = HAND_TYPES[0]
        case [4, 1]: hand_type = HAND_TYPES[1]
        case [3, 2]: hand_type = HAND_TYPES[2]
        case [3, 1, 1]: hand_type = HAND_TYPES[3]
        case [2, 2, 1]: hand_type = HAND_TYPES[4]
        case [2, 1, 1, 1]: hand_type = HAND_TYPES[5]
        case [1, 1, 1, 1, 1]: hand_type = HAND_TYPES[6]
    i["type"] = hand_type
    data2[index] = i
data2.sort(key=lambda hand: (HAND_TYPES.index(hand["type"]), *[CARDS2.index(c) for c in hand["cards"]]))
data2.reverse()
for index, i in enumerate(data2): part_2 += i["bid"]*(index+1)

# Results
aoc_utils.print_results(part_1, part_2)
