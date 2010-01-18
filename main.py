from itertools import permutations
from eurail import EURail, Coords
from utils import *

def exportDot(city, path):
    print "digraph g"
    print "{"
    
    for v in vertices(city):
        x,y=Coords[v]
        
        print v, "[pos=\"%(a)f,%(b)f\"];" % {'a':y*50, 'b':x*50}
    
    for ((a, b), c) in city:
        print a, "->", b, "[dir=none color=\"#dddddd\"];"
    
    for i in range(0, len(path) - 1):
        print path[i], "->", path[i + 1], ";"
    
    print "}"

def exportMathematica(city, path):
    print "{"
    
    for ((a, b), c) in city:
        print a, "->", b, ","
    
    print "}"

def shortestPath(city, mustPass, start=None):
    c = Graph(city)
    
    # Floyd-Warshall; generate optimal path between each pair of vertices
    dist = [[Infinity] * c.n for i in range(0, c.n)]
    path = [[None] * c.n for i in range(0, c.n)]
    
    for ((a, b), w) in c.data:
        dist[c.vertexIndex(a)][c.vertexIndex(b)] = w
        dist[c.vertexIndex(b)][c.vertexIndex(a)] = w
    
    for k in range(0, c.n):
        for i in range(0, c.n):
            for j in range(0, c.n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][j] = c.vertexAtIndex(k)
    
    # Reconstruct the Floyd-Warshall-generated path
    def followPath(i, j):
        if dist[i][j] == Infinity:
            return ["FAIL"]
        
        next = path[i][j]
        
        if next is None:
            return []
        else:
            nexti = c.vertexIndex(next)
            return followPath(i, nexti) + [next] + followPath(nexti, j)
    
    # Test all permutations of "must-pass" vertices, find shortest path
    short = Infinity
    shortorder = None
    shortindices = None
    
    for p in permutations(mustPass):
        p = list(p)
        
        if start:
            p.insert(0, start)
        
        # Get a list of vertex indices from the given start/mustpass vertices
        pi = [c.vertexIndex(v) for v in p]
        
        # Calculate the total distance with the given permutation
        pd = sum([dist[pi[i]][pi[i+1]] for i in range(0, len(p) - 1)])
        
        # Store the (potentially new) minimum difference
        if pd < short:
            short, shortorder, shortindices = pd, p, pi
    
    # Compute the actual path (adding intermediate stops, etc.)
    shortpath = [shortorder[0]]
    for i in range(0, len(shortorder) - 1):
        shortpath.extend(followPath(shortindices[i],shortindices[i+1]))
        shortpath.append(shortorder[i+1])

    return shortpath

path = shortestPath(EURail, ["Barcelona", "Rome"], "Paris")
exportDot(EURail, path)