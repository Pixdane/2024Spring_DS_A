#T27928:遍历树
class Node:
    values = {}
    def __init__(self, id):
        self.id = id
        self.children = []
        self.father = None
    def set_value(self, value):
        self.value = value
        Node.values[value] = self

    def traverse(self):
        if self.children == []:
            print(self.value)
            return
        l = sorted([self.value] + self.children)
        for item in l:
            if item != self.value:
                Node.values[item].traverse()
            else:
                print(self.value)
        return
childrens = []
n = int(input())
nodes = {index: Node(index) for index in range(n)}
for i in range(n):
    iinput = [int(x) for x in input().split()]
    nodes[i].set_value(iinput[0])
    if len(iinput) > 1:
        nodes[i].children = iinput[1:]
        childrens += iinput[1:]

for i in range(n):
    if not nodes[i].value in childrens:
        nodes[i].traverse()