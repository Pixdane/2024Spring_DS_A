# 28190:奶牛排队
N = int(input())
cows = [int(input()) for _ in range(N)]
monotonic_increasing = [0]
monotonic_decreasing = [0]
res = 1
for b in range(1, N):
    cow = cows[b]
    while monotonic_increasing and cow <= cows[monotonic_increasing[-1]]:
        monotonic_increasing.pop()
    while monotonic_decreasing and cow > cows[monotonic_decreasing[-1]]:
        monotonic_decreasing.pop()
    if monotonic_increasing:
        s = monotonic_increasing[-1]
        for a in monotonic_decreasing:
            if a > s:
                res = max(res, b - a + 1)
                break
    monotonic_increasing.append(b)
    monotonic_decreasing.append(b)

print(res)
