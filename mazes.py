import numpy as np
from random import randint as r
import pygame

pygame.init()
n = 3
colors = [(51, 51, 51) for i in range(n ** 2)]
reward = np.zeros((n, n))
terminals = []
scrx = n * 100
scry = n * 100
screen = pygame.display.set_mode((scrx, scry))
font = pygame.font.SysFont('arial',45)

def layout(current_position, colors):
    colors[n ** 2 - 1] = (0, 255, 0)
    colors[0] = (0, 0, 255)
    c = 0
    for i in range(0, scrx, 100):
        for j in range(0, scry, 100):
            pygame.draw.rect(screen, (255, 255, 255), (j, i, j + 100, i + 100), 0)
            pygame.draw.rect(screen, colors[c], (j + 10, i + 10, j + 95, i + 95), 0)
            c += 1
            pygame.draw.circle(screen, (255, 255, 0), (current_position[1] * 100 + 50, current_position[0] * 100 + 50), 30, 0)

class mazes():
    def __init__(self):
        self.colors = colors
        self.terminals = terminals
        self.reward = reward

    def getMazeRewards(self):
        reward[0,1] = -10
        reward[2,0] = -10
        reward[2,1] = -10
        return reward

    def getMazeColors(self):
        colors[n * 0 + 1] = (255, 0, 0)
        colors[n * 2 + 1] = (255, 0, 0)
        colors[n * 2 + 0] = (255, 0, 0)
        colors[n * 2 + 2] = (0, 255, 0)
        return colors

    def getMazeTerminals(self):
        terminals.append(n * 0 + 1)
        terminals.append(n * 2 + 1)
        terminals.append(n * 1 + 1)
        return terminals
