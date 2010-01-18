Infinity = float('inf')

def flatten(iterable):
    it = iter(iterable)
    for e in it:
        if isinstance(e, (list, tuple)):
            for f in flatten(e):
                yield f
        else:
            yield e

def vertices(graph):
    vertices = {}
    for ((a, b), w) in graph:
        vertices[a] = vertices[b] = 1
    return vertices.keys()

class Graph(object):
    def __init__(self, city):
        super(Graph, self).__init__()

        self.data = city
        self.v = vertices(self.data)
        self.n = len(self.v)

    def vertexAtIndex(self, n):
        return self.v[n]

    def vertexIndex(self, v):
        return self.v.index(v)