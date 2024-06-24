n = int(input())
timing = list(zip(range(1, n + 1), [int(i) for i in input().split()]))
timing.sort(key=lambda x: x[1])

res = 0
people = n
for person, time in timing:
    people -= 1
    print(person, end=' ')
    res += time * people
print(f"\n{res / n:.2f}")
