# Imports
import timeit

# Classes and Definitions
# Graph Node
class GraphNode:
    def __init__(self, data):
        self.data = data

# Graph
class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def addNode(self, data):
        node = GraphNode(data)
        self.adjacency_list[node] = []
        return node
    
    def removeNode(self, node):
        del self.adjacency_list[node]
        for adj_list in self.adjacency_list.values():
            adj_list[:] = [edge for edge in adj_list if edge[0] != node]

    def addEdge(self, n1, n2, weight=None):
        if n1 not in self.adjacency_list or n2 not in self.adjacency_list:
            raise ValueError("One or both nodes do not exist in the graph.")
        self.adjacency_list[n1].append((n2, weight))
        self.adjacency_list[n2].append((n1, weight))

    def removeEdge(self, n1, n2):
        if n1 not in self.adjacency_list or n2 not in self.adjacency_list:
            raise ValueError("One or both nodes do not exist in the graph.")
        self.adjacency_list[n1] = [edge for edge in self.adjacency_list[n1] if edge[0] != n2]
        self.adjacency_list[n2] = [edge for edge in self.adjacency_list[n2] if edge[0] != n1]

    def importFromFile(self, file):
        try:
            with open(file, 'r') as f:
                lines = f.readlines()
                if lines[0].strip() != 'strict graph G {':
                    raise ValueError("Error: Graph type is not 'strict graph G'")
                for line in lines[1:]:
                    if line.strip() == "}":
                        break
                    line_parts = line.strip().split("[")
                    nodes = line_parts[0].strip().split("--")
                    if len(nodes) != 2:
                        raise ValueError("Error: Invalid edge definition")
                    n1 = self.getNodeByData(nodes[0].strip())
                    n2 = self.getNodeByData(nodes[1].strip())
                    if not n1:
                        n1 = self.addNode(nodes[0].strip())
                    if not n2:
                        n2 = self.addNode(nodes[1].strip())
                    weight = 1  # Default weight is 1 if not specified
                    if len(line_parts) == 2:
                        weight_text = line_parts[1].strip().split("=")[1].split("]")[0]
                        weight = int(''.join(filter(str.isdigit, weight_text)))
                    self.addEdge(n1, n2, weight)
        except Exception as e:
            print("Error:", e)
            return None
        return self.adjacency_list

    def getNodeByData(self, data):
        for node in self.adjacency_list.keys():
            if node.data == data:
                return node
        return None

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        result = [start.data]
        for neighbor, _ in self.adjacency_list[start]:
            if neighbor not in visited:
                result.extend(self.dfs(neighbor, visited))
        return result

# Graph2
class Graph2(Graph):
    def __init__(self):
        super().__init__()
        self.adjacency_matrix = {}

    def addNode(self, data):
        node = GraphNode(data)
        self.adjacency_list[node] = []
        self.adjacency_matrix[node] = {}
        for n in self.adjacency_matrix:
            self.adjacency_matrix[node][n] = 0
            self.adjacency_matrix[n][node] = 0
        return node

    def addEdge(self, n1, n2, weight=None):
        if n1 not in self.adjacency_list or n2 not in self.adjacency_list:
            raise ValueError("One or both nodes do not exist in the graph.")
        self.adjacency_list[n1].append((n2, weight))
        self.adjacency_list[n2].append((n1, weight))
        self.adjacency_matrix[n1][n2] = weight
        self.adjacency_matrix[n2][n1] = weight

    def removeEdge(self, n1, n2):
        if n1 not in self.adjacency_list or n2 not in self.adjacency_list:
            raise ValueError("One or both nodes do not exist in the graph.")
        self.adjacency_list[n1] = [edge for edge in self.adjacency_list[n1] if edge[0] != n2]
        self.adjacency_list[n2] = [edge for edge in self.adjacency_list[n2] if edge[0] != n1]
        self.adjacency_matrix[n1][n2] = 0
        self.adjacency_matrix[n2][n1] = 0

    def dfs(self, start):
        visited = set()
        result = []
        stack = [start]

        while stack:
            node = stack.pop()
            if node not in visited:
                result.append(node.data)
                visited.add(node)
                for neighbor, _ in self.adjacency_list[node]:
                    if neighbor not in visited:
                        stack.append(neighbor)

        return result

# Main Code
file = "c:/Users/mattg/ENSF_338/lab8/random.dot"

graph = Graph()
graph2 = Graph2()
graph_data = graph.importFromFile(file)
graph2_data = graph2.importFromFile(file)
num_traversals = 10

# Graph (adjacency list)
start_node = None
if graph.adjacency_list:
    start_node = list(graph.adjacency_list.keys())[0]

if start_node:
    print("\nPerformance for Graph (adjacency list):")
    min_time = float('inf')
    max_time = 0
    total_time = 0
    for _ in range(num_traversals):
        try:
            time_taken = timeit.timeit(lambda: graph.dfs(start_node), number=1)
            total_time += time_taken
            min_time = min(min_time, time_taken)
            max_time = max(max_time, time_taken)
        except ValueError as e:
            print("Error:", e)
            exit()

    avg_time = total_time / num_traversals
    print("Minimum Time:", min_time)
    print("Maximum Time:", max_time)
    print("Average Time:", avg_time)
else:
    print("Graph is empty. Cannot perform DFS.")

# Graph2 (adjacency matrix)
start_node_graph2 = None
if graph2.adjacency_list:
    start_node_graph2 = list(graph2.adjacency_list.keys())[0]

if start_node_graph2:
    print("\nPerformance for Graph2 (adjacency matrix):")
    min_time = float('inf')
    max_time = 0
    total_time = 0
    for _ in range(num_traversals):
        try:
            time_taken = timeit.timeit(lambda: graph2.dfs(start_node_graph2), number=1)
            total_time += time_taken
            min_time = min(min_time, time_taken)
            max_time = max(max_time, time_taken)
        except ValueError as e:
            print("Error:", e)
            exit()

    avg_time = total_time / num_traversals
    print("Minimum Time:", min_time)
    print("Maximum Time:", max_time)
    print("Average Time:", avg_time)
else:
    print("Graph2 is empty. Cannot perform DFS.")

'''
Question 3.
Graph2, which uses an adjacency matrix, performed approximately 2x better than Graph, which uses an adjacency list.
The improved performance of the adjacency matrix over the adjacency list can be attributed to several factors.
However, graph density plays the most significant role, where the adjacency matrix tends to perform better for dense graphs, as is the case for this exercise,
while the adjacency list may excel for sparse graphs. First of all, this enhanced performance can be attribute to its constant-time edge lookup
In this case, the graph was quite dense, aiding in a better performance for Graph2. Memory overhead is another consideration,
with the adjacency matrix consuming more memory but offering efficient lookup. In dense graphs where the number of edges approaches the maximum possible (O(n^2) for n nodes),
the adjacency matrix consumes less memory compared to the adjacency list, as it only stores a boolean or weight value for each possible edge.
Additionally, both edge insertion and deletion operations can be performed in constant time (O(1)) with the adjacency matrix,
which is particularly advantageous for dense graphs with a large number of edges. Overall, the adjacency matrix is well-suited for dense graphs due to its efficient edge lookup,
constant-time operations, and memory efficiency, making it a preferred choice when handling such graph structures.
'''