#1364A. XXXXX

def length(n, x, nums):
    if sum(nums) % x:
        return n
    for index in range(1, n + 1):
        if nums[index - 1] % x or nums[- index] % x:
            return n - index
    return -1

t = int(input())

for _ in range(t):
    ni, xi = map(int, input().split())
    print(length(ni, xi, [int(i) for i in input().split()]))
