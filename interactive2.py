import pygame
import random


WIDTH = 500
HEIGHT = 250

screen = pygame.display.set_mode((WIDTH, HEIGHT))

COLORS = [(255, 0, 0),
          (255, 255, 0),
          (0, 255, 0),
          (0, 255, 255),
          (0, 0, 255),
          (255, 0, 255),
          (0, 0, 0)]


def get_hint(_code, attempt, choices):
    correct = sum(1 for i in range(len(_code)) if _code[i] == attempt[i])
    wrong = sum(min(_code.count(n), attempt.count(n)) for n in choices) - correct
    return correct, wrong


code = [random.randint(0, 5) for _ in range(4)]
print(code)
guesses = [[-1 for _ in range(4)] for _ in range(12)]
feedbacks = []

moves = 0

while True:
    screen.fill((48, 48, 48))

    pygame.draw.rect(screen, (64, 64, 64), pygame.Rect(50*moves, 0, 50, 250))

    for g in range(len(guesses)):
        for p in range(4):
            pygame.draw.circle(screen, COLORS[guesses[g][p]], (50*g+25, 50*p+25), 20)

    for f in range(len(feedbacks)):
        b, w = feedbacks[f]
        holes = [(50*f+16, 216), (50*f+16, 234), (50*f+34, 216), (50*f+34, 234)]
        pegs = [(0, 0, 0) for _ in range(b)] + [(255, 255, 255) for _ in range(w)]
        for p in range(len(pegs)):
            pygame.draw.circle(screen, pegs[p], holes[p], 7)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if 50*moves+5 < pos[0] < 50*moves+45 and 0 < pos[1] < 200:
                guesses[moves][int(pos[1]/50)] = (guesses[moves][int(pos[1]/50)] + 1) % 6
                # moves += 1
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if -1 not in guesses[moves]:
                    feedbacks.append(get_hint(code, guesses[moves], range(6)))
                    moves += 1

    pygame.event.pump()
    pygame.display.flip()
