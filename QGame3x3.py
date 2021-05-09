from mazes import *
from random import randint as r
import random
from time import time,sleep


maze = mazes()


Q = np.zeros((9,4))
actions = {"up": 0, "down": 1, "left": 2, "right": 3}
states = {}
wins = 0
k = 0
for i in range(n):
    for j in range(n):
        states[(i, j)] = k
        k += 1
reward[2,2] = 10

alpha = 0.6
gamma = 0.9
epsilon = 1

current_position = [0, 0]


def select_action(current_state):
    global current_position, epsilon
    possible_actions = []
    if np.random.uniform(0,1) <= epsilon: #exploration
        global ModeFlag
        if current_position[0] != 0:
            possible_actions.append("up")
        if current_position[0] != n - 1:
            possible_actions.append("down")
        if current_position[1] != 0:
            possible_actions.append("left")
        if current_position[1] != n - 1:
            possible_actions.append("right")
        action = actions[possible_actions[r(0, len(possible_actions) - 1)]]
        ModeFlag = True
    else: #Use Q table
        minQ = np.min(Q[current_state])
        if current_position[0] != 0:  # up
            possible_actions.append(Q[current_state, 0])
        else:
            possible_actions.append(minQ - 100)
        if current_position[0] != n - 1:  # down
            possible_actions.append(Q[current_state, 1])
        else:
            possible_actions.append(minQ - 100)
        if current_position[1] != 0:  # left
            possible_actions.append(Q[current_state, 2])
        else:
            possible_actions.append(minQ - 100)
        if current_position[1] != n - 1:  # right
            possible_actions.append(Q[current_state, 3])
        else:
            possible_actions.append(minQ - 100)
        action = random.choice([i for i, a in enumerate(possible_actions) if a == max(
            possible_actions)])
    return action

def epoch(terminals, reward):
    global current_position, epsilon, its, wins, steps, step, last_position, ouches
    current_state = states[(current_position[0], current_position[1])]
    action = select_action(current_state)
    if action == 0:  # move up
        current_position[0] -= 1
    elif action == 1:  # move down
        current_position[0] += 1
    elif action == 2:  # move left
        current_position[1] -= 1
    elif action == 3:  # move right
        current_position[1] += 1
    new_state = states[(current_position[0], current_position[1])]
    if new_state not in terminals:
        Q[current_state, action] += alpha * (reward[current_position[0], current_position[1]] + gamma * (np.max(Q[new_state])) - Q[current_state, action])
        if current_position[0] == 2 and current_position[1] == 2:
            wins += 1
            current_position = [0,0]

    else:
        Q[current_state, action] += alpha * (reward[current_position[0], current_position[1]] + gamma * (np.max(Q[new_state])) - Q[current_state, action])
        if epsilon > 0.1:
            epsilon -= 3e-4  # reducing as time increases to satisfy Exploration & Exploitation Tradeoff

run = True

while run:
    layout(current_position,maze.getMazeColors())
    epoch(maze.getMazeTerminals(), maze.getMazeRewards())
    print(reward)
    #sleep(2)

    pygame.display.flip()
    if wins == 200:
        run = False
print(Q)
pygame.quit()