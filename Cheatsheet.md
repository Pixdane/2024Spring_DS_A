# Cheatsheet: Data Structure and Algorithm

2200011765 靳禹安

```py
# pylint: skip-file
```

## 二叉搜索树

## BFS

## DFS

## Dijkstra
```python
import heapq
class Graph:
    def __init__(self, n):
        self.connected_vertex = {i: [] for i in range(1, n + 1)}
    def connect(self, point1, point2, weight):
        self.connected_vertex[point1].append((point2, weight))
    def dijkstra(self, start, end):
        heap = [(0, start, [])]
        while len(heap) > 0:
            distance, v_now, passed = heapq.heappop(heap)
            if v_now == end:
                return distance
            for v_next, edge_weight in self.connected_vertex[v_now]:
                if v_next not in passed:
                    heapq.heappush(
                      heap, 
                      (distance + edge_weight, v_next, [*passed, v_now])
                    )
        return -1

```

## Prim

```python
res = 0
traversed = [0]
vertices = set(vertices)
heap = []
for x in edges[0]:
    heapq.heappush(heap, x)
while len(traversed) < N and len(heap) > 0:
    minimum_edge = heapq.heappop(heap)
    if minimum_edge[1] not in traversed:
        res += minimum_edge[0]
        for x in edges[minimum_edge[1]]:
            heapq.heappush(heap, x)
        traversed.append(minimum_edge[1])
print(res)
```

## 并查集

```py
class Node:
    def __init__(self):
        self.parent = self
        self.rank = 0
class DisjointSet:
    def __init__(self, n):
        self.nodes = [Node() for _ in range(n)]
        self.count = n
    def _find(self, n):
        if n.parent != n:
            n.parent = self._find(n.parent)
        return n.parent
    def find(self, n):
        return self._find(self.nodes[n])
    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u != v:
            if u.rank < v.rank:
                u.parent = v
            else:
                v.parent = u
                if v.rank == u.rank:
                    u.rank += 1
            self.count -= 1
    def __len__(self):
        return self.count
```

## 拓扑排序

```py
from collections import deque
class Vertex:
    def __init__(self, key):
        self.key = key
        self.next = []
        self.deg_in = 0
class Graph:
    def __init__(self, n):
        self.vertices = {i: Vertex(i) for i in range(1, n + 1)}
        self.n_vertices = n
        self.zero_in = set(self.vertices.values())
    def connect(self, x, y):
        self.vertices[x].next.append(self.vertices[y])
        self.vertices[y].deg_in += 1
        self.zero_in.discard(self.vertices[y])
    def topo(self):
        vs = set(self.vertices.values())
        zero = deque(self.zero_in)
        while len(zero) > 0:
            v = zero.popleft()
            vs.remove(v)
            for next_v in v.next:
                if next_v not in vs:
                    continue
                next_v.deg_in -= 1
                if next_v.deg_in == 0:
                    zero.append(next_v)
        if len(vs) > 0:
            return True
        return False
```

## 单调栈

```py
n = int(input())
nums = [int(x) for x in input().split()]
res = ['0'] * n
stack = [1]
for i in range(2, n + 1):
    while stack and nums[i - 1] > nums[stack[-1] - 1]:
        res[stack.pop() - 1] = i
    stack.append(i)
print(' '.join(map(str, res)))
```

## 常用工具

### 处理括号

```py
def parse_parentheses(s):
    def push(obj, l, depth):
        while depth:
            l = l[-1]
            depth -= 1
        l.append(obj)
    groups = []
    depth = 0
    try:
        for char in s:
            if char == '(':
                push([], groups, depth)
                depth += 1
            elif char == ')':
                depth -= 1
            elif char != ',':
                push(char, groups, depth)
    except IndexError as exc:
        raise ValueError('Parentheses mismatch') from exc
    if depth > 0:
        raise ValueError('Parentheses mismatch')
    else:
return groups
```

### heapq

这个模块实现了堆队列算法，即优先队列算法。

堆是一种二叉树，其中每个上级节点的值都小于等于它的任意子节点。 我们将这一条件称为堆的不变性。

