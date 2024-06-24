#04082:树的镜面映射
class Node:
    def __init__(self, id, is_leaf):
        self.id = id
        self.is_leaf = is_leaf
        self.left = None
        self.right = None

    def is_full(self):
        return self.is_leaf == 1 or (self.left is not None and self.right is not None)

    def node_traverse(self):
        if self.left is None or self.left.id == '$':
            next_layer = []
        else:
            next_layer = [self.left]
        if self.right is None or self.right.id == '$':
            return [self.id], next_layer
        res = self.right.node_traverse()
        return res[0] + [self.id], res[1] + next_layer

class Tree:
    def __init__(self):
        self.nodes = {}
        self.root = None

    def add_node(self, id, is_leaf):
        node = Node(id, is_leaf)
        if self.nodes == {}:
            self.root = node
        self.nodes[id] = node
        return self.nodes[id]

    def add_child(self, father, left, right):
        father.left = left
        father.right = right
        return father

    def traverse(self):
        return Tree._traverse(self.root)

    @staticmethod
    def node_parser(xs):
        return xs[0], int(xs[1])

    @staticmethod
    def _traverse(node):
        def flatten(xss):
            return [x for xs in xss for x in xs]
        res = node.node_traverse()
        return flatten(res[0] + [Tree._traverse(node) for node in res[1]])

def stack_parser(xs):
    if len(xs) >= 3 and xs[-1].is_full() and xs[-2].is_full():
        return stack_parser(xs[:-3] + [tree.add_child(xs[-3], xs[-2], xs[-1])])
    return xs

n = int(input())
tree = Tree()
nodes = [tree.add_node(*Tree.node_parser(i)) for i in input().split()]
stack = []
for node in nodes:
    stack.append(node)
    stack = stack_parser(stack)
print(*tree.traverse())
