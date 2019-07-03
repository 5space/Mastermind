import random
import itertools
from util import Mastermind


class DeterministicAlgorithm(Mastermind):

    def __init__(self, colors, pegs):
        super().__init__(colors, pegs)

    def start_game(self, code=None, first_attempt=None):

        remaining = list(itertools.product(*[range(self.colors) for _ in range(self.pegs)]))
        code = code or random.choice(remaining)
        moves = 1

        attempt = first_attempt or remaining[0]
        while True:
            hint = self.compare(code, attempt)
            if hint == (self.pegs, 0):
                return code, moves
            remaining = list(filter(lambda x: self.compare(x, attempt) == hint, remaining))
            moves += 1
            attempt = remaining[0]


total = 0
count = 0
if __name__ == "__main__":
    game = DeterministicAlgorithm(6, 4)
    codes = list(itertools.product(*[range(6) for _ in range(4)]))
    for c in codes:
        _, moves = game.start_game(c)
        total += moves
        count += 1
        print(f"{str().join(map(str, c))} found in {moves} moves")
print(total/count)
