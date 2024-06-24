#E02808:校门外的树

l, m = map(int, input().split())

result = [1] * (l + 1)

for i in range(m):
    start, stop = map(int, input().split())
    for j in range(start, stop + 1):
        result[j] = 0

print(sum(result))
