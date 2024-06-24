#02524:宗教信仰
class Node:
    def __init__(self):
        self.parent = self
        self.rank = 0

class DisjointSet:
    def __init__(self, n):
        self.nodes = [Node() for _ in range(n)]
        self.count = n

    def _find(self, n):
        if n.parent != n:
            n.parent = self._find(n.parent)
        return n.parent

    def find(self, n):
        return self._find(self.nodes[n])

    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u != v:
            if u.rank < v.rank:
                u.parent = v
            else:
                v.parent = u
                if v.rank == u.rank:
                    u.rank += 1
            self.count -= 1

    def __len__(self):
        return self.count
case = 0
while 1:
    case += 1
    n, m = map(int, input().split())
    if (n, m) == (0, 0):
        break
    ds = DisjointSet(n)
    for _ in range(m):
        i, j = map(int, input().split())
        ds.union(i - 1, j - 1)
    print(f"Case {case}: {len(ds)}")
