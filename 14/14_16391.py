x = 49 ** 7 + 7 ** 20 - 28
count6 = 0
while x != 0:
    if x % 7 == 6:
        count6 += 1
    x = x // 7
print(count6)
