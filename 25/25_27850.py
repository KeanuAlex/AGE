def prost(vol):
    c = 0
    for i in range(1, vol + 1):
        if vol % i == 0:
            c += 1
    if c == 2:
        return 1


num1 = [x for x in range(245690, 245756)]
for num, vol in enumerate(num1):
    if prost(vol) == 1:
        print(num+1, vol)
