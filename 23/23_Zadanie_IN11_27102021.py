def num(start, x):
    if x < start:
        return 0
    if x == start:
        return 1
    return num(start + 1, x) + num(start * 3, x)


print(num(2, 28) * num(28, 90))
