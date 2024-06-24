# 28190:奶牛排队
N = int(input())
cows = [int(input()) for _ in range(N)]
monotonic_increasing = []
monotonic_decreasing = []
right_smaller_idx = [N] * N
left_larger_idx = [0] * N

for i in range(N):
    cow = cows[i]
    while monotonic_increasing and cow <= cows[monotonic_increasing[-1]]:
        right_smaller_idx[monotonic_increasing.pop()] = i
    monotonic_increasing.append(i)

for i in range(N - 1, -1, -1):
    cow = cows[i]
    while monotonic_decreasing and cow >= cows[monotonic_decreasing[-1]]:
        left_larger_idx[monotonic_decreasing.pop()] = i
    monotonic_decreasing.append(i)

res = 1

for j in range(N - 1, 0, -1):
    for i in range(left_larger_idx[j] + 1, j):
        if j < right_smaller_idx[i]:
            res = max(res, j - i + 1)

print(res)
