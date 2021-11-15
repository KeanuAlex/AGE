for A in range(1,100): #1,2,3,4,5,6,7...99
    flag = 1
    for x in range(1, 100): #1,2,3,4,5,6,7...99
        if ((x & 25 == 0) or ((x & 17 != 0) or (x & A!= 0))) == 0:
            flag = 0
            break
    if flag == 1:
        print(A)
        break


