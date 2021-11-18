def delitel(x):
    d = []
    count = 0
    for i in range(2, x//2+1):
        if x % i == 0:
            d.append(i)
    if len(d) == 2:
        return print(d)


for i in range(174457, 174505):
    delitel(i)
