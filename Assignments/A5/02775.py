#02775:文件结构“图”
from collections import defaultdict

class Dir:
    tree = defaultdict()
    def __init__(self, dir_name, dss):
        self.ds = dss
        self.name = dir_name
        Dir.tree[self.name] = self
        self.files = []
        self.dirs = []
        self.depth = -1

    def __str__(self):
        prefix = "|     " * self.depth
        res = prefix + self.name + "\n"
        for dirr in self.dirs:
            res += str(dirr)
        for file in sorted(self.files):
            res += (prefix + file + "\n")
        return res

    def add_dir(self, dirr):
        self.dirs.append(dirr)
        dirr.depth = self.depth + 1

    def add_file(self, file):
        self.files.append(file)

ds = 1
a = 2
while 1:
    Dir("ROOT", ds)
    stack = [Dir.tree["ROOT"]]
    stack[-1].depth = 0
    while 1:
        current = input()
        if current in ('#', '*'):
            if current == '#':
                a = 0
            else:
                a = 2
            break
        elif a == 2 and current != '*':
            a = 1
            print(f"DATA SET {ds}:")
        if current[0] == 'd':
            current_dir = Dir(current, ds)
            stack[-1].add_dir(current_dir)
            stack.append(current_dir)
        if current == ']':
            stack.pop()
        if current[0] == 'f':
            stack[-1].add_file(current)
    if a == 0:
        break
    print(Dir.tree["ROOT"])
    ds += 1
