#18176: 2050年成绩计算
pri = []
t_primes = set()
not_prime = [False] * 10001

for i in range(2, 10000 + 1):
    if not not_prime[i]:
        pri.append(i)
        t_primes.add(i**2)
    for pri_j in pri:
        if i * pri_j > 10000:
            break
        not_prime[i * pri_j] = True
        if i % pri_j == 0:
            break

def mean(l):
    mean_value = sum(l) / len(l)
    if mean_value == 0:
        return 0
    return f"{mean_value:.2f}"

m, n = map(int, input().split())
for _ in range(m):
    print(mean([int(x) if int(x) in t_primes else 0 for x in input().split()]))
