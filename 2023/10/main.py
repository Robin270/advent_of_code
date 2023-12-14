import aoc_utils

# Init
data = aoc_utils.import_rows()
for row, i in enumerate(data):
    if "S" in i: start = (i.index("S"), row)

# Part 1
start_options = aoc_utils.get_neighbours(start[0], start[1], data, as_tuple=True)
two_way_start = []
for i in start_options:
    dir = aoc_utils.get_neighbour_direction(start, i)
    if (dir == "N" and data[i[1]][i[0]] in ("7", "F", "|")) or (dir == "S" and data[i[1]][i[0]] in ("L", "J", "|")) or (dir == "E" and data[i[1]][i[0]] in ("J", "7", "-")) or (dir == "W" and data[i[1]][i[0]] in ("F", "L", "-")): two_way_start.append(i)
visited = {}
for s in two_way_start:
    previous = start
    current = s
    distance = 1
    while True:
        if not current in visited.keys(): visited[current] = [distance]
        else: visited[current].append(distance)
        distance += 1
        match data[current[1]][current[0]]:
            case "|": way = ["N", "S"]
            case "-": way = ["W", "E"]
            case "7": way = ["W", "S"]
            case "F": way = ["E", "S"]
            case "L": way = ["E", "N"]
            case "J": way = ["W", "N"]
        way.remove(aoc_utils.get_neighbour_direction(current, previous))
        way = way[0]
        previous = current
        options = aoc_utils.get_neighbours(current[0], current[1], data, as_tuple=True)
        for i in options:
            if aoc_utils.get_neighbour_direction(current, i) == way: current = i; break
        if current == start: break
distances = []
for i in visited.items(): distances.append(min(i[1]))
part_1 = max(distances)

# Part 2
part_2 = None


# Results
aoc_utils.print_results(part_1, part_2)
