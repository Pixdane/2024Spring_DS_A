nn, a, b, c = input().split()
n = int(nn)

pows = [list(range(n, 0, -1)), [], []]
names = {0: a, 1: b, 2: c}

def move(source, destination, vacancy, num):
    if num == 0:
        return

    move(source, vacancy, destination, num - 1)

    print(f"{pows[source][-1]}:{names[source]}->{names[destination]}")
    pows[destination].append(pows[source].pop())

    move(vacancy, destination, source, num - 1)

move(0, 2, 1, n)
