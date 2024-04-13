# Problem Statement
# Practical 1 : Implement depth first search algorithm and Breadth First Search algorithm, 
# Use an undirected graph and develop a recursive algorithm 
# for searching all the vertices of a graph or tree data structure.

from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def addVertex(self, v):
        self.graph[v]

    def DFS(self, v, d, visitSet = None) -> bool:
        visited = visitSet or set()
        visited.add(v)
        print(v,end=" ")

        if v == d:
            return True

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                if self.DFS(neighbour, d, visited):
                    return True

        return False

    def BFS(self, s, d):
        visited = defaultdict(bool)
        queue = deque([s])
        visited[s] = True

        while queue:
            s = queue.popleft() 
            print(s, end=' ')
            if s == d:
                return True
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
        return False


if __name__ == '__main__':
    g = Graph()

    n = int(input("Enter number of nodes: "))

    for i in range(n):
        node = input("Enter node {}: ".format(i+1))
        g.addVertex(node)

    e = int(input("\nEnter number of edges: "))

    for i in range(e):
        nodes = input("Enter edge {} (format: node1 node2): ".format(i+1)).split()
        g.addEdge(nodes[0], nodes[1])

    print("\nGraph input completed")

    s = input("Enter source node: ")
    d = input("Enter destination node: ")
    
    print("\nFollowing is Depth First Traversal {} -> {}:".format(s, d))
    g.DFS(s, d)
    

    print("\n\nFollowing is Breadth First Traversal {} -> {}:".format(s, d))
    g.BFS(s, d)



# --------------- Terminal --------------------
# Enter number of nodes: 8
# Enter node 1: a   
# Enter node 2: b
# Enter node 3: c
# Enter node 4: d
# Enter node 5: e
# Enter node 6: f
# Enter node 7: g
# Enter node 8: h

# Enter number of edges: 14
# Enter edge 1 (format: node1 node2): h a
# Enter edge 2 (format: node1 node2): a d
# Enter edge 3 (format: node1 node2): a b
# Enter edge 4 (format: node1 node2): b f
# Enter edge 5 (format: node1 node2): b c
# Enter edge 6 (format: node1 node2): c e
# Enter edge 7 (format: node1 node2): c g
# Enter edge 8 (format: node1 node2): c h
# Enter edge 9 (format: node1 node2): g h
# Enter edge 10 (format: node1 node2): g e
# Enter edge 11 (format: node1 node2): e f
# Enter edge 12 (format: node1 node2): e b
# Enter edge 13 (format: node1 node2): f a
# Enter edge 14 (format: node1 node2): d f

# Graph input completed
# Enter source node: h
# Enter destination node: e

# Following is Depth First Traversal h -> e:
# h a d f b c e

# Following is Breadth First Traversal h -> e:
# h a d b f c e