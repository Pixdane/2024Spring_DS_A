# 05443:兔子与樱花
import heapq

INFINITY = float('inf')


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.connected_vertex = {vertex: [] for vertex in self.vertices}
        self.num_vertices = len(self.vertices)

    def connect(self, point1, point2, weight):
        self.connected_vertex[point1].append((point2, weight))
        self.connected_vertex[point2].append((point1, weight))

    def dijkstra(self, start, end):
        if start == end:
            return start
        visited = set()
        heap = [(0, start)]
        distance = {vertex: INFINITY for vertex in self.vertices}
        distance[start] = 0
        paths = {}
        while len(visited) < self.num_vertices and len(heap) > 0:
            now = heapq.heappop(heap)[1]
            if now in visited:
                continue
            visited.add(now)
            for point, edge_weight in self.connected_vertex[now]:
                if point not in visited and distance[now] + edge_weight <= distance[point]:
                    distance[point] = distance[now] + edge_weight
                    heapq.heappush(heap, (distance[point], point))
                    paths[point] = (now, f'({edge_weight})')

        def find(end):
            if end == start:
                return []
            return [*find(paths[end][0]), *paths[end]]
        return '->'.join(find(end) + [end])


p = int(input())
vertices = [input() for _ in range(p)]
graph = Graph(vertices)
q = int(input())
for _ in range(q):
    point1, point2, weight = input().split()
    graph.connect(point1, point2, int(weight))
r = int(input())
for _ in range(r):
    print(graph.dijkstra(*input().split()))
