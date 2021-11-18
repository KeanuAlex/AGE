# лучше решать руками
P = [i for i in range(22, 73)]
Q = [i for i in range(42, 103)]
A = []
for x in range(1, 110):
    if (x in P) and not (x in Q):
        A.append(x)
print(len(A))
