#24750:根据二叉树中后序序列建树
def parse(mid, post):
    if mid == '':
        return ''
    if len(mid) == 1:
        return mid[0]
    root = post[-1]
    root_index = mid.find(root)
    return root + parse(mid[:root_index], post[:root_index]) + parse(mid[root_index + 1:], post[root_index:-1])

print(parse(input(), input()))
