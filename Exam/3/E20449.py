# E20449:是否被5整除
inp = input()
res = []
for i in range(len(inp)):
    res.append('1' if int('0b' + inp[:i + 1], base=0) % 5 == 0 else '0')
print(''.join(res))
