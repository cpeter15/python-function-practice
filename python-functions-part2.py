

from audioop import lin2adpcm


def arb_args(*args):
    for i in args:
        print(i)


# arb_args(1, 2, 3, 4, 5, 6)


def inner_func(x, y):

    def sum(x, y):
        return x + y

    def sub(x, y):
        return x - y

    print(sum(x, y) + sub(x, y))


# inner_func(4, 6)


def lunch_lady(student_name, preference="Mystery Meat"):
    print(student_name + ': ' + preference)


# lunch_lady("Caleb", "Pizza")
# lunch_lady("Bradley")


def sum_n_product(x, y):
    sum = x + y
    product = x * y

    return sum, product


# print(sum_n_product(3, 5))

alias_arb_args = arb_args

# alias_arb_args(1, 2, 3, 4, 5, 6)


def arb_mean(*args):
    sum = 0
    count = 0
    for i in args:
        sum += i
        count += 1
    print(sum/count)


# arb_mean(1, 2, 3, 4, 5, 6)


def arb_longest_string(*args):
    longest = ''
    for i in args:
        if (len(longest) < len(i)):
            longest = i
    return longest


longest = arb_longest_string(
    'Hello', 'World', 'What\'s', 'up', 'dog', 'longest')

print(longest)
