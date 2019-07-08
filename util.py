import itertools
import random


class Mastermind:

    def __init__(self, colors=6, pegs=4):
        self.colors = colors
        self.pegs = pegs

    def compare(self, code1, code2):
        correct = sum(1 for i in range(len(code1)) if code1[i] == code2[i])
        wrong = sum(min(code1.count(n), code2.count(n)) for n in range(self.colors)) - correct
        return correct, wrong

    def get_codes(self):
        return list(itertools.product(*[range(self.colors) for _ in range(self.pegs)]))

    def get_random_code(self):
        return random.choice(self.get_codes())

    def start_game(self, code=None, first_attempt=None):
        pass
