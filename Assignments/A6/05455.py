#05455:二叉搜索树的层次遍历
class BinarySearchTree:
    depths = {}
    def __init__(self, value, depth=0):
        self.value = value
        self.left_node = None
        self.right_node = None
        self.depth = depth
        BinarySearchTree.depths.setdefault(depth, [])
        BinarySearchTree.depths[depth].append(self.value)

    def insert(self, value):
        if self.value == value:
            return
        if self.value > value:
            if self.left_node is None:
                self.left_node = BinarySearchTree(value, self.depth + 1)
            else:
                self.left_node.insert(value)
        if self.value < value:
            if self.right_node is None:
                self.right_node = BinarySearchTree(value, self.depth + 1)
            else:
                self.right_node.insert(value)

inputs = [int(x) for x in input().split()]
root = BinarySearchTree(inputs[0])
for i in inputs[1:]:
    root.insert(i)

print(*[' '.join([str(j) for j in sorted(i)]) for i in BinarySearchTree.depths.values()])
