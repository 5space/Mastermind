def get_hint(code, attempt, choices):
    correct = sum(1 for i in range(len(code)) if code[i] == attempt[i])
    wrong = sum(min(code.count(n), attempt.count(n)) for n in choices) - correct
    return correct, wrong


"""
class RandomAlgorithm:

    def __init__(self, gametype, code):
        self.gametype = gametype

    def get_hint(code, attempt):
        correct = sum(1 for i in range(len(code)) if code[i] == attempt[i])
        wrong = sum(min(code.count(n), attempt.count(n)) for n in range(gametype[0])) - correct
        return correct, wrong
"""
