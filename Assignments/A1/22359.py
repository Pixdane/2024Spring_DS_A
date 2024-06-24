#22359: Goldbach Conjecture

import math

def is_prime(num: int) -> bool:
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True

def goldbach(num: int):
    for i in range(2, num//2 + 1):
        j = num - i
        if is_prime(i) and is_prime(j):
            return (i, j)

if __name__ == "__main__":
    n = int(input())
    print(*goldbach(n))
