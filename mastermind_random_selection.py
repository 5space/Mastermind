import random
import itertools
from util import get_hint


def start_game(gametype):

    remaining = list(itertools.product(*[range(gametype[0]) for t in range(gametype[1])]))
    code = random.choice(remaining)
    moves = 0

    while len(remaining) > 1:
        attempt = random.choice(remaining)
        print(f"Trying {attempt}")

        hint = get_hint(code, attempt, gametype)
        for k in remaining.copy():
            if get_hint(k, attempt, gametype) != hint:
                remaining.remove(k)
        print(f"Result: {hint}, {len(remaining)} possibilities remaining")
        moves += 1

    print(f"Code: {code}")
    print(f"Found in {moves} moves")


if __name__ == "__main__":
    start_game((6, 4))
