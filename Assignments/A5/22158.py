#22158:根据二叉树前中序序列建树
def parse(pre, mid):
    if mid == '':
        return ''
    if len(mid) == 1:
        return mid[0]
    root = pre[0]
    root_index = mid.find(root)
    return parse(pre[1:root_index + 1], mid[:root_index]) + parse(pre[root_index + 1:], mid[root_index + 1:]) + root

while 1:
    try:
        print(parse(input(), input()))
    except EOFError:
        break
