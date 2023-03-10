def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list.copy()
    elif idx > len(my_list) - 1:
        return my_list.copy()
    else:
        my_list[idx] = element
        return my_list


if __name__ == "__main__":
    new_in_list()
