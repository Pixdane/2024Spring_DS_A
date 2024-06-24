#02255:重建二叉树
def parse(forward, backward):
    if len(forward) == 0:
        return ''
    if len(forward) == 1:
        return forward[0]
    root = forward[0]
    index = backward.find(root)
    return parse(forward[1:index + 1], backward[:index]) + parse(forward[index + 1:], backward[index + 1:]) + root
while 1:
    try:
        forward, backward = input().split()
    except EOFError:
        break
    print(parse(forward, backward))