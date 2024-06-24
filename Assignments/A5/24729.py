#24729:括号嵌套树
from collections import defaultdict

class Node:
    tree = defaultdict()
    def __init__(self, key, children):
        self.key = key
        Node.tree[self.key] = self
        if children is None:
            self.children = []
        else:
            self.children = children

    def __str__(self):
        return self.key

def parse_parentheses(s):
    def push(obj, l, depth):
        while depth:
            l = l[-1]
            depth -= 1
        l.append(obj)

    groups = []
    depth = 0
    try:
        for char in s:
            if char == '(':
                push([], groups, depth)
                depth += 1
            elif char == ')':
                depth -= 1
            elif char != ',':
                push(char, groups, depth)
    except IndexError as exc:
        raise ValueError('Parentheses mismatch') from exc
    if depth > 0:
        raise ValueError('Parentheses mismatch')
    else:
        return groups

def parse_nodes(l):
    res = []
    for index, node in enumerate(l):
        if isinstance(node, str):
            if index + 1 <= len(l) - 1 and isinstance(l[index + 1], list):
                res.append(Node(node, parse_nodes(l[index + 1])))
            else:
                res.append(Node(node, []))
    return res

def forward(*node):
    res = []
    for i in node:
        res.append(str(i))
        for j in forward(*i.children):
            res.append(j)
    return res

def backward(*node):
    res = []
    for i in node:
        for j in backward(*i.children):
            res.append(j)
        res.append(str(i))
    return res

parsed = parse_parentheses(input())
parse_nodes(parsed)
print(''.join(forward(Node.tree[parsed[0]])))
print(''.join(backward(Node.tree[parsed[0]])))
