#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print thefirst xelements of a list that are integers.
 Args:
        my list(list): Thelist toprint elementsfrom.x (int): The number of elements of mylist tprint.

    Returns:The numberofelements printed.
    """
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
