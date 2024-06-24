#22067:快速堆猪
pigs = []
mins = []

def push(weight):
    pigs.append(weight)
    mins.append(min(mins[-1], weight) if len(mins) > 0 else weight)

def pop():
    if len(pigs) > 0:
        pigs.pop()
        mins.pop()

while 1:
    try:
        inp = input().split()
        if inp[0] == "push":
            push(int(inp[1]))
        if inp[0] == "pop":
            pop()
        if inp[0] == "min":
            if len(pigs) > 0:
                print(mins[-1])
    except EOFError:
        break
