# readme.md

# Practical 1 - Graph Traversal Algorithms (DFS & BFS)

This code implements depth first search (DFS) and breadth first search (BFS) algorithms to traverse a graph data structure.

## Problem Statement

Implement depth first search algorithm and Breadth First Search algorithm, Use an undirected graph and develop a recursive algorithm for searching all the vertices of a graph or tree data structure.

## Graph Class

The Graph class represents an undirected graph using an adjacency list. It has the following methods:

- `__init__()` - Initializes a graph object
- `addEdge()` - Adds an edge between two vertices
- `addVertex()` - Adds a vertex to the graph
- `DFS()` - Implements recursive DFS traversal
- `BFS()` - Implements iterative BFS traversal using a queue

The graph is stored as a Python dictionary where keys are vertices and values are lists of neighboring vertices.

## Main

The main section:

- Takes graph input from the user - number of vertices and edges
- Calls `addVertex()` and `addEdge()` to construct the graph
- Takes source and destination vertex as input
- Calls `DFS()` and `BFS()` to print traversal from source to destination
- Provides sample I/O

## Explanation

DFS traversal visits vertices depth-wise, going as deep as possible down a branch before backtracking. It uses recursion to visit neighbors of a vertex.

BFS traversal visits vertices breadth-wise, level by level. It uses a queue to track the set of vertices to visit next.

Both traversals print out the vertex sequence from source to destination.
