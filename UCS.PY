import heapq

def ucs(graph, start, goal):
    priority_queue = [(0, start, [start])]
    visited = set()

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)

        if node == goal:
            return path, cost

        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph[node]:
                heapq.heappush(
                    priority_queue,
                    (cost + weight, neighbor, path + [neighbor])
                )

    return None


# -------- GIVEN INPUT --------
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

start = 'A'
goal = 'F'

# -------- EXECUTION --------
path, cost = ucs(graph, start, goal)
print("UCS Path:", path)
print("Total Cost:", cost)
