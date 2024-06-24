while True:
    n, p, m = map(int, input().split())
    if (n, p, m) == (0, 0, 0):
        break
    length = n
    kids = list(range(1, length + 1))
    index = m + p - 1
    res = []
    for i in range(n):
        res.append(str(kids.pop((index % length) - 1)))
        index = index % length + m - 1
        length -= 1
    print(",".join(res))
