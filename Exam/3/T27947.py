# T27947:动态中位数
import heapq
t = int(input())
for _ in range(t):
    h = []
    inp = map(int, input().split())
    for index, num in enumerate(inp):
        print(num)
        heapq.heappush(h, num)
        print(h)
        if index % 2 == 0:
            pass # print(h[0])
