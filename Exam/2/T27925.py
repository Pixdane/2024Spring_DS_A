#T27925:小组队列
n = int(input())
queue = [[] for _ in range(n)]
queues = []
types = {}
for i in range(n):
    for j in input().split():
        types[j] = i

while 1:
    order = input().split()
    if order[0] == "STOP":
        break

    if order[0] == "ENQUEUE":
        queue[types[order[1]]].append(order[1])
        if not types[order[1]] in queues:
            queues.append(types[order[1]])

    if order[0] == "DEQUEUE":
        print(queue[queues[0]].pop(0))
        if queue[queues[0]] == []:
            queues.pop(0)
