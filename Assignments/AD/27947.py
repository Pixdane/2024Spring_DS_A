# 27947:动态中位数
import heapq

T = int(input())
for _ in range(T):
    nums = map(int, input().split())
    small = []
    large = []
    res = []
    for idx, num in enumerate(nums):
        if len(small) == len(large):
            if len(small) == 0 or num <= -small[0]:
                heapq.heappush(small, -num)
            else:
                heapq.heappush(large, num)
                heapq.heappush(small, -heapq.heappop(large))
        elif len(small) == len(large) + 1:
            if num >= -small[0]:
                heapq.heappush(large, num)
            else:
                heapq.heappush(small, -num)
                heapq.heappush(large, -heapq.heappop(small))

        if idx % 2 == 0:
            res.append(str(-small[0]))
    print(len(res))
    print(' '.join(res))
