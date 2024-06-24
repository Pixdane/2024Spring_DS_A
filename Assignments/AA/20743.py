#20743:整人的提词本
stack = []
inp = input()
for char in inp:
    if char == ')':
        aux = []
        while stack[-1] != '(':
            aux.append(stack.pop())
        stack.pop()
        stack += aux
    else:
        stack.append(char)
print(''.join(stack))
