R = set()
for N in range(10, 1000):
    N2 = bin(N)
    N2 = int(N2[3:])
    R.add(N - int(str(N2), 2))
print(R)