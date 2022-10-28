
def hello():
    print("Hello User")


def pack(a, b, c):
    return [a, b, c]


def eat_lunch(box):
    if (len(box) == 0):
        print("My lunchbox is empty!")
    else:
        print(f"First I eat {box[0]}")
        i = 1
        while (i < len(box)):
            print(f"Next I eat {box[i]}")
            i += 1


hello()

print(pack(2, "Test", 13))

eat_lunch([])

eat_lunch(["Chips", "Sandwich", "Yogurt"])
