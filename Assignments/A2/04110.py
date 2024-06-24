#04110: 圣诞⽼⼈的礼物-Santa Clau’s Gifts

n, w = map(int, input().split())
candies = [list(map(int, input().split())) for _ in range(n)]
candies.sort(key=lambda x: x[0] / x[1], reverse=True)

result = 0
weight = 0
for i, j in candies:
    if weight + j < w:
        result += i
        weight += j
    else:
        result += i * (w - weight) / j
        break
print('{:.1f}'.format(result))
