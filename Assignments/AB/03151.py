# 03151:Pots
from collections import deque


def fill1(state):
    return (VOLUME[0], state[1])


def fill2(state):
    return (state[0], VOLUME[1])


def drop1(state):
    return (0, state[1])


def drop2(state):
    return (state[0], 0)


def pour12(state):
    if state[0] > VOLUME[1] - state[1]:
        return (state[0] + state[1] - VOLUME[1], VOLUME[1])
    return (0, state[0] + state[1])


def pour21(state):
    if state[1] > VOLUME[0] - state[0]:
        return (VOLUME[0], state[1] + state[0] - VOLUME[0])
    return (state[0] + state[1], 0)


def find_path(state, depth=0):
    if traversed[state] == ():
        print(depth)
        return
    find_path(traversed[state][0], depth + 1)
    print(traversed[state][1])


METHODS = {fill1: 'FILL(1)', fill2: 'FILL(2)', drop1: 'DROP(1)',
           drop2: 'DROP(2)', pour12: 'POUR(1,2)', pour21: 'POUR(2,1)'}

*VOLUME, TARGET = map(int, input().split())
initial_state = (0, 0)
traversed = {initial_state: ()}
queue = deque()
queue.append(initial_state)
res = None
while len(queue) > 0:
    this = queue.popleft()
    for method, op in METHODS.items():
        now = method(this)
        if now not in traversed:
            traversed[now] = (this, op)
            queue.append(now)
            if TARGET in now:
                res = now
                break
    if res is not None:
        break

if res is None:
    print('impossible')
else:
    find_path(res)
