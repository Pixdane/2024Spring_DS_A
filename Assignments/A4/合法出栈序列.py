def check(i=-1, j=-1, length=-1):
    if i > minimum:
        if stack and stack[-1] == standard[i]:
            stack.pop()
            i -= 1
        else:
            try:
                stack.append(test[j])
                j -= 1
            except IndexError:
                pass
    else:
        return "YES"
    if len(stack) == length:
        if length == 0:
            return "YES"
        return "NO"
    return check(i, j, len(stack))

standard = input()
while 1:
    try:
        test = input()
        if len(test) != len(standard) or set(test) != set(standard):
            print("NO")
        else:
            minimum = -len(standard)
            stack = []
            i = -1
            j = -1
            print(check())
    except EOFError:
        break
