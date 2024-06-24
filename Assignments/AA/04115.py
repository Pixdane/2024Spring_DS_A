# 04115:鸣人和佐助
from collections import deque

m, n, t = map(int, input().split())
traversed = set()
bfs = deque()
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
grid = [[-1 for _ in range(n)] for _ in range(m)]
value = [[-1 for _ in range(n)] for _ in range(m)]
time = [[-1 for _ in range(n)] for _ in range(m)]

for i in range(m):
    for j, char in enumerate(input()):
        if char in ('*', '+', '@'):
            grid[i][j] = 0
        if char == '+':
            start = (i, j)
            value[i][j] = t
            time[i][j] = 0
        if char == '@':
            end = (i, j)

traversed.add(start)
bfs.append(start)

while len(bfs) > 0:
    point = bfs.popleft()
    for dx, dy in directions:
        if point[0] + dx >= m or point[0] + dx < 0 or point[1] + dy >= n or point[1] + dy < 0:
            continue

        next_move = (point[0] + dx, point[1] + dy)
        new_value = (value[point[0]][point[1]]
                     + grid[next_move[0]][next_move[1]])

        if new_value <= value[next_move[0]][next_move[1]] and next_move in traversed:
            continue

        if new_value > value[next_move[0]][next_move[1]]:
            bfs.append(next_move)
            value[next_move[0]][next_move[1]] = new_value
            if time[next_move[0]][next_move[1]] == -1:
                time[next_move[0]][next_move[1]] = time[point[0]][point[1]] + 1
            else:
                time[next_move[0]][next_move[1]] = min(
                    time[next_move[0]][next_move[1]], time[point[0]][point[1]] + 1)

        traversed.add(next_move)

print(time[end[0]][end[1]])
