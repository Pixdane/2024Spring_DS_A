#27638:求二叉树的高度和叶子数目
from collections import defaultdict

class Node:
    tree = defaultdict()
    def __init__(self, key):
        self.key = key
        self.father = None
        self.children = []
        self.height = -1
        Node.tree[self.key] = self

    def add_child(self, child):
        self.children.append(child)
        child.father = self

    def __str__(self):
        return self.key

    def check_height(self):
        if self.father is None:
            return 0
        if self.height != -1:
            return self.height
        return self.father.check_height() + 1

root = 0
leaves = []

n = int(input())
for index in range(n):
    node = Node(index) if index not in Node.tree else Node.tree[index]
    l, r = map(int, input().split())
    if l == r == -1:
        leaves.append(node)
    else:
        for i in (l, r):
            if i != -1:
                node.add_child(Node(i) if i not in Node.tree else Node.tree[i])

print(max(x.check_height() for x in leaves), len(leaves))
