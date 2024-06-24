# 28203:【模板】单调栈

n = int(input())
nums = [int(x) for x in input().split()]
res = ['0'] * n
stack = [1]
for i in range(2, n + 1):
    while stack and nums[i - 1] > nums[stack[-1] - 1]:
        res[stack.pop() - 1] = i
    stack.append(i)

print(' '.join(map(str, res)))
