def print_multiplication_table(table=4, start=1, end=10):
    for i in range(start, end+1):
        print(f"{table} X {i} = {table*i}")


def sum_of_numbers(num1, num2):
    sum = num1 + num2
    return sum


#print_multiplication_table()


print(sum_of_numbers(10, 20))