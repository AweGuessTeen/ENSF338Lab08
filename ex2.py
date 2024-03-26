## Question 1
# For the performance of Dijkstra's algorithm is it's very crucial to implement the queue efficiently
# Two possible ways to implement in the queue are:

# 1) Slow Implementation (Linear Search):
#     In this implementation, we can use a simple list or array to store nodes along with their distances
#     from the source. When searching for the node with the smallest distance, we can iterate thorough the
#     entire list or array to find the minimum distance node. This approach will have a time complexity of 
#     O(n), where n is the number of nodes in the queue.

# 2) Faster Implementation (Priority Queue):
#     A priority queue is a data structure that efficiently supports the following operations:
#         i) Insertion of elements
#         ii) Extraction of the minimum (or maximum) element
#     We can also implement a priority queue using a binary heap or other data structures related for this
#     purpose. These implementations typically have efficient insertion and extraction of the minimum element,
#     oftern with a time complexity of O(log n), where n is the number of elements in the queue. This would
#     significantly improve the efficiency of Dijkstra's algorithm compared to the linear search method.

## Question 2 
import time
import numpy as np
import matplotlib.pyplot as plt
import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))

    def slowSP(self, node):
        distances = {node: 0}
        queue = [node]

        while queue:
            current_node = queue.pop(0)
            if current_node not in self.graph:
                continue  # Skip if the node has no outgoing edges
            for neighbor, weight in self.graph[current_node]:
                if neighbor not in distances or distances[neighbor] > distances[current_node] + weight:
                    distances[neighbor] = distances[current_node] + weight
                    queue.append(neighbor)

        return distances

    def fastSP(self, node):
        distances = {node: 0}
        queue = [(0, node)]

        while queue:
            dist, current_node = heapq.heappop(queue)
            if current_node not in self.graph:
                continue  # Skip if the node has no outgoing edges
            if dist > distances[current_node]:
                continue
            for neighbor, weight in self.graph[current_node]:
                if neighbor not in distances or distances[neighbor] > dist + weight:
                    distances[neighbor] = dist + weight
                    heapq.heappush(queue, (dist + weight, neighbor))

        return distances

def load_graph_from_dot(filename):
    graph = Graph()
    with open(filename, 'r') as file:
        for line in file:
            if ' -- ' in line:
                parts = line.strip().split()
                u, v = parts[0], parts[2]
                weight_str = parts[3].split('=')[1].strip('[];')
                weight = int(weight_str)
                graph.add_edge(u, v, weight)
    return graph

## Question 3

def measure_performance(graph):
    slow_times = []
    fast_times = []
    nodes = list(graph.graph.keys())

    for node in nodes:
        start_time = time.time()
        graph.slowSP(node)
        end_time = time.time()
        slow_times.append(end_time - start_time)

        start_time = time.time()
        graph.fastSP(node)
        end_time = time.time()
        fast_times.append(end_time - start_time)

    return slow_times, fast_times

## Question 4

def plot_histogram(execution_times):
    plt.hist(execution_times, bins=10, color='blue', alpha=0.7)
    plt.title('Distribution of Execution Times')
    plt.xlabel('Execution Time (seconds)')
    plt.ylabel('Frequency')
    plt.show()

def main():
    graph = load_graph_from_dot("random.dot")

    slow_times, fast_times = measure_performance(graph)

    slow_avg = np.mean(slow_times) if slow_times else 0
    slow_max = np.max(slow_times) if slow_times else 0
    slow_min = np.min(slow_times) if slow_times else 0

    fast_avg = np.mean(fast_times) if fast_times else 0
    fast_max = np.max(fast_times) if fast_times else 0
    fast_min = np.min(fast_times) if fast_times else 0

    print("Slow algorithm:")
    print("Average time:", slow_avg)
    print("Max time:", slow_max)
    print("Min time:", slow_min)

    print("Fast algorithm:")
    print("Average time:", fast_avg)
    print("Max time:", fast_max)
    print("Min time:", fast_min)

    plot_histogram(slow_times + fast_times)

if __name__ == "__main__":
    main()


