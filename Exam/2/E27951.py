#E27951:机器翻译
cache = []
m, n = map(int, input().split())
res = 0
for now in map(int, input().split()):
    if not now in cache:
        cache.append(now)
        res += 1
        if len(cache) > m:
            cache.pop(0)
print(res)
