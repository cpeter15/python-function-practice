from pickle import TRUE


def name_args(**kwargs):
    for i in kwargs.keys():
        print(f"{i}: {kwargs[i]}")

# name_args(a="Writing", b="Python", c="Functions", d="Is", e="Great")


def all_true(iter):
    return all(iter)


def one_true(iter):
    return any(iter)


def recursive_factorial(x):
    if (x < 1):
        return x
    else:
        return x * recursive_factorial(x - 1)


def recursive_deduplicate(str, i=0):

    if (i >= (len(str) - 1) or i < 0):
        return str[i]
    elif (str[i] != str[i + 1]):
        return (str[i] + recursive_deduplicate(str, i + 1))
    else:
        return ("" + recursive_deduplicate(str, i + 1))


# print(recursive_deduplicate("AABCCDDEEEF"))

def recursive_reverse(str):
    if (len(str) == 1):
        return str
    else:
        return str[-1] + recursive_reverse(str[:-1])


print(recursive_reverse("Python"))
