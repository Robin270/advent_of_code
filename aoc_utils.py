from typing import Literal
"""Custom module with utilities. Consists of functions to handle frequently needed subtasks when dealing with AoC"""

# General purpose
def import_rows(sep: str = "\n") -> list[str]:
    """
    Loads the puzzle input in line-by-line list format from ./input.in file.

    :param sep: Separator to use when splitting the data. Default is \\n
    :type sep: str
    :return: List of strings where each element is exactly one line of the source file
    :rtype: list[str]
    """

    with open("./input.in", "r") as input_data: return input_data.read().split(sep)

def print_results(first: str | int | None, second: str | int | None) -> None:
    """
    Prints puzzle answers to the console.

    :param first: The final answer to the first part of the puzzle
    :type first: str | int | None
    :param second: The final answer to the second part of the puzzle
    :type second: str | int | None
    :rtype: None
    """

    print("#"*21)
    print("Part 1 answer:", first if first is not None else "N/A")
    print("Part 2 answer:", second if second is not None else "N/A")
    print("#"*21)

# Specific purpose
def get_neighbours(x: int, y: int, field: list, corners: bool = False, as_tuple: bool = False) -> list[tuple[int, int]] | tuple[tuple[int, int]]:
    """
        Returns positions of neighbouring elements of given coordinates in a 2D list

        :param x: Starting x-coordinate
        :type x: int
        :param y: Starting y-coordinate
        :type y: int
        :param field: A list to operate within
        :type field: list
        :param corners: Whether elements sharing just a corner should be treated as neighbours. False by default
        :type corners: bool
        :param as_tuple: Whether the return value should be a tuple instead of a list. False by default
        :type as_tuple: bool
        :return: A list or a tuple of neighbours' positions
        :rtype: list[tuple[int, int]] | tuple[tuple[int, int]]
    """

    possibilities = [[(x, y-1), (x-1, y), (x+1, y), (x, y+1)], [(x-1, y-1), (x+1, y-1), (x-1, y+1), (x+1, y+1)]]
    neighbours = []
    for i, j in enumerate(possibilities):
        if i == 0 or (i == 1 and corners):
            for k in j:
                if k[1] >= 0 and k[1] < len(field) and k[0] >= 0 and k[0] < len(field[k[1]]): neighbours.append(k)
    return tuple(neighbours) if as_tuple else neighbours

def get_neighbour_direction(base: tuple[int, int], neighbour: tuple[int, int]) -> Literal["N", "NE", "E", "SE", "S",
"SW", "W", "NW"] | None:
    """
        Starting at a specific point, it returns which direction within a 2D field do you have to move to reach a
        specific neighbour (supports diagonal movement)

        :param base: x, y coordinates of the base point
        :type base: tuple[int, int]
        :param neighbour: x, y coordinates of the neighbour
        :type neighbour: tuple[int, int]
        :return: Direction from the base to the neighbour or None when not neighbouring each other
        :rtype: Literal["N", "NE", "E", "SE", "S", "SW", "W", "NW"] | None
    """

    match (base[0]-neighbour[0], base[1]-neighbour[1]):
        case (1, 0): return "W"
        case (-1, 0): return "E"
        case (0, 1): return "N"
        case (0, -1): return "S"
        case (1, 1): return "NW"
        case (1, -1): return "SW"
        case (-1, 1): return "NE"
        case (-1, -1): return "SE"
        case _: return None
