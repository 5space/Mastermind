import random
import itertools
from util import Mastermind


class RandomAlgorithm(Mastermind):

    def __init__(self, colors, pegs):
        super().__init__(colors, pegs)

    def start_game(self, code=None, first_attempt=None):

        remaining = list(itertools.product(*[range(self.colors) for _ in range(self.pegs)]))
        code = code or random.choice(remaining)
        moves = 1

        attempt = first_attempt or random.choice(remaining)
        while True:
            hint = self.compare(code, attempt)
            if hint == (self.pegs, 0):
                return code, moves
            remaining = list(filter(lambda x: self.compare(x, attempt) == hint, remaining))
            moves += 1
            attempt = random.choice(remaining)


game = RandomAlgorithm(6, 4)
if __name__ == "__main__":
    c, m = game.start_game()
    print(f"Code: {c}")
    print(f"Found in {m} moves")
