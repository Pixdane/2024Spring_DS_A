# 09202:舰队、海域出击！
from collections import deque


class Vertex:
    def __init__(self, key):
        self.key = key
        self.next = []
        self.deg_in = 0


class Graph:
    def __init__(self, n):
        self.vertices = {i: Vertex(i) for i in range(1, n + 1)}
        self.n_vertices = n
        self.zero_in = set(self.vertices.values())

    def connect(self, x, y):
        self.vertices[x].next.append(self.vertices[y])
        self.vertices[y].deg_in += 1
        self.zero_in.discard(self.vertices[y])

    def topo(self):
        vs = set(self.vertices.values())
        zero = deque(self.zero_in)
        while len(zero) > 0:
            v = zero.popleft()
            vs.remove(v)
            for next_v in v.next:
                if next_v not in vs:
                    continue
                next_v.deg_in -= 1
                if next_v.deg_in == 0:
                    zero.append(next_v)
        if len(vs) > 0:
            return True
        return False


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    graph = Graph(N)
    for _ in range(M):
        graph.connect(*map(int, input().split()))
    print('Yes' if graph.topo() else 'No')
