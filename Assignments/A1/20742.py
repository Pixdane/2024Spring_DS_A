# 20742: 泰波拿契数

from functools import lru_cache

@lru_cache
def tribonacci(index: int) -> int:
    if index == 0:
        return 0
    if index in (1, 2):
        return 1
    return tribonacci(index - 1) + tribonacci(index - 2) + tribonacci(index - 3)

if __name__ == "__main__":
    n = int(input())
    print(tribonacci(n))
