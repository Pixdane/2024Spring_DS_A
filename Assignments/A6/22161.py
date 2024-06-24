#22161:哈夫曼编码树
import heapq

class Char:
    char_dict = {}
    def __init__(self, weight, char):
        self.weight = weight
        self.char = char
        self.chars = [char]
        self.parent = self
        self.code = ''
        Char.char_dict[char] = self

    def __lt__(self, other):
        if self.weight == other.weight:
            return min(self.chars) < min(other.chars)
        else:
            return self.weight < other.weight

class Node:
    def __init__(self, lchild, rchild):
        self.weight = lchild.weight + rchild.weight
        self.children = (lchild, rchild)
        self.parent = self
        self.code = ''
        self.chars = lchild.chars + rchild.chars
        lchild.parent = self
        rchild.parent = self
        self.children[0].code = '0' + self.children[0].code
        self.children[1].code = '1' + self.children[1].code
        if isinstance(self.children[0], Node):
            self.children[0].code_update('0')
        if isinstance(self.children[1], Node):
            self.children[1].code_update('1')

    def code_update(self, code):
        self.children[0].code = code + self.children[0].code
        self.children[1].code = code + self.children[1].code
        if isinstance(self.children[0], Node):
            self.children[0].code_update(code)
        if isinstance(self.children[1], Node):
            self.children[1].code_update(code)

    def __lt__(self, other):
        if self.weight == other.weight:
            return min(self.chars) < min(other.chars)
        else:
            return self.weight < other.weight

heap = []

n = int(input())
for _ in range(n):
    char, weight = input().split()
    heapq.heappush(heap, (int(weight), Char(int(weight), char)))

while len(heap) > 1:
    lchild, rchild = heapq.heappop(heap)[1], heapq.heappop(heap)[1]
    if lchild > rchild:
        lchild, rchild = rchild, lchild
    father = Node(lchild, rchild)
    heapq.heappush(heap, (father.weight, father))
root = heap[0][1]

while 1:
    try:
        inp = input()
        if inp.isdigit():
            pointer = root
            res = []
            for digit in inp:
                pointer = pointer.children[int(digit)]
                if isinstance(pointer, Char):
                    res.append(pointer.char)
                    pointer = root
            print(''.join(res))
        else:
            res = []
            for char in inp:
                res.append(Char.char_dict[char].code)
            print(''.join(res))
    except EOFError:
        break
