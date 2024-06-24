#04078:实现堆结构
heap = []

def heap_swap(i, j):
    heap[i], heap[j] = min(heap[i], heap[j]), max(heap[i], heap[j])

def father(i):
    return (i - 1) // 2

def sons(i):
    return (2 * i + 1, 2 * i + 2)

def insert(value):
    def search_upwards(index):
        if index == 0 or heap[father(index)] <= heap[index]:
            return
        heap_swap(father(index), index)
        search_upwards(father(index))

    heap.append(value)
    search_upwards(len(heap) - 1)

def pop_smallest():
    def search_downwards(index):
        real_sons = [son for son in sons(index) if son < len(heap)]
        if real_sons == []:
            return
        min_son = real_sons[0]
        for son in real_sons:
            if heap[son] < heap[min_son]:
                min_son = son
        if heap[min_son] >= heap[index]:
            return
        heap_swap(index, min_son)
        search_downwards(min_son)

    heap[0], heap[-1] = heap[-1], heap[0]
    res = heap.pop()
    search_downwards(0)
    return res

n = int(input())
for _ in range(n):
    op = [int(i) for i in input().split()]
    if op[0] == 1:
        insert(op[1])
    elif op[0] == 2:
        print(pop_smallest())
