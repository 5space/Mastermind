def get_hint(code, attempt, choices):
    correct = sum(1 for i in range(len(code)) if code[i] == attempt[i])
    wrong = sum(min(code.count(n), attempt.count(n)) for n in choices) - correct
    return correct, wrong


class Mastermind:

    def __init__(self, colors=6, pegs=4):
        self.colors = colors
        self.pegs = pegs

    def compare(self, code1, code2):
        correct = sum(1 for i in range(len(code1)) if code1[i] == code2[i])
        wrong = sum(min(code1.count(n), code2.count(n)) for n in range(self.colors)) - correct
        return correct, wrong

    def start_game(self, code=None):
        pass
