for A in range(1,32):
    flag = 1
    for x in range(1,32):
        if ((x & 29 == 0) or((x & 17 != 0)or(x & A != 0))) == 0:
            flag = 0
            break
    if flag == 1:
        print(A)
        break


