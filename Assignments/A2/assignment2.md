# Assignment #2: 编程练习

Updated 0953 GMT+8 Feb 24, 2024

2024 spring, Complied by ==同学的姓名、院系==



**说明：**

1）The complete process to learn DSA from scratch can be broken into 4 parts:
- Learn about Time and Space complexities
- Learn the basics of individual Data Structures
- Learn the basics of Algorithms
- Practice Problems on DSA

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知3月1日导入选课名单后启用。**作业写好后，保留在自己手中，待3月1日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



**编程环境**

==（请改为同学的操作系统、编程环境等）==

操作系统：macOS Ventura 13.4.1 (c)

Python编程环境：Spyder IDE 5.2.2, PyCharm 2023.1.4 (Professional Edition)

C/C++编程环境：Mac terminal vi (version 9.0.1424), g++/gcc (Apple clang version 14.0.3, clang-1403.0.22.14.1)



## 1. 题目

### 27653: Fraction类

http://cs101.openjudge.cn/practice/27653/



思路：

类的实现与运算符重载

##### 代码

```python
import math

class Fraction:
    def __init__(self, numerator: int, denominator: int) -> None:
        if denominator == 0:
            raise ZeroDivisionError
        g = math.gcd(numerator, denominator)
        self.numerator = numerator // g
        self.denominator = denominator // g

    def __add__(self, other):
        numerator = self.numerator*other.denominator + self.denominator*other.numerator
        denominator = self.denominator*other.denominator
        return Fraction(numerator, denominator)

    def __str__(self) -> str:
        return f"{self.numerator}/{self.denominator}"

a, b, c, d = map(int, input().split())
print(Fraction(a, b) + Fraction(c, d))

```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240312191054094](https://p.ipic.vip/ppl3xi.png)



### 04110: 圣诞老人的礼物-Santa Clau’s Gifts

greedy/dp, http://cs101.openjudge.cn/practice/04110



思路：

按单位重量价值排序。

##### 代码

```python
n, w = map(int, input().split())
candies = [list(map(int, input().split())) for _ in range(n)]
candies.sort(key=lambda x: x[0] / x[1], reverse=True)

result = 0
weight = 0
for i, j in candies:
    if weight + j < w:
        result += i
        weight += j
    else:
        result += i * (w - weight) / j
        break
print('{:.1f}'.format(result))

```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240312191157000](https://p.ipic.vip/jajrv9.png)



### 18182: 打怪兽

implementation/sortings/data structures, http://cs101.openjudge.cn/practice/18182/



思路：

排序后依次使用技能

##### 代码

```python
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

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240312191305401](https://p.ipic.vip/vb0sn6.png)



### 230B. T-primes

binary search/implementation/math/number theory, 1300, http://codeforces.com/problemset/problem/230/B



思路：只有质数的完全平方数为t-prime。



##### 代码

```python
import math
n = int(input())
ns = map(int, input().split())
 
def is_prime(n : int) -> bool:
    if n == 1:
        return False
    r = range(2, int(math.sqrt(n)) + 1)
    for i in r:
            k = n / i
            if k == int(k):
                return False
    return True
 
 
for i in ns:
    if i == 1000000000000:
        print('NO')
    else:
        n = i ** 0.5
        if n == int(n) and is_prime(n):
            print('YES')
        else:
            print('NO')
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240312191927631](https://p.ipic.vip/y6h0pu.png)



### 1364A. XXXXX

brute force/data structures/number theory/two pointers, 1200, https://codeforces.com/problemset/problem/1364/A



思路：

同时从左和从右遍历列表，满足条件就短路

##### 代码

```python
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

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240312192622338](https://p.ipic.vip/kzh9rp.png)



### 18176: 2050年成绩计算

http://cs101.openjudge.cn/practice/18176/



思路：

欧拉筛打质数表，但由于使用pypy提交一直tle，换成python3提交后马上就ac了。

##### 代码

```python
pri = []
t_primes = set()
not_prime = [False] * 10001

for i in range(2, 10000 + 1):
    if not not_prime[i]:
        pri.append(i)
        t_primes.add(i**2)
    for pri_j in pri:
        if i * pri_j > 10000:
            break
        not_prime[i * pri_j] = True
        if i % pri_j == 0:
            break

def mean(l):
    mean_value = sum(l) / len(l)
    if mean_value == 0:
        return 0
    return f"{mean_value:.2f}"

m, n = map(int, input().split())
for _ in range(m):
    print(mean([int(x) if int(x) in t_primes else 0 for x in input().split()]))

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240312195800781](https://p.ipic.vip/iyl76f.png)



## 2. 学习总结和收获

学习数据结构与算法后，我对oop的理解更加深刻了，同时也接触了一些函数式编程的思路。



