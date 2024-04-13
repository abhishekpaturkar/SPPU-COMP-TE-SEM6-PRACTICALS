# A\* Search Algorithm Implementation in Python

## Problem Statement

Implement A star Algorithm for any game search problem

## Overview

This program implements the A\* search algorithm to find the shortest path between two nodes in a graph. It utilizes a heuristic function to guide the search towards the goal node.

## Code Explanation

### Node Class

The Node class represents each node in the graph. It contains the vertex number and fScore (estimated cost to goal). The **lt** method is overridden to allow nodes to be compared based on fScore for priority queue operations.

### Edge Class

The Edge class is nested within the Graph class and represents each edge in the graph. It contains the destination vertex and edge weight.

### Graph Class

The Graph class represents the graph using an adjacency list. It contains the number of vertices, adjacency list, and heuristics.

- addEdge() method adds an edge to the graph
- setHeuristic() sets the heuristic value for each node
- AStar() implements the A\* algorithm

### A\* Algorithm

- Create a priority queue and add the start node to it
- Mark all nodes unvisited
- Set gScore of start node to 0 and infinity for others
- While priority queue is not empty:
  - Pop the node with lowest fScore
  - If node is goal, return the path
  - Mark node visited
  - Update neighbors:
    - Calculate fScore
    - If better than previous, update gScore and add neighbor to queue
- If no path found, print message

### Main

- Take graph size and edges as input
- Take heuristic values as input
- Run A\* algorithm
- Print shortest path and cost

## Example Run

Enter the size of the graph: 5
Enter the size of input: 7
Enter edges of graph
Enter 1 edges and weight of that edges: 0 1 4
Enter 2 edges and weight of that edges: 0 2 2
Enter 3 edges and weight of that edges: 1 2 1
Enter 4 edges and weight of that edges: 1 3 5
Enter 5 edges and weight of that edges: 2 3 8
Enter 6 edges and weight of that edges: 2 4 10
Enter 7 edges and weight of that edges: 3 4 1
Enter heuristic of the edges of graph
Enter 1 edges heuristic value: 7
Enter 2 edges heuristic value: 6
Enter 3 edges heuristic value: 2
Enter 4 edges heuristic value: 1
Enter 5 edges heuristic value: 0
Enter the starting and the ending vertex where you want to find the shortest distance: 0 4
The Shortest Path: 0 2 1 3 4  
Shortest path from 0 to 4 has cost of: 14

This implements the A\* algorithm and finds the shortest path from node 0 to 4.
