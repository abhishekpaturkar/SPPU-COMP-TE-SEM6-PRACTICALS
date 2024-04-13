# Problem 2
# Implement A star Algorithm for any game search problem 


# Node class to represent each node in the graph
# Contains vertex number and fScore
class Node:
    def __init__(self, vertex, fScore):
        self.vertex = vertex
        self.fScore = fScore
    
    def __lt__(self, other):
        return self.fScore < other.fScore

# Graph class to represent the graph
# Contains number of vertices, adjacency list, heuristics
class AStarGraph:

    # Edge class to represent each edge
    # Contains destination vertex and weight
    class Edge:
        def __init__(self, dest, weight):
            self.dest = dest
            self.weight = weight
    
    def __init__(self, v):
        self.V = v
        self.adj = [[] for _ in range(v)]
        self.h = [0] * v
    
    # Add edge to graph
    def addEdge(self, u, v, weight):
        self.adj[u].append(self.Edge(v, weight))
    
    # Set heuristics
    def setHeuristic(self, heuristic):
        self.h = heuristic
    
    # A* search algorithm
    def AStar(self, start, end):
        pq = []
        heapq.heappush(pq, Node(start, self.h[start]))
        visited = [False] * self.V
        gScore = [float('inf')] * self.V
        gScore[start] = 0
        print("The Shortest Path:", end=' ')
        while pq:
            curr = heapq.heappop(pq)
            u = curr.vertex
            print(u, end=' ')
            if u == end:
                print("\nShortest path from", start, "to", end, "has cost of:", gScore[u])
                return
            visited[u] = True
            for e in self.adj[u]:
                v = e.dest
                w = e.weight
                if not visited[v]:
                    fScore = gScore[u] + w + self.h[v]
                    if fScore < gScore[v]:
                        gScore[v] = fScore
                        heapq.heappush(pq, Node(v, fScore))
        print("No path found from", start, "to", end)

# Driver code
if __name__ == "__main__":
    print("Enter the size of the graph:", end=' ')
    n = int(input())
    g = AStarGraph(n)
    print("Enter the size of input:", end=' ')
    size = int(input())
    print("Enter edges of graph")
    for i in range(size):
        print("Enter", i + 1, "edges and weight of that edges:", end=' ')
        j, k, w = map(int, input().split())
        if j < n and k < n:
            g.addEdge(j, k, w)
        else:
            print("Invalid Input")
    heuristic = [0] * n
    print("Enter heuristic of the edges of graph")
    for i in range(n):
        print("Enter", i + 1, "edges heuristic value:", end=' ')
        heuristic[i] = int(input())
    g.setHeuristic(heuristic)
    print("Enter the starting and the ending vertex where you want to find the shortest distance:", end=' ')
    start, end = map(int, input().split())
    g.AStar(start, end)


# -----------------Terminal---------------------
# Enter the size of the graph: 5
# Enter the size of input: 7
# Enter edges of graph
# Enter 1 edges and weight of that edges: 0 1 4
# Enter 2 edges and weight of that edges: 0 2 2
# Enter 3 edges and weight of that edges: 1 2 1
# Enter 4 edges and weight of that edges: 1 3 5
# Enter 5 edges and weight of that edges: 2 3 8
# Enter 6 edges and weight of that edges: 2 4 10
# Enter 7 edges and weight of that edges: 3 4 1
# Enter heuristic of the edges of graph
# Enter 1 edges heuristic value: 7
# Enter 2 edges heuristic value: 6
# Enter 3 edges heuristic value: 2
# Enter 4 edges heuristic value: 1
# Enter 5 edges heuristic value: 0
# Enter the starting and the ending vertex where you want to find the shortest distance: 0 4
# The Shortest Path: 0 2 1 3 4
# Shortest path from 0 to 4 has cost of: 14