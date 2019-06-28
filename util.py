def get_hint(code, attempt, choices):
    correct = sum(1 for i in range(len(code)) if code[i] == attempt[i])
    wrong = sum(min(code.count(n), attempt.count(n)) for n in choices) - correct
    return correct, wrong
