#Question 1
#Topological sorting can be implemented using a DFS algorithm (Depth-First Search)
#DFS is used for topological sorting because it explores each node in depth while traversing.
#It works by starting at a random node and then traversing the nodes next to it and marking each one 
#as "visited" and then adding them to a stack. Once all the nodes have been traversed over, the stack 
#ends up in reverse topological order. Then it can be simply reversed and you end up with the graph
#in topological order.

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
                    weight = 1 
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
    
    def isdag(self):
        visited = set()
        stack = set()

        def dfs(self, start):
            visited = set()
            stack = [(start, None)]  

            while stack:
                node, parent = stack.pop()
                if node in visited:
                    return True 
                visited.add(node)
                for neighbor, _ in self.adjacency_list.get(node, []):
                    if neighbor != parent: 
                        stack.append((neighbor, node))

            return False

    def toposort(self):
        if not self.isdag():
            return None  

        visited = set()
        result = []

        def dfs(node):
            visited.add(node)
            for neighbor, _ in self.adjacency_list.get(node, []):
                if neighbor not in visited:
                    dfs(neighbor)
            result.append(node)

        for node in self.adjacency_list:
            if node not in visited:
                dfs(node)

        return result[::-1]  

