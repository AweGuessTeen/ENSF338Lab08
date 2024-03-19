# #  Question 1
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