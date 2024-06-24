#sy383: 最大权值连通块

class Vertex:
    def __init__(self, key, weight):
        self.id = key
        self.weight = weight
        self.connected_to = {}
        self.traversed = 0
    
    def add_neighbor(self, nbr):
        self.connected_to[nbr] = 1

    def get_connections(self):
        return self.connected_to.keys()
    
    def degree(self):
        return(len(self.get_connections()))

class Graph:
    def __init__(self):
        self.vertex_list = {}
    
    def add_vertex(self, key, weight):
        self.vertex_list[key] = Vertex(key, weight)

    def get_vertices(self):
        return self.vertex_list.keys()
    
    def num_vertices(self):
        return len(self.get_vertices())
    
    def add_edge(self, i, j):
        self.vertex_list[i].add_neighbor(j)
        self.vertex_list[j].add_neighbor(i)

    def traverse(self, vert):
        if self.vertex_list[vert].traversed:
            return 0
        res = self.vertex_list[vert].weight
        self.vertex_list[vert].traversed = 1
        for nbr in self.vertex_list[vert].get_connections():
            res += self.traverse(nbr)
        return res

n, m = map(int, input().split())
graph = Graph()
for index, weight in enumerate(input().split()):
    graph.add_vertex(index, int(weight))
for _ in range(m):
    i, j = map(int, input().split())
    graph.add_edge(i, j)
print(max(map(graph.traverse, range(n))))
