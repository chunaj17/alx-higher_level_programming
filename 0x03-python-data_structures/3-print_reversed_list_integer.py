def print_reversed_list_integer(my_list=[]):
    length = len(my_list) -1

    while (length >= 0):
        print(my_list[length])
        length -= 1


if __name__ == "__main__":
    print_reversed_list_integer()
