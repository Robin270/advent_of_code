"""Custom module with utilities. Consists of functions to handle frequently needed subtasks when dealing with AOC"""

# General purpose
def import_rows() -> list[str]:
    """
    Loads the puzzle input in line-by-line list format from ./input.in file.

    :return: List of strings where each element is exactly one line of the source file
    :rtype: list[str]
    """

    with open("./input.in", "r") as input_data:
        return input_data.read().split("\n")

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
