import random
import itertools
from util import Mastermind
from matplotlib import pyplot as plt
import numpy as np


class KnuthAlgorithm(Mastermind):

    def __init__(self, colors=6, pegs=4):
        super().__init__(colors, pegs)
        self.combinations = list(itertools.product(*[range(self.colors) for _ in range(self.pegs)]))
        self.remaining = self.combinations.copy()

    def minimal_value_single_knuth(self, attempt):
        feedbacks = {}
        for code in self.remaining:
            feedback = self.compare(code, attempt)
            if feedback not in feedbacks:
                feedbacks[feedback] = 1
            else:
                feedbacks[feedback] += 1
        return max(feedbacks.values())

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

    def start_game(self, code=None, first_attempt=None):

        self.remaining = self.get_codes()

        code = code or random.choice(self.remaining)
        moves = 1

        attempt = first_attempt or tuple(random.randint(0, self.colors - 1) for _ in range(self.pegs))
        while True:
            feedback = self.compare(code, attempt)
            if feedback == (self.pegs, 0):
                return code, moves
            self.remaining = list(filter(lambda x: self.compare(x, attempt) == feedback, self.remaining))
            moves += 1
            attempt = None
            options = self.minimal_value_knuth()
            for k in options:
                if k in self.remaining:
                    attempt = k
                    break
            if attempt is None:
                attempt = options[0]


if __name__ == "__main__":
    game = KnuthAlgorithm(4, 4)
    codes = game.get_codes()

    total = 0
    count = len(codes)
    results = []
    for c in codes:
        _, m = game.start_game(c, (0, 0, 2, 2))
        print(f"{str().join(map(str, c))} found in {m} moves")
        results.append(m)
        total += m
    print(f"{total}/{count} = {total/count}")
    data = np.array(results)
    d = np.diff(np.unique(data)).min()
    left_of_first_bin = data.min() - float(d) / 2
    right_of_last_bin = data.max() + float(d) / 2
    plt.xlabel("Number of Moves")
    plt.ylabel("Frequency")
    plt.hist(data, np.arange(left_of_first_bin, right_of_last_bin + d, d), alpha=0.5)
    plt.show()
