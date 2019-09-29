"""
Given a list create a new list such that each element is the product of all
the other elements, not including itself

If there is only one zero in the list, that element will be the only one with
a value.

If there are more than one zeros in the list, then every element will be zero

If the list has 1 or less elements the result is [0]
"""
import random
from functools import reduce

def main():
    """
    Main driver, sets up the list and calls the function to apply the changes
    """
    random_list = random.sample(range(10), 5) + random.sample(range(10), 5)
    print(random_list)

    if len(random_list) <= 1:
        print([0])
    else:
        new_list = apply_product(random_list)
        print(new_list)

    print("One Liner no division")
    print([reduce(lambda a, b: a *b,
                  [ y for x, y in enumerate(random_list) if x != idx])
           for idx, _ in enumerate(random_list)])

def apply_product(the_list):
    """
    takes a list and determines if there are any zeros

    if there is 1 zero it does a product of the rest of the elements
    and stores it in the one with the zero position and sets the rest to
    zero.

    if there are 2 or more zeros then it simply fills the new list with zeros

    If there are no zeros then it calculates the product of all numbers
    and stores product / the element value
    """
    zero_count = the_list.count(0)
    if zero_count == 1:
        # only one will have a value
        prod = 1
        for non_zero_element in (non_zero_element for non_zero_element
                                 in the_list if non_zero_element):
            prod *= non_zero_element

        new_list = [prod if not element else 0 for element in the_list]
    elif zero_count > 1:
        # all values will be 0
        new_list = [0 for element in the_list]
    else:
        # each value will be product of the list divided by it
        prod = 1
        for element in the_list:
            prod *= element

        new_list = [prod / element for element in the_list]

    return new_list


if __name__ == "__main__":
    main()
