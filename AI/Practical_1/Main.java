import java.util.*;

class Graph {
    private int V; // No. of vertices
    private LinkedList<Integer> adj[]; // Adjacency List

    // Constructor
    Graph(int v) {
        V = v;
        adj = new LinkedList[v];
        for (int i = 0; i < v; ++i)
            adj[i] = new LinkedList();
    }

    // Function to add an edge into the graph
    void addEdge(int v, int w) {
        adj[v].add(w);
        adj[w].add(v);
    }

    // Recursive function to perform DFS traversal from a vertex
    void DFSUtil(int s, boolean visited[]) {
        // Mark the current node as visited
        visited[s] = true;
        System.out.print(s + " ");

        // Recur for all the vertices adjacent to this vertex
        Iterator<Integer> i = adj[s].listIterator();
        while (i.hasNext()) {
            int n = i.next();
            if (!visited[n])
                DFSUtil(n, visited);
        }
    }

    // Function to perform DFS traversal from a source vertex
    void DFS(int s) {
        // Mark all the vertices as not visited
        boolean visited[] = new boolean[V];

        // Call the recursive helper function to print DFS traversal
        DFSUtil(s, visited);
    }

    // Function to perform BFS traversal from a source vertex
    void BFS(int s) {
        // Mark all the vertices as not visited
        boolean visited[] = new boolean[V];

        // Create a queue for BFS
        LinkedList<Integer> queue = new LinkedList<Integer>();

        // Mark the current node as visited and enqueue it
        visited[s] = true;
        queue.add(s);

        while (!queue.isEmpty()) {
            // Dequeue a vertex from queue and print it
            s = queue.poll();
            System.out.print(s + " ");

            // Get all adjacent vertices of the dequeued vertex s
            // If a adjacent has not been visited, then mark it
            // visited and enqueue it
            Iterator<Integer> i = adj[s].listIterator();
            while (i.hasNext()) {
                int n = i.next();
                if (!visited[n]) {
                    visited[n] = true;
                    queue.add(n);
                }
            }
        }
    }
}

public class Main {
    public static void main(String args[]) {
        Graph g = new Graph(4);

        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 2);
        g.addEdge(2, 0);
        g.addEdge(2, 3);
        g.addEdge(3, 3);

        System.out.println("Depth First Traversal (starting from vertex 2)");
        g.DFS(2);
        System.out.println("\nBreadth First Traversal (starting from vertex 2)");
        g.BFS(2);
    }
}
