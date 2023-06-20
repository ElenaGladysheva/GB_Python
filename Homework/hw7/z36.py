def print_operation_table(operation, num_rows=6, num_columns=6):
    for n in range(num_rows):
        for m in range(num_columns):
            print(operation(n + 1, m + 1), end=' ')
        print()

print_operation_table(lambda x,y: x*y)