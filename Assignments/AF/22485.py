# 22485:升空的焰火，从侧面看
class Node:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None


class Tree:
    def __init__(self, n):
        self.nodes = {i: Node(i) for i in range(1, n + 1)}
        self.root = self.nodes[1]
        self.nodes[-1] = None

    def add_child(self, father, lchild, rchild):
        self.nodes[father].lchild = self.nodes[lchild]
        self.nodes[father].rchild = self.nodes[rchild]

    @staticmethod
    def _bfs(layer, result=None):
        if result is None:
            result = []
        if layer == []:
            return [], result
        next_layer = []
        for node in layer:
            if node.lchild is not None:
                next_layer.append(node.lchild)
            if node.rchild is not None:
                next_layer.append(node.rchild)
        return Tree._bfs(next_layer, [*result, layer[-1].key])

    def bfs(self):
        start = [self.root]
        return Tree._bfs(start)[1]


N = int(input())
tree = Tree(N)
for i in range(1, N + 1):
    tree.add_child(i, *map(int, input().split()))
print(' '.join(map(str, tree.bfs())))