这个实现使用了数组，其中对于所有从 0 开始计数的 *k* 都有 `heap[k] <= heap[2*k+1]` 且 `heap[k] <= heap[2*k+2]`。 为了便于比较，不存在的元素将被视为无穷大。 堆最有趣的特性在于其最小的元素始终位于根节点 `heap[0]`。 

这个API与教材的堆算法实现有所不同，具体区别有两方面：（a）我们使用了从零开始的索引。这使得节点和其孩子节点索引之间的关系不太直观但更加适合，因为 Python 使用从零开始的索引。 （b）我们的 pop 方法返回最小的项而不是最大的项（这在教材中称为“最小堆”；而“最大堆”在教材中更为常见，因为它更适用于原地排序）。

基于这两方面，把堆看作原生的Python list也没什么奇怪的： `heap[0]` 表示最小的元素，同时 `heap.sort()` 维护了堆的不变性！

要创建一个堆，可以新建一个空列表 `[]`，或者用函数 [`heapify()`](https://docs.python.org/zh-cn/3/library/heapq.html#heapq.heapify) 把一个非空列表变为堆。

定义了以下函数：

- heapq.**heappush**(*heap*, *item*)

  将 *item* 的值加入 *heap* 中，保持堆的不变性。

- heapq.**heappop**(*heap*)

  弹出并返回 *heap* 的最小的元素，保持堆的不变性。如果堆为空，抛出 [`IndexError`](https://docs.python.org/zh-cn/3/library/exceptions.html#IndexError) 。使用 `heap[0]` ，可以只访问最小的元素而不弹出它。

- heapq.**heappushpop**(*heap*, *item*)

  将 *item* 放入堆中，然后弹出并返回 *heap* 的最小元素。该组合操作比先调用 [`heappush()`](https://docs.python.org/zh-cn/3/library/heapq.html#heapq.heappush) 再调用 [`heappop()`](https://docs.python.org/zh-cn/3/library/heapq.html#heapq.heappop) 运行起来更有效率。

- heapq.**heapify**(*x*)

  将list *x* 转换成堆，原地，线性时间内。

- heapq.**heapreplace**(*heap*, *item*)

  弹出并返回 *heap* 中最小的一项，同时推入新的 *item*。 堆的大小不变。 如果堆为空则引发 [`IndexError`](https://docs.python.org/zh-cn/3/library/exceptions.html#IndexError)。这个单步骤操作比 [`heappop()`](https://docs.python.org/zh-cn/3/library/heapq.html#heapq.heappop) 加 [`heappush()`](https://docs.python.org/zh-cn/3/library/heapq.html#heapq.heappush) 更高效，并且在使用固定大小的堆时更为适宜。 pop/push 组合总是会从堆中返回一个元素并将其替换为 *item*。返回的值可能会比新加入的值大。如果不希望如此，可改用 [`heappushpop()`](https://docs.python.org/zh-cn/3/library/heapq.html#heapq.heappushpop)。它的 push/pop 组合返回两个值中较小的一个，将较大的留在堆中。

该模块还提供了三个基于堆的通用目的函数。

- heapq.**merge**(**iterables*, *key=None*, *reverse=False*)

  将多个已排序的输入合并为一个已排序的输出（例如，合并来自多个日志文件的带时间戳的条目）。 返回已排序值的 [iterator](https://docs.python.org/zh-cn/3/glossary.html#term-iterator)。类似于 `sorted(itertools.chain(*iterables))` 但返回一个可迭代对象，不会一次性地将数据全部放入内存，并假定每个输入流都是已排序的（从小到大）。具有两个可选参数，它们都必须指定为关键字参数。*key* 指定带有单个参数的 [key function](https://docs.python.org/zh-cn/3/glossary.html#term-key-function)，用于从每个输入元素中提取比较键。 默认值为 `None` (直接比较元素)。*reverse* 为一个布尔值。 如果设为 `True`，则输入元素将按比较结果逆序进行合并。 要达成与 `sorted(itertools.chain(*iterables), reverse=True)` 类似的行为，所有可迭代对象必须是已从大到小排序的。*在 3.5 版本发生变更:* 添加了可选的 *key* 和 *reverse* 形参。

- heapq.**nlargest**(*n*, *iterable*, *key=None*)

  从 *iterable* 所定义的数据集中返回前 *n* 个最大元素组成的列表。 如果提供了 *key* 则其应指定一个单参数的函数，用于从 *iterable* 的每个元素中提取比较键 (例如 `key=str.lower`)。 等价于: `sorted(iterable, key=key, reverse=True)[:n]`。

- heapq.**nsmallest**(*n*, *iterable*, *key=None*)

  从 *iterable* 所定义的数据集中返回前 *n* 个最小元素组成的列表。 如果提供了 *key* 则其应指定一个单参数的函数，用于从 *iterable* 的每个元素中提取比较键 (例如 `key=str.lower`)。 等价于: `sorted(iterable, key=key)[:n]`。

后两个函数在 *n* 值较小时性能最好。 对于更大的值，使用 [`sorted()`](https://docs.python.org/zh-cn/3/library/functions.html#sorted) 函数会更有效率。 此外，当 `n==1` 时，使用内置的 [`min()`](https://docs.python.org/zh-cn/3/library/functions.html#min) 和 [`max()`](https://docs.python.org/zh-cn/3/library/functions.html#max) 函数会更有效率。 如果需要重复使用这些函数，请考虑将可迭代对象转为真正的堆。

### deque

示例:

```
>>> from collections import deque
>>> d = deque('ghi')                 # make a new deque with three items
>>> for elem in d:                   # iterate over the deque's elements
...     print(elem.upper())
G
H
I

>>> d.append('j')                    # add a new entry to the right side
>>> d.appendleft('f')                # add a new entry to the left side
>>> d                                # show the representation of the deque
deque(['f', 'g', 'h', 'i', 'j'])

>>> d.pop()                          # return and remove the rightmost item
'j'
>>> d.popleft()                      # return and remove the leftmost item
'f'
>>> list(d)                          # list the contents of the deque
['g', 'h', 'i']
>>> d[0]                             # peek at leftmost item
'g'
>>> d[-1]                            # peek at rightmost item
'i'

>>> list(reversed(d))                # list the contents of a deque in reverse
['i', 'h', 'g']
>>> 'h' in d                         # search the deque
True
>>> d.extend('jkl')                  # add multiple elements at once
>>> d
deque(['g', 'h', 'i', 'j', 'k', 'l'])
>>> d.rotate(1)                      # right rotation
>>> d
deque(['l', 'g', 'h', 'i', 'j', 'k'])
>>> d.rotate(-1)                     # left rotation
>>> d
deque(['g', 'h', 'i', 'j', 'k', 'l'])

>>> deque(reversed(d))               # make a new deque in reverse order
deque(['l', 'k', 'j', 'i', 'h', 'g'])
>>> d.clear()                        # empty the deque
>>> d.pop()                          # cannot pop from an empty deque
Traceback (most recent call last):
    File "<pyshell#6>", line 1, in -toplevel-
        d.pop()
IndexError: pop from an empty deque

>>> d.extendleft('abc')              # extendleft() reverses the input order
>>> d
deque(['c', 'b', 'a'])
```

### defaultdict

使用 [`list`](https://docs.python.org/zh-cn/3/library/stdtypes.html#list) 作为 [`default_factory`](https://docs.python.org/zh-cn/3/library/collections.html#collections.defaultdict.default_factory)，很轻松地将（键-值对组成的）序列转换为（键-列表组成的）字典：

```
>>> s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
>>> d = defaultdict(list)
>>> for k, v in s:
...     d[k].append(v)
...
>>> sorted(d.items())
[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
```

### itertools

**无穷迭代器：**

| 迭代器                                                       | 实参            | 结果                                  | 示例                                  |
| :----------------------------------------------------------- | :-------------- | :------------------------------------ | :------------------------------------ |
| [`count()`](https://docs.python.org/zh-cn/3/library/itertools.html#itertools.count) | [start[, step]] | start, start+step, start+2*step, ...  | `count(10) → 10 11 12 13 14 ...`      |
| [`cycle()`](https://docs.python.org/zh-cn/3/library/itertools.html#itertools.cycle) | p               | p0, p1, ... plast, p0, p1, ...        | `cycle('ABCD') → A B C D A B C D ...` |
| [`repeat()`](https://docs.python.org/zh-cn/3/library/itertools.html#itertools.repeat) | elem [,n]       | elem, elem, elem, ... 重复无限次或n次 | `repeat(10, 3) → 10 10 10`            |

**根据最短输入序列长度停止的迭代器：**

| 迭代器                                                       | 实参                        | 结果                                          | 示例                                                     |
| :----------------------------------------------------------- | :-------------------------- | :-------------------------------------------- | :------------------------------------------------------- |
| [`accumulate()`](https://docs.python.org/zh-cn/3/library/itertools.html#itertools.accumulate) | p [,func]                   | p0, p0+p1, p0+p1+p2, ...                      | `accumulate([1,2,3,4,5]) → 1 3 6 10 15`                  |
| [`batched()`](https://docs.python.org/zh-cn/3/library/itertools.html#itertools.batched) | p, n                        | (p0, p1, ..., p_n-1), ...                     | `batched('ABCDEFG', n=3) → ABC DEF G`                    |
| [`chain()`](https://docs.python.org/zh-cn/3/library/itertools.html#itertools.chain) | p, q, ...                   | p0, p1, ... plast, q0, q1, ...                | `chain('ABC', 'DEF') → A B C D E F`                      |
| [`chain.from_iterable()`](https://docs.python.org/zh-cn/3/library/itertools.html#itertools.chain.from_iterable) | iterable -- 可迭代对象      | p0, p1, ... plast, q0, q1, ...                | `chain.from_iterable(['ABC', 'DEF']) → A B C D E F`      |
| [`compress()`](https://docs.python.org/zh-cn/3/library/itertools.html#itertools.compress) | data, selectors             | (d[0] if s[0]), (d[1] if s[1]), ...           | `compress('ABCDEF', [1,0,1,0,1,1]) → A C E F`            |
| [`dropwhile()`](https://docs.python.org/zh-cn/3/library/itertools.html#itertools.dropwhile) | predicate, seq              | seq[n], seq[n+1], 从 predicate 未通过时开始   | `dropwhile(lambda x: x<5, [1,4,6,3,8]) → 6 3 8`          |
| [`filterfalse()`](https://docs.python.org/zh-cn/3/library/itertools.html#itertools.filterfalse) | predicate, seq              | predicate(elem) 未通过的 seq 元素             | `filterfalse(lambda x: x<5, [1,4,6,3,8]) → 6 8`          |
| [`groupby()`](https://docs.python.org/zh-cn/3/library/itertools.html#itertools.groupby) | iterable[, key]             | 根据key(v)值分组的迭代器                      |                                                          |
| [`islice()`](https://docs.python.org/zh-cn/3/library/itertools.html#itertools.islice) | seq, [start,] stop [, step] | seq[start:stop:step]中的元素                  | `islice('ABCDEFG', 2, None) → C D E F G`                 |
| [`pairwise()`](https://docs.python.org/zh-cn/3/library/itertools.html#itertools.pairwise) | iterable -- 可迭代对象      | (p[0], p[1]), (p[1], p[2])                    | `pairwise('ABCDEFG') → AB BC CD DE EF FG`                |
| [`starmap()`](https://docs.python.org/zh-cn/3/library/itertools.html#itertools.starmap) | func, seq                   | func(*seq[0]), func(*seq[1]), ...             | `starmap(pow, [(2,5), (3,2), (10,3)]) → 32 9 1000`       |
| [`takewhile()`](https://docs.python.org/zh-cn/3/library/itertools.html#itertools.takewhile) | predicate, seq              | seq[0], seq[1], 直到 predicate 未通过         | `takewhile(lambda x: x<5, [1,4,6,3,8]) → 1 4`            |
| [`tee()`](https://docs.python.org/zh-cn/3/library/itertools.html#itertools.tee) | it, n                       | it1, it2, ... itn 将一个迭代器拆分为n个迭代器 |                                                          |
| [`zip_longest()`](https://docs.python.org/zh-cn/3/library/itertools.html#itertools.zip_longest) | p, q, ...                   | (p[0], q[0]), (p[1], q[1]), ...               | `zip_longest('ABCD', 'xy', fillvalue='-') → Ax By C- D-` |

**排列组合迭代器：**

| 迭代器                                                       | 实参                 | 结果                                  |
| :----------------------------------------------------------- | :------------------- | :------------------------------------ |
| [`product()`](https://docs.python.org/zh-cn/3/library/itertools.html#itertools.product) | p, q, ... [repeat=1] | 笛卡尔积，相当于嵌套的for循环         |
| [`permutations()`](https://docs.python.org/zh-cn/3/library/itertools.html#itertools.permutations) | p[, r]               | 长度r元组，所有可能的排列，无重复元素 |
| [`combinations()`](https://docs.python.org/zh-cn/3/library/itertools.html#itertools.combinations) | p, r                 | 长度r元组，有序，无重复元素           |
| [`combinations_with_replacement()`](https://docs.python.org/zh-cn/3/library/itertools.html#itertools.combinations_with_replacement) | p, r                 | 长度r元组，有序，元素可重复           |

| 例子                                       | 结果                                              |
| :----------------------------------------- | :------------------------------------------------ |
| `product('ABCD', repeat=2)`                | `AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD` |
| `permutations('ABCD', 2)`                  | `AB AC AD BA BC BD CA CB CD DA DB DC`             |
| `combinations('ABCD', 2)`                  | `AB AC AD BC BD CD`                               |
| `combinations_with_replacement('ABCD', 2)` | `AA AB AC AD BB BC BD CC CD DD`                   |

### functools

@lru_cache

```py
@cache
def factorial(n):
    return n * factorial(n-1) if n else 1

>>> factorial(10)      # no previously cached result, makes 11 recursive calls
3628800
>>> factorial(5)       # just looks up cached value result
120
>>> factorial(12)      # makes two new recursive calls, the other 10 are cached
479001600
```

### operator

以下表格显示了抽象运算是如何对应于 Python 语法中的运算符和 [`operator`](https://docs.python.org/zh-cn/3/library/operator.html#module-operator) 模块中的函数的。

| 运算         | 语法                | 函数                                |
| :----------- | :------------------ | :---------------------------------- |
| 加法         | `a + b`             | `add(a, b)`                         |
| 除法         | `a / b`             | `truediv(a, b)`                     |
| 除法         | `a // b`            | `floordiv(a, b)`                    |
| 取幂         | `a ** b`            | `pow(a, b)`                         |
| 标识         | `a is b`            | `is_(a, b)`                         |
| 标识         | `a is not b`        | `is_not(a, b)`                      |
| 取模         | `a % b`             | `mod(a, b)`                         |
| 乘法         | `a * b`             | `mul(a, b)`                         |
| 矩阵乘法     | `a @ b`             | `matmul(a, b)`                      |
| 取反（算术） | `- a`               | `neg(a)`                            |
| 取反（逻辑） | `not a`             | `not_(a)`                           |
| 减法         | `a - b`             | `sub(a, b)`                         |
| 真值测试     | `obj`               | `truth(obj)`                        |
| 比较         | `a < b`             | `lt(a, b)`                          |
| 比较         | `a <= b`            | `le(a, b)`                          |
| 相等         | `a == b`            | `eq(a, b)`                          |
| 不等         | `a != b`            | `ne(a, b)`                          |
| 比较         | `a >= b`            | `ge(a, b)`                          |
| 比较         | `a > b`             | `gt(a, b)`                          |

### bisect

这个模块对有序列表提供了支持，使得他们可以在插入新数据仍然保持有序。对于长列表，如果其包含元素的比较操作十分昂贵的话，这可以是对更常见方法的改进。这个模块叫做 [`bisect`](https://docs.python.org/zh-cn/3.6/library/bisect.html#module-bisect) 因为其使用了基本的二分（bisection）算法。源代码也可以作为很棒的算法示例（边界判断也做好啦！）

定义了以下函数：

- bisect.**bisect_left**(*a*, *x*, *lo=0*, *hi=len(a)*)

  在 *a* 中找到 *x* 合适的插入点以维持有序。参数 *lo* 和 *hi* 可以被用于确定需要考虑的子集；默认情况下整个列表都会被使用。如果 *x* 已经在 *a* 里存在，那么插入点会在已存在元素之前（也就是左边）。如果 *a* 是列表（list）的话，返回值是可以被放在 `list.insert()` 的第一个参数的。返回的插入点 *i* 可以将数组 *a* 分成两部分。左侧是 `all(val < x for val in a[lo:i])` ，右侧是 `all(val >= x for val in a[i:hi])` 。

- bisect.**bisect_right**(*a*, *x*, *lo=0*, *hi=len(a)*)

- bisect.**bisect**(*a*, *x*, *lo=0*, *hi=len(a)*)

  类似于 [`bisect_left()`](https://docs.python.org/zh-cn/3.6/library/bisect.html#bisect.bisect_left)，但是返回的插入点是 *a* 中已存在元素 *x* 的右侧。返回的插入点 *i* 可以将数组 *a* 分成两部分。左侧是 `all(val <= x for val in a[lo:i])`，右侧是 `all(val > x for val in a[i:hi])` for the right side。

- bisect.**insort_left**(*a*, *x*, *lo=0*, *hi=len(a)*)

  将 *x* 插入到一个有序序列 *a* 里，并维持其有序。如果 *a* 有序的话，这相当于 `a.insert(bisect.bisect_left(a, x, lo, hi), x)`。要注意搜索是 O(log n) 的，插入却是 O(n) 的。

- bisect.**insort_right**(*a*, *x*, *lo=0*, *hi=len(a)*)

- bisect.**insort**(*a*, *x*, *lo=0*, *hi=len(a)*)

  类似于 [`insort_left()`](https://docs.python.org/zh-cn/3.6/library/bisect.html#bisect.insort_left)，但是把 *x* 插入到 *a* 中已存在元素 *x* 的右侧。
  
### statistics

| [`mean()`](https://docs.python.org/zh-cn/3.12/library/statistics.html#statistics.mean) | 数据的算术平均数（“平均数”）。                 |
| ------------------------------------------------------------ | ---------------------------------------------- |
| [`fmean()`](https://docs.python.org/zh-cn/3.12/library/statistics.html#statistics.fmean) | 快速的浮点算术平均值，带有可选的权重设置。     |
| [`geometric_mean()`](https://docs.python.org/zh-cn/3.12/library/statistics.html#statistics.geometric_mean) | 数据的几何平均数                               |
| [`harmonic_mean()`](https://docs.python.org/zh-cn/3.12/library/statistics.html#statistics.harmonic_mean) | 数据的调和均值                                 |
| [`median()`](https://docs.python.org/zh-cn/3.12/library/statistics.html#statistics.median) | 数据的中位数（中间值）                         |
| [`median_low()`](https://docs.python.org/zh-cn/3.12/library/statistics.html#statistics.median_low) | 数据的低中位数                                 |
| [`median_high()`](https://docs.python.org/zh-cn/3.12/library/statistics.html#statistics.median_high) | 数据的高中位数                                 |
| [`median_grouped()`](https://docs.python.org/zh-cn/3.12/library/statistics.html#statistics.median_grouped) | 分组数据的中位数（即第 50 个百分点的位置）。   |
| [`mode()`](https://docs.python.org/zh-cn/3.12/library/statistics.html#statistics.mode) | 离散的或标称的数据的单个众数（出现最多的值）。 |
| [`multimode()`](https://docs.python.org/zh-cn/3.12/library/statistics.html#statistics.multimode) | 离散的或标称的数据的众数（出现最多的值）列表。 |
| [`quantiles()`](https://docs.python.org/zh-cn/3.12/library/statistics.html#statistics.quantiles) | 将数据以相等的概率分为多个间隔。               |