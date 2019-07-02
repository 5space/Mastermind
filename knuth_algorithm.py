import random
import itertools
from util import get_hint


def minimal_value_single_knuth(remaining, attempt, gametype):
    hints = {}
    for code in remaining:
        hint = get_hint(code, attempt, range(gametype[0]))
        if hint not in hints:
            hints[hint] = 1
        else:
            hints[hint] += 1
    return max(hints.values())


def minimal_value_knuth(remaining, gametype):

    scores = {}
    possibilities = list(itertools.product(*[range(gametype[0]) for _ in range(gametype[1])]))
    for attempt in possibilities:
        scores[attempt] = minimal_value_single_knuth(remaining, attempt, gametype)

    minimum = min(scores.values())
    guesses = []
    for attempt in scores:
        if scores[attempt] == minimum:
            guesses.append(attempt)
    return sorted(guesses)


def get_all_hints(gametype):
    for a in range(gametype[1]+1):
        for b in range(gametype[1]+1-a):
            yield (a, b)


def start_game(gametype, c=None):

    remaining = list(itertools.product(*[range(gametype[0]) for _ in range(gametype[1])]))
    code = c or random.choice(remaining)
    moves = 1

    attempt = (0, 0, 1, 1)
    while True:
        hint = get_hint(code, attempt, range(gametype[0]))
        if hint == (gametype[1], 0):
            return code, moves
        remaining = [k for k in remaining if get_hint(k, attempt, range(gametype[0])) == hint]
        moves += 1
        attempt = None
        options = minimal_value_knuth(remaining, gametype)
        for k in options:
            if k in remaining:
                attempt = k
                break
        if attempt is None:
            attempt = options[0]


total = 0
count = 0
if __name__ == "__main__":
    gametype = (6, 4)
    codes = list(itertools.product(*[range(gametype[0]) for _ in range(gametype[1])]))
    for code in codes:
        _, moves = start_game(gametype, code)
        total += moves
        count += 1
        print(f"{''.join(map(str, code))} found in {moves} moves")
print(total/count)
