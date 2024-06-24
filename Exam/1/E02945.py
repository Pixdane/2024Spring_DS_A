k = int(input())
ms = [int(x) for x in input().split()]

def find_max(xs, sup=None):
    if xs == []:
        return 0
    if sup == None:
        return max(1 + find_max(xs[1:], xs[0]), find_max(xs[1:]))
    if xs[0] > sup:
        return find_max(xs[1:], sup)
    return max(1 + find_max(xs[1:], xs[0]), find_max(xs[1:], sup))

print(find_max(ms))
