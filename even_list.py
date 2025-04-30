#even list finished
from typing import List
# Skeleton code for even_list
def even_list(int_list: List[int]) -> List[int]:
    """
    Determines if a number is even and return an even list.
    Args:
        int_list: A list of integer.
    Returns:
        A list of even integers.
    """
    # TODO Implement even_list
    numlist = []
    for i in range(len(int_list)):
        if int_list[i] %2 == 0:
            numlist.append(int_list[i])
    return numlist
