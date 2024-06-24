# 18250:冰阔落 I
class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self


class DisjointSet:
    def __init__(self, n):
        self.nodes = {i: Node(i) for i in range(1, n + 1)}
        self.cups = set(self.nodes)
        self.count = n

    def _find(self, node):
        if node.parent != node:
            node.parent = self._find(node.parent)
        return node.parent

    def find(self, n):
        return self._find(self.nodes[n])

    def union(self, u, v):
        coke_u = self.find(u)
        coke_v = self.find(v)
        if coke_u == coke_v:
            return 'Yes'
        coke_v.parent = coke_u
        self.cups.remove(coke_v.key)
        self.count -= 1
        return 'No'

    def __len__(self):
        return self.count

    def check_empty(self):
        return ' '.join(map(str, sorted(self.cups)))


while 1:
    try:
        nn, m = map(int, input().split())
        cups = DisjointSet(nn)
        for _ in range(m):
            x, y = map(int, input().split())
            print(cups.union(x, y))
        print(len(cups))
        print(cups.check_empty())
    except EOFError:
        break
