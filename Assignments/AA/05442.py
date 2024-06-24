# 05442:兔子与星空
import heapq
N = int(input())
vertices = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:N]
edges = {x: [] for x in vertices}


def connect(vertex1, vertex2, w):
    edges[vertex1].append((w, vertex2))
    edges[vertex2].append((w, vertex1))


for _ in range(N - 1):
    now, count, *others = map(lambda x: int(x)
                              if x not in vertices else x, input().split())
    for _ in range(count):
        other, weight = others.pop(0), others.pop(0)
        connect(now, other, weight)

res = 0
traversed = ['A']
vertices = set(vertices)
heap = []
for x in edges['A']:
    heapq.heappush(heap, x)
while len(traversed) < N and len(heap) > 0:
    minimum_edge = heapq.heappop(heap)
    if minimum_edge[1] not in traversed:
        res += minimum_edge[0]
        for x in edges[minimum_edge[1]]:
            heapq.heappush(heap, x)
        traversed.append(minimum_edge[1])
print(res)
