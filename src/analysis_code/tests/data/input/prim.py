import heapq


def prim(graph):
    start_node = list(graph.keys())[0]
    visited = set([start_node])
    edges = [
        (weight, start_node, next_node)
        for next_node, weight in graph[start_node].items()
    ]
    heapq.heapify(edges)
    minimum_spanning_tree = []
    while edges:
        weight, node1, node2 = heapq.heappop(edges)
        if node2 not in visited:
            visited.add(node2)
            minimum_spanning_tree.append((weight, node1, node2))
            for next_node, weight in graph[node2].items():
                if next_node not in visited:
                    heapq.heappush(edges, (weight, node2, next_node))
    return minimum_spanning_tree
