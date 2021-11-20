for A in range(1000,1,-1):
    flog = 1
    for x in range(1,100):
        for y in range(1,100):
            if (((x > 9) or (x**2<=A)) and ((y**2 > A)or(y<=9))) == 0:
                flog = 0
                break
    if flog == 1:
        print(A)
        break



