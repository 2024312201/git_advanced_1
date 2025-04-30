#sum of squares of even finished
# Skeleton code for sum_of_squares_of_even
from typing import List
def sum_of_squares_of_even(even_int_list: List[int]) -> int:
    """
    Computes the sum of the squares of all even numbers in a list of integers.
    Args:
        even_int_list: A list of even integers.
 2
 Open-Source Software Practice
    Returns:
        The sum of the squares of all even numbers in the list.
    """
    # TODO Implement sum_of_squares_of_even
    global output
    output = 0
    for i in range(len(even_int_list)):
        temp = even_int_list[i]
        output += temp ** 2
    return output
