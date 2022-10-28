
from itertools import product
from unittest import result


def max_num(x, y, z):
    return max(x, y, z)


print("max_num:")
print(max_num(1, 2, 3))
print(max_num(80, 65, 50))
print(max_num(20, 40, 10))


def mult_list(list):

    if (len(list) == 0):
        return 0

    product = 1
    for i in list:
        product * i
    return product


print("mult_list: ")
print(mult_list([1, 2, 3]))
print(mult_list([]))
print(mult_list([20]))


def rev_string(str):
    i = (len(str) - 1)
    result = ''
    while (i >= 0):
        result += str[i]
        i -= 1
    return result


print("rev_string: ")
print(rev_string(""))
print(rev_string("orange"))
print(rev_string("test string"))


def num_within(x, start, end):
    if (start <= x and x <= end):
        return True
    else:
        return False


print("num_within: ")
print(num_within(9, 8, 12))
print(num_within(10, 3, 10))
print(num_within(6, 1, 4))


def pascal(n):
    triangle = [[1], [1, 1]]

    if (n < 1):
        print("invalid number of rows")
    elif (n == 1):
        print(triangle[0])
    else:
        row_number = 2
        while (len(triangle) < n):
            row = []
            row_prev = triangle[row_number - 1]
            length = len(row_prev) + 1
            for i in range(length):
                if (i == 0):
                    row.append(1)
                elif (i > 0 and i < length - 1):
                    row.append(triangle[row_number-1]
                               [i-1]+triangle[row_number-1][i])
                else:
                    row.append(1)
            triangle.append(row)
            row_number += 1

            for row in triangle:
                print(row)


print("pascal: ")
pascal(1)
pascal(2)
pascal(4)
pascal(6)
