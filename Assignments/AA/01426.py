#01426:Find The Multiple
from queue import deque
while 1:
    num = int(input())
    if num == 0:
        break
    queue = deque([1])
    while len(queue) > 0:
        i = queue.popleft()
        if i % num == 0:
            print(i)
            break
        queue.append(10 * i)
        queue.append(10 * i + 1)
