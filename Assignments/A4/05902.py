#05902:双端队列

class Deque:
    def __init__(self, iterable=None):
        self.__list = []
        if iterable is not None:
            for i in iterable:
                self.__list.append(i)

    def elements(self):
        if self.__list:
            return " ".join(map(str, self.__list))
        else:
            return "NULL"
    def append(self, item):
        self.__list.append(item)

    def popr(self):
        return self.__list.pop()

    def popl(self):
        return self.__list.pop(0)

for _ in range(int(input())):
    n = int(input())
    deque = Deque()
    for _ in range(n):
        x, c = map(int, input().split())
        if x == 1:
            deque.append(c)
        elif (x, c) == (2, 0):
            deque.popl()
        elif (x, c) == (2, 1):
            deque.popr()
    print(deque.elements())
