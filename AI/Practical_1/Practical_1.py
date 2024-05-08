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
    
    # The selected code defines a recursive depth-first search (DFS) function to traverse a graph data structure.
    # It takes in 3 parameters:
    # - v: The current node being visited
    # - d: The target destination node 
    # - visitSet: A set to track visited nodes (initialized to None)
    # The function first initializes a visited set if one was not passed in. It adds the current node v to the visited set. 
    # It prints the current node v.
    # It checks if v is equal to the target node d. If so, it returns True.
    # It then loops through all the neighbors of the current node v from the graph. 
    # For each neighbor, it checks if that node has already been visited. 
    # If not, it recursively calls the DFS function on that neighbor to explore it, passing along the visited set. 
    # If that recursive call returns True (meaning it found the destination), this call also returns True.
    # If after exploring all neighbors it did not find the destination, it returns False.
    # So in summary, this implements a recursive depth-first search that explores a graph data structure to try to find a path between a source and destination node.

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

    # This function implements breadth-first search (BFS) to find a path from node s to node d.
    # It uses a queue to keep track of the nodes to visit next. 
    # It also uses a visited dictionary to mark nodes as visited to avoid visiting them again.
    # It starts by adding the source node s to the queue and marking it visited. 
    # Then in a loop, it dequeues the next node, prints it, and checks if it's the destination.
    # If not, it loops through all its adjacent unvisited nodes, adds them to the queue and marks them visited.
    # This continues until either the destination is reached, or the queue is empty, meaning there is no path.
    # The visited dictionary allows fast lookups to check if a node was already visited.
    # Using BFS ensures the shortest path is found from s to d if it exists.

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


