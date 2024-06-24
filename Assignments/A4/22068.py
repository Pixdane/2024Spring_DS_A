#22068: 合法出栈序列
index = 0
order = {}
for i in input():
    order[i] = index
    index += 1
while 1:
    try:
        orders = [order[i] for i in input()]
    except EOFError:
        break
    if len(orders) != len(order.values()) or set(orders) != set(order.values()):
        print('NO')
        continue
    stack = [-1]
    original = []
    while orders:
        while orders and orders[-1] < stack[-1]:
            original.append(stack.pop())
        stack.append(orders.pop())
    while len(stack) > 1:
        original.append(stack.pop())
    print(original)
    for j in range(len(original) - 1):
        if original[j] < original[j + 1]:
            print("NO")
            break
    else:
        print("YES")
