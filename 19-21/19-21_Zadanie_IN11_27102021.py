from functools import lru_cache


def move(x, y):
    return (x + 3, y), (x * 2, y), (x, y + 3), (x, y * 2)


@lru_cache(None)
def game(x, y):
    if x + y >= 75:
        return 'Win'
    if any(game(a, b) == 'Win' for a, b in move(x, y)):
        return 'V1'
    if all(game(a, b) == 'V1' for a, b in move(x, y)):
        return 'P1'
    if any(game(a, b) == 'P1' for a, b in move(x, y)):
        return 'V2'
    if all(game(a, b) == 'V1' or game(a, b) == 'V2' for a, b in move(x, y)):
        return 'P2'


for s in range(1, 66):
    print(s, game(9, s))
