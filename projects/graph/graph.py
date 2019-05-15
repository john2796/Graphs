"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()
        pass  # TODO

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        v1 -> (5, 3) <- v2
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")
        pass  # TODO

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.

        """
        # Create an empty Queue
        q = Queue()
        # Create an empty Visisted set
        visited = set()
        # Add the starting vertex (node) to the queue
        q.enqueue(starting_vertex)
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeu the first vertex (node)
            v = q.dequeue()
        # If it has not been visited in a set...
            if v not in visited:
                # Mark it as visisted (print it and add it to the visaited set)
                print(v, visited, '<----------bft')
                visited.add(v)  # add element to a set
                # Then enqueue each of its neighbors in the queue
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)
        # TODO

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty Stack
        s = Stack()
        # Create an empty Visited set
        visited = set()
        # Push the starting vertex to the queue
        s.push(starting_vertex)
        # While the Stack is not empty...
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            # If it has not been visited...
            if v not in visited:
                # Mark it as visited (print it and add it to the visited set)
                print(v, visited, '<---------dft')
                visited.add(v)
            # Then push each of its neighbors onto the Stack
            for neighbor in self.vertices[v]:
                s.push(neighbor)
        pass  # TODO

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # Mark the starting node as visited
        # Call DFT_Recursive on each unvisited neighbors
        if visited is None:
            visited = set()
        # Mark the starting node as visited
        print(starting_vertex, visited, '<-----dft_recursive')
        visited.add(starting_vertex)
        # Call DFT_Recursive on each unvisited neighbors
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order. Queue
        """
        # Create an empty Queue
        q = Queue()
        # Create an empty Visited set
        visited = set()
        # Add A PATH / Add to the starting vertext to the queue -> add starting vertex to the queue
        q.enqueue([starting_vertex])
        # while the queue is not empty...
        while q.size() > 0:
            # Dequeue the first Path
            path = q.dequeue()
            # Grab the last vertex of the path
            v = path[-1]
            # Check if it's our destination
            if v == destination_vertex:
                return path
            # If it has not been visited...
            if v not in visited:
                # Mark it as visited (add it to the visited set)
                visited.add(v)
            # Then enqueue PATHS To each of its neighbors in the queue
            for edges in self.vertices[v]:
                edges_copy = path.copy()
                edges_copy.append(edges)
                q.enqueue(edges_copy)
                print(v, path)

        # print(v, path, visited, edges)

    def dfs(self, starting_vertex, destination_vertex, visited=None):
        """ 
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order. Stack
        """
        # Create an empty Stack
        s = Stack()
        # Create an empty Visited set
        visited = set()
        # Add A Path to the starting vertex to the queue
        s.push([starting_vertex])
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the First PATH
            path = s.pop()
            # Grab the last vertex of the path
            v = path[-1]
            # Check if it's our destination
            if v == destination_vertex:
                return path
            # If it has not been visited..
            if v not in visited:
                # Mark it as visited ( add it to the visited set)
                visited.add(v)
                # Then push PATHS To each of its neighbors in the stack
                for edges in self.vertices[v]:
                    edges_copy = path.copy()
                    edges_copy.append(edges)
                    s.push(edges_copy)
                    print(v, edges_copy)


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    # print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # graph.bfs(1, 6)

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # graph.dfs(1, 6)
