def print_lol(a_list, indent=False, level=0):
    """Prints each item in a list, recursively descending
       into nested lists (if necessary)."""

    for each_item in a_list:
        if isinstance(each_item, list):
            print_lol(each_item, True, level + 1)
        else:
            if indent:
                for l in range(level):
                    print("\t")
        print(each_item)


a = [5, 6, 7, 8, 9, 10]

print_lol(a)
