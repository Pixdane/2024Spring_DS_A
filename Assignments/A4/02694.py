# 02694:波兰表达式
import operator as op

ops = {'+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv}
stack = []

notion = list(map(lambda x: x if x in ops else float(x), input().split()))
notion.reverse()

for i in notion:
    if i in ops:
        stack.append(ops[i](stack.pop(), stack.pop()))
    else:
        stack.append(i)

print(f"{stack[0]:.6f}")
