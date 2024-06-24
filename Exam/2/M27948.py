#M27948:FBI树
def find_type(s):
    zero = '0' in s
    one = '1' in s
    if zero and one:
        return 'F'
    if zero:
        return 'B'
    if one:
        return 'I'

class Node:
    def __init__(self, type, lchild=None, rchild=None):
        self.lchild = lchild
        self.rchild = rchild
        self.type = type
    def traverse(self):
        l = self.lchild.traverse() if self.lchild != None else ''
        r = self.rchild.traverse() if self.rchild != None else ''
        return l + r + self.type

def tree_parser(s, depth):
    l = len(s)
    if depth < 1:
        return Node(find_type(s))
    return Node(find_type(s), tree_parser(s[:l // 2], depth - 1), tree_parser(s[l // 2:], depth - 1))

n = int(input())
string = input()
print(tree_parser(string, n).traverse())
