n = int(input())
models= {}
for _ in range(n):
    name, paras = input().split('-')
    if name in models.keys():
        models[name].append(paras)
    else:
        models[name] = [paras]

def sort_paras(a):
    if a[-1] == 'B':
        return [1, float(a[:-1])]
    return [0, float(a[:-1])]

for key in sorted(models.keys()):
    print(f"{key}: {', '.join(sorted(models[key], key=sort_paras))}")
