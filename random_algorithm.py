import random
import itertools
from util import get_hint


def start_game(gametype):

    remaining = list(itertools.product(*[range(gametype[0]) for _ in range(gametype[1])]))
    code = random.choice(remaining)
    moves = 1

    while True:
        attempt = random.choice(remaining)

        hint = get_hint(code, attempt, range(gametype[0]))
        if hint == (gametype[1], 0):
            return code, moves
        for k in remaining.copy():
            if get_hint(k, attempt, range(gametype[0])) != hint:
                remaining.remove(k)
        moves += 1


if __name__ == "__main__":
    code, moves = start_game((6, 4))
    print(f"Code: {code}")
    print(f"Found in {moves} moves")
