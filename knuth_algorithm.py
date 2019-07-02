import random
import itertools
from util import Mastermind


class KnuthAlgorithm(Mastermind):

    def __init__(self, colors=6, pegs=4):
        super().__init__(colors, pegs)
        self.combinations = list(itertools.product(*[range(self.colors) for _ in range(self.pegs)]))
        self.remaining = self.combinations.copy()

    def minimal_value_single_knuth(self, attempt):
        hints = {}
        for code in self.remaining:
            hint = self.compare(code, attempt)
            if hint not in hints:
                hints[hint] = 1
            else:
                hints[hint] += 1
        return max(hints.values())

    def minimal_value_knuth(self):

        scores = {}
        for attempt in self.combinations:
            scores[attempt] = self.minimal_value_single_knuth(attempt)

        minimum = min(scores.values())
        guesses = []
        for attempt in scores:
            if scores[attempt] == minimum:
                guesses.append(attempt)
        return sorted(guesses)

    def start_game(self, code=None):

        self.remaining = list(itertools.product(*[range(self.colors) for _ in range(self.pegs)]))

        code = code or random.choice(self.remaining)
        moves = 1

        attempt = (0, 0, 1, 1)
        while True:
            hint = self.compare(code, attempt)
            if hint == (self.pegs, 0):
                return code, moves
            self.remaining = [k for k in self.remaining if self.compare(k, attempt) == hint]
            moves += 1
            attempt = None
            options = self.minimal_value_knuth()
            for k in options:
                if k in self.remaining:
                    attempt = k
                    break
            if attempt is None:
                attempt = options[0]


total = 0
count = 0
if __name__ == "__main__":
    game = KnuthAlgorithm(6, 4)
    codes = list(itertools.product(*[range(4, 6) for _ in range(4)]))
    for c in codes:
        _, moves = game.start_game(c)
        total += moves
        count += 1
        print(f"{''.join(map(str, c))} found in {moves} moves")
print(total/count)
