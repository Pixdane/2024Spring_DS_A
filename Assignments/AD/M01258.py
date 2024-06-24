# M01258:Agri-Net
import heapq
from itertools import product
while 1:
    try:
        N = int(input())
    except EOFError:
        break
    connectivity = [[int(x) for x in input().split()] for _ in range(N)]
    vertices = range(N)
    edges = {x: [] for x in vertices}


    def connect(vertex1, vertex2, w):
        edges[vertex1].append((w, vertex2))
        edges[vertex2].append((w, vertex1))


    for i, j in product(range(N), range(N)):
        if i != j:
            connect(i, j, connectivity[i][j])

    res = 0
    traversed = [0]
    vertices = set(vertices)
    heap = []
    for x in edges[0]:
        heapq.heappush(heap, x)
    while len(traversed) < N and len(heap) > 0:
        minimum_edge = heapq.heappop(heap)
        if minimum_edge[1] not in traversed:
            res += minimum_edge[0]
            for x in edges[minimum_edge[1]]:
                heapq.heappush(heap, x)
            traversed.append(minimum_edge[1])
    print(res)
