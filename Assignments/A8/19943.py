#19943: 图的拉普拉斯矩阵

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}
    
    def add_neighbor(self, nbr):
        self.connected_to[nbr] = 1

    def get_connections(self):
        return self.connected_to.keys()
    
    def degree(self):
        return(len(self.get_connections()))

class Graph:
    def __init__(self):
        self.vertex_list = {}
    
    def add_vertex(self, key):
        self.vertex_list[key] = Vertex(key)

    def get_vertices(self):
        return self.vertex_list.keys()
    
    def num_vertices(self):
        return len(self.get_vertices())
    
    def add_edge(self, i, j):
        if i not in self.vertex_list:
            self.add_vertex(i)
        if j not in self.vertex_list:
            self.add_vertex(j)
        self.vertex_list[i].add_neighbor(j)
        self.vertex_list[j].add_neighbor(i)
    
    def degree_matrix(self, i, j):
        return self.vertex_list[i].degree() * (i == j)
    
    def adjacent_matrix(self, i, j):
        return j in self.vertex_list[i].connected_to

    def laplacian_matrix(self, i, j):
        return self.degree_matrix(i, j) - self.adjacent_matrix(i, j)
    
n, m = map(int, input().split())
graph = Graph()
for i in range(n):
    graph.add_vertex(i)
for _ in range(m):
    graph.add_edge(*(int(x) for x in input().split()))

for i in range(n):
    print(*(graph.laplacian_matrix(i, j) for j in range(n)))
