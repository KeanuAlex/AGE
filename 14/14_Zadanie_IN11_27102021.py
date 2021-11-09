chislo = 4 ** 36 + 3 * 4 ** 20 + 4 ** 15 + 2 * 4 ** 7 + 49
chislo = list(hex(chislo))
print(* chislo)
chislo1 = set(chislo[2:])
print(len(chislo1))


for i in chislo1:
    print(f'{i}={chislo[2:].count(i)}')