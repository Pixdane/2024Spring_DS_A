# 05907:二叉树的操作
class Node:
    def __init__(self, key):
        self.key = key
        self.father = None
        self.position = None
        self.children = ()

    def traverse(self):
        if len(self.children) > 0 and self.children[0] is not None:
            return self.children[0].traverse()
        return self


class Tree:
    def __init__(self, number_of_nodes):
        self.nodes = {key: Node(key) for key in range(number_of_nodes)}

    def _node_construct(self, key):
        if key in self.nodes:
            return self.nodes[key]
        return None

    def add_child(self, fkey, lkey, rkey):
        father, lchild, rchild = map(self._node_construct, (fkey, lkey, rkey))
        if father is not None:
            father.children = (lchild, rchild)
        if lchild is not None:
            lchild.father = father
            lchild.position = 0
        if rchild is not None:
            rchild.father = father
            rchild.position = 1

    @staticmethod
    def change_binary_tuple(t, position, x):
        if position == 0:
            return (x, t[1])
        if position == 1:
            return (t[0], x)
        return None

    def swap(self, key1, key2):
        node1, node2 = self._node_construct(key1), self._node_construct(key2)
        node1.father.children = Tree.change_binary_tuple(
            node1.father.children, node1.position, node2)
        node2.father.children = Tree.change_binary_tuple(
            node2.father.children, node2.position, node1)
        node1.father, node2.father = node2.father, node1.father
        node1.position, node2.position = node2.position, node1.position

    def traverse(self, key):
        return self._node_construct(key).traverse().key


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    tree = Tree(n)
    for _ in range(n):
        x, y, z = map(int, input().split())
        tree.add_child(x, y, z)
    for _ in range(m):
        inp_type, *inp = map(int, input().split())
        if inp_type == 1:
            tree.swap(*inp)
        if inp_type == 2:
            print(tree.traverse(inp[0]))
