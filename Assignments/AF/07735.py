# 07735:道路
import heapq


class Graph:
    def __init__(self, n):
        self.connected_vertex = {i: [] for i in range(1, n + 1)}

    def connect(self, point1, point2, weight, cost):
        self.connected_vertex[point1].append((point2, weight, cost))

    def dijkstra(self, start, end):
        heap = [(0, start, K, [])]
        while len(heap) > 0:
            d, city, c, passed = heapq.heappop(heap)
            if city == end:
                return d
            for point, edge_weight, cost in self.connected_vertex[city]:
                if point not in passed and c >= cost:
                    heapq.heappush(
                        heap, (d + edge_weight, point, c - cost, [*passed, city]))
        return -1


K = int(input())
N = int(input())
R = int(input())
graph = Graph(N)
for _ in range(R):
    graph.connect(*(int(i) for i in input().split()))
print(graph.dijkstra(1, N))
