# 06646:二叉树的深度

class Tree:
    structure = {}
    def __init__(self, number, *nodes):
        self.__number = number
        Tree.structure[self.__number] = self
        self.__nodes = nodes
    def depth(self):
        if self.__nodes == ('-1', '-1'):
            return 1
        return 1 + max(Tree.structure[i].depth() for i in self.__nodes if i != '-1')

n = int(input())
for i in range(1, n + 1):
    Tree(str(i), *input().split())

print(Tree.structure['1'].depth())
