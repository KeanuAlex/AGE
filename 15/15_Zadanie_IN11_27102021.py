A = 1
while True:
    count = 0
    for x in range(0, 500):
        if ((x & 85 == 0) <= ((x & 54 != 0) <= (x & A != 0))) == 0:
            count = 1
            break
    if count == 0:
        print(A)
        break
    A += 1