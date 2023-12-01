"""Custom module with utilities. Consists of functions to handle frequently needed subtasks when dealing with AOC"""

def import_rows(day: int) -> list[str]:
    """
    Loads the puzzle input in line-by-line list format.

    :param day: The number of the day. Tries to find an .in file with this name in input_data/ directory
    :type day: int
    :return: List of strings where each element is exactly one line of the source file
    :rtype: list[str]
    """

    with open(f"../input_data/{day}.in", "r") as input_data:
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
