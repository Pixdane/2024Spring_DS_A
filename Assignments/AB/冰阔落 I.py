class DisjointSet:
    father_dict: dict

    def __init__(self, l):
        self.father_dict = {}
        for x in l:
            self.father_dict[x] = x

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
            return 'No\n'
        return 'Yes\n'

    def getUnions(self):
        for x in self.father_dict:
            self.find(x)
        l = sorted(list(set(self.father_dict.values())))
        return str(len(l)) + '\n' + ' '.join([str(x) for x in l])


while 1:
    try:
        n, m = map(int, input().split())
        ds = DisjointSet(range(1, n + 1))
        ans = ''
        for _ in range(m):
            ans += ds.union(*map(int, input().split()))
        print(ans + ds.getUnions())
    except EOFError:
        break
