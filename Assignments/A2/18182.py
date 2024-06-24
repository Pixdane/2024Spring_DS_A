#18182: 打怪兽

ncases = int(input())
for _ in range(ncases):
    n, m, b = map(int, input().split())
    skills = dict()
    for _ in range(n):
        t, x = map(int, input().split())
        skills.setdefault(t, [])
        skills[t].append(x)
    for i in sorted(skills.keys()):
        b -= sum(sorted(skills[i])[-min(m, len(skills[i])):])
        if b <= 0:
            print(i)
            break
    else:
        print('alive')
