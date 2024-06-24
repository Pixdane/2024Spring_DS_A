#02299:Ultra-QuickSort

import bisect
def inversions_bisect(l: list) -> int:
    ri, res = [], 0
    for i in reversed(range(0, len(l))):
        bs = bisect.bisect_left(ri, l[i])
        res += bs
        ri.insert(bs, l[i])
    return res

while 1:
    if (n := int(input())) == 0:
        break
    print(inversions_bisect([int(input()) for i in range(n)]))
