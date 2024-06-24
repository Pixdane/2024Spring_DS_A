# 01182:食物链
class DisjointSet:
    def __init__(self, n):
        self.size = n
        self.father_dict = {}
        self.fake = 0
        for i in range(3 * n):
            self.father_dict[i] = i

    def find(self, x):
        if self.father_dict[x] == x:
            return x
        self.father_dict[x] = self.find(self.father_dict[x])
        return self.father_dict[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            self.father_dict[py] = px
            return 'No'
        return 'Yes'

    def op(self, type_n, a, b):
        if a > self.size or b > self.size:
            self.fake += 1
        elif type_n == 1:
            self.checknmerge(a - 1, b - 1)
        elif type_n == 2:
            self.checknseteat(a - 1, b - 1)

    def checknseteat(self, a, b):
        if self.find(a) == self.find(b) or self.find(a + self.size) == self.find(b):
            self.fake += 1
        else:
            self.seteat(a, b)

    def seteat(self, a, b):
        self.union(a, b + self.size)
        self.union(a + self.size, b + 2*self.size)
        self.union(a + 2*self.size, b)

    def checknmerge(self, a, b):
        if self.find(a) == self.find(b + self.size) or self.find(a + self.size) == self.find(b):
            self.fake += 1
        else:
            self.merge(a, b)

    def merge(self, a, b):
        self.union(a, b)
        self.union(a + self.size, b + self.size)
        self.union(a + 2*self.size, b + 2*self.size)


N, K = map(int, input().split())
ds = DisjointSet(N)
for _ in range(K):
    ds.op(*map(int, input().split()))
print(ds.fake)
