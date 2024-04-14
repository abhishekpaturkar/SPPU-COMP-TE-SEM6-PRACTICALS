# Practical_3.py

This Python file contains implementations of various algorithms covered in the course.

## Problem Statement

Implement Greedy search algorithm for any of the following application:
I. Selection Sort
II. Minimum Spanning Tree
III. Single-Source Shortest Path Problem
IV. Job Scheduling Problem
V. Prim's Minimal Spanning Tree Algorithm
VI. Kruskal's Minimal Spanning Tree Algorithm
VII. Dijkstra's Minimal Spanning Tree Algorithm

## Functions

### selectionSort(A)

Performs selection sort on the input array A.

- Makes a copy of the original array called U.
- Iterates through the array, finding the minimum element from i to end and swapping it with A[i].
- Prints the unsorted and sorted arrays.

### jobScheduling(arr)

Solves the Job Scheduling problem using Priority Queue.

- Sort jobs by finish time.
- Iterate through jobs. Calculate slots available.
- Add jobs to a max heap based on profit.
- While slots available, pop from heap and add to result.

### PGraph(vertices, graph)

Implements Prim's MST for a graph represented as adjacency matrix.

- `minKey` finds unvisited vertex with minimum key value.
- `primMST` calculates MST using minKey and prints edges and cost.

### KGraph(vertices, graph)

Implements Kruskal's MST for a graph represented as adjacency matrix.

- `find` and `union` functions for disjoint sets.
- `KruskalMST` calculates MST using union-find and prints edges and cost.

### dijkstra(inp, source, dest)

Implements Dijkstra's algorithm to find shortest path.

- Builds graph from adjacency matrix inp.
- Uses priority queue to find shortest path.
- Prints path and minimum cost.

## Sample Inputs

- Enter number of elements: 5
- Enter element 1: 2
- Enter element 2: 5
- Enter element 3: 1
- Enter element 4: 0
- Enter element 5: 10
- Selection Sort:
- Unsorted array: [2, 5, 1, 0, 10]
- Sorted array: [0, 1, 2, 5, 10]
- Enter number of jobs: 3
- Enter job name, deadline and profit separated by spaces: a 2 100
- Enter job name, deadline and profit separated by spaces: b 1 50
- Enter job name, deadline and profit separated by spaces: c 3 150

- Job Scheduling Problem:
- Following is maximum profit sequence of jobs: [['b', 1], ['a', 2], ['c', 3]]
- None
- Enter number of vertices: 5
- Enter row 1: 0 4 0 0 0
- Enter row 2: 4 0 5 0 3
- Enter row 3: 0 5 0 1 6
- Enter row 4: 0 0 1 0 0
- Enter row 5: 0 3 6 0 0

- Prim’s Minimum Spanning Tree:
- Edge Weight
- 0 -- 1 == 4
- 1 -- 2 == 5
- 2 -- 3 == 1
- 1 -- 4 == 3
- Minimum cost = 13

- Kruskal’s Minimum Spanning Tree:
- Edge Weight
- 2 -- 3 == 1
- 1 -- 4 == 3
- 0 -- 1 == 4
- 1 -- 2 == 5
- Minimum cost = 13

- Dijkstra Single-Source Shortest Path:
- Path: [0, 1, 4]
- Minimum Cost: 7
