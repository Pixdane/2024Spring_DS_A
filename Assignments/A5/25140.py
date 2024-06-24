#25140:根据后序表达式建立表达式树
class Repr:
    def __init__(self, op, arg1, arg2):
        self.op, self.arg1, self.arg2 = op, arg1, arg2

def parse_input(l):
    stack = []
    for item in l:
        if item.islower():
            stack.append(item)
        else:
            stack.append(Repr(item, stack.pop(), stack.pop()))
    return stack[-1]

def parse_tree(repr_list):
    if repr_list == []:
        return ''
    res = ''
    stack = []
    for repr_ in repr_list:
        if isinstance(repr_, Repr):
            res += repr_.op
            stack.append(repr_.arg2)
            stack.append(repr_.arg1)
        else:
            res += repr_
    return res + parse_tree(stack)

n = int(input())
for _ in range(n):
    my_repr = parse_input(input())
    print(parse_tree([my_repr])[::-1])
