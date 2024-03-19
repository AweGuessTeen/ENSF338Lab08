class GraphNode:
    def __init__(self, data):
        self.data = data

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
                if lines[0].strip() != 'strict graph G':
                    return None
                edges = lines[1:-1]
                for edge in edges:
                    edge = edge.strip().split()
                    n1 = edge[0]
                    n2 = edge[2]
                    if len(edge) == 4:
                        weight = int(edge[3][7:-1])
                        self.addEdge(n1, n2, weight)
                    else:
                        self.addEdge(n1, n2)
        except:
            return None
        return self.adjList

    def getNodeByData(self, data):
        for node in self.adjacency_list.keys():
            if node.data == data:
                return node
        return None
