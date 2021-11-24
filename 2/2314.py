for x in 0,1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if ((not(w) or y) and ((not(x)or z)==(not(y) or x)))==1:
                    print(x,y,z,w)

