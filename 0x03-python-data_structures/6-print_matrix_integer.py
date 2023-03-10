def print_matrix_integer(matrix=[[]]):
    main_len = len(matrix)

    for i in range(0, main_len):
        nested_len = len(matrix[i])
        for j in range(0, nested_len):
            print("{:d} ".format(matrix[i][j]), end="")
        print()


if __name__ == "__main__":
    print_matrix_integer()
