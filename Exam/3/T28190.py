# T28190:奶牛排队
import heapq
n = int(input())
res = 0
mins = []
maxs = []
for _ in range(n):
    num = int(input())
    if len(mins) > 1:
        if mins[0] >= num:
            mins = [num]
            maxs = [-num]
            res = max(res, 1)
        elif maxs[0] > -num:
            heapq.heappush(maxs, -num)
            heapq.heappush(mins, num)
            res = max(res, len(mins))
        elif maxs[0] <= -num:
            heapq.heappush(maxs, -num)
            heapq.heappush(mins, num)
    elif len(mins) == 1:
        if mins[0] >= num:
            mins = [num]
            maxs = [-num]
            res = max(res, 1)
        else:
            heapq.heappush(maxs, -num)
            heapq.heappush(mins, num)
            res = max(res, 2)
    else:
        mins = [num]
        maxs = [-num]

print(res)
