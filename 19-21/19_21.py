N1, TARGET = 9, 75
KADD, KMUL = 3, 2


def gameOver(n1, n2):
    return n1 + n2 >= TARGET


def win(n1, n2, byMove):
    if gameOver(n1, n2): return False
    return lose(n1 + KADD, n2, byMove - 1) or \
           lose(n1 * KMUL, n2, byMove - 1) or \
           lose(n1, n2 + KADD, byMove - 1) or \
           lose(n1, n2 * KMUL, byMove - 1)


def lose(n1, n2, byMove):
    if gameOver(n1, n2): return True
    if byMove == 0: return False
    return win(n1 + KADD, n2, byMove) and \
           win(n1 * KMUL, n2, byMove) and \
           win(n1, n2 + KADD, byMove) and \
           win(n1, n2 * KMUL, byMove)


from math import ceil

ans1 = min(ceil((TARGET - N1) / KMUL / KMUL),
           ceil(TARGET - N1 * KMUL * KMUL))
ans2, ans3 = [], []
for s in range(1, TARGET - N1 + 1):
    if win(N1, s, 2) and not win(N1, s, 1):
        ans2.append(s)
    if lose(N1, s, 2) and not lose(N1, s, 1):
        ans3.append(s)

print("--- Ответы ---")
print("19. ", ans1)
print("20. ", sorted(ans2))
print("21. ", ans3)
