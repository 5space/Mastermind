import random
from util import Mastermind
from matplotlib import pyplot as plt
import numpy as np


class RandomAlgorithm(Mastermind):

    def __init__(self, colors, pegs):
        super().__init__(colors, pegs)

    def start_game(self, code=None, first_attempt=None):

        remaining = self.get_codes()
        code = code or random.choice(remaining)
        moves = 1

        attempt = first_attempt or random.choice(remaining)
        while True:
            feedback = self.compare(code, attempt)
            if feedback == (self.pegs, 0):
                return code, moves
            remaining = list(filter(lambda x: self.compare(x, attempt) == feedback, remaining))
            moves += 1
            attempt = random.choice(remaining)


if __name__ == "__main__":
    game = RandomAlgorithm(6, 4)
    results = []
    for a in range(10000):
        results.append(game.start_game()[1])
        if a % 50 == 0:
            print(a)
    data = np.array(results)
    d = np.diff(np.unique(data)).min()
    left_of_first_bin = data.min() - float(d) / 2
    right_of_last_bin = data.max() + float(d) / 2
    plt.xlabel("Number of Moves")
    plt.ylabel("Frequency")
    plt.hist(data, np.arange(left_of_first_bin, right_of_last_bin + d, d), alpha=0.5)
    plt.show()
