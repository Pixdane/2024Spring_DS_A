# 20106:走山路
from itertools import product
import heapq

M, N, P = map(int, input().split())
INFINITY = float('inf')
MAP = [[int(x) if x != '#' else INFINITY for x in input().split()]
       for _ in range(M)]


def height(point):
    x, y = point
    return MAP[x][y]


def adjacent_points(point):
    def is_out_of_bound(point):
        x, y = point
        return x < 0 or y < 0

    DIRECTIONS = [(0, -1), (-1, 0)]
    x, y = point
    res = []
    for dx, dy in DIRECTIONS:
        new_point = (x + dx, y + dy)
        if not is_out_of_bound(new_point):
            res.append(new_point)
    return res


def weight(point1, point2):
    return abs(height(point1) - height(point2))


class Graph:
    def __init__(self):
        self.connected_vertex = {(i, j): []
                                 for i, j in product(range(M), range(N))}
        for point in product(range(M), range(N)):
            for adj in adjacent_points(point):
                self.connect(point, adj)

    def connect(self, point1, point2):
        edge_weight = weight(point1, point2)
        self.connected_vertex[point1].append((point2, edge_weight))
        self.connected_vertex[point2].append((point1, edge_weight))

    def dijkstra(self, start, end):
        visited = set()
        heap = [(0, start)]
        distance = {(i, j): INFINITY
                    for i, j in product(range(M), range(N))}
        distance[start] = 0
        while len(visited) < M*N and len(heap) > 0:
            now = heapq.heappop(heap)[1]
            if now in visited:
                continue
            visited.add(now)
            for point, edge_weight in self.connected_vertex[now]:
                if point not in visited and distance[now] + edge_weight <= distance[point]:
                    distance[point] = distance[now] + edge_weight
                    heapq.heappush(heap, (distance[point], point))
        return distance[end] if distance[end] != INFINITY else 'NO'


graph = Graph()
for _ in range(P):
    x1, y1, x2, y2 = map(int, input().split())
    print(graph.dijkstra((x1, y1), (x2, y2)))
