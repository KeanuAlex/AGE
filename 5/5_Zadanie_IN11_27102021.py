for N in range(1, 10000):
    N = str(N)
    summ1 = 0
    summ2 = 0
    for i in N:
        if int(i) % 2 == 0:
            summ1 += int(i)
    for i in range(0, len(N)):
        if (i + 1) % 2 == 0:
            summ2 += int(N[i])

    if abs(summ1 - summ2) == 13:
        print(N)
        break
print(summ1,summ2 )