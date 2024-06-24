#28046:词梯
from queue import deque

class Vertex:
    def __init__(self, id, word):
        self.id = id
        self.word = word
        self.connected = []
        self.visited = False
        self.father = None

class Graph:
    def __init__(self, words):
        self.words = words
        self.word2vertex = {}
        self.len = len(words)
        for id, word in enumerate(words):
            self.word2vertex[word] = Vertex(id, word)

    def add_edge(self, word1, word2):
        self.word2vertex[word1].connected.append(self.word2vertex[word2])
        self.word2vertex[word2].connected.append(self.word2vertex[word1])

    def connect(self):
        buckets = {}
        for word in self.words:
            for i, _ in enumerate(word):
                bucket = f"{word[:i]}_{word[i + 1:]}"
                buckets.setdefault(bucket, set()).add(word)
        for similar_words in buckets.values():
            for word1 in similar_words:
                for word2 in similar_words - {word1}:
                    self.add_edge(word1, word2)

    def search(self, start, end):
        queue = deque()
        queue.append(self.word2vertex[start])
        self.word2vertex[start].visited = True
        while len(queue) != 0:
            now = queue.popleft()
            if now == self.word2vertex[end]:
                break
            for child in now.connected:
                if child.visited == False:
                    queue.append(child)
                    child.father = now
                    child.visited = True
        if self.word2vertex[end].father is None:
            return "NO"
        res = [end]
        now = self.word2vertex[end]
        while now.father is not None:
            res.append(now.father.word)
            now = now.father
        return ' '.join(reversed(res))

n = int(input())
graph = Graph([input() for _ in range(n)])
graph.connect()
print(graph.search(*input().split()))
