x = 4 ** 36 + 3 * 4 ** 20 + 4 ** 15 + 2 * 4 ** 7 + 49
a =set()
while x != 0:
    a.add(x % 16)
    x =  x // 16
print(len(a))