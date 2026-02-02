from collections import deque
def water_jug(jug1, jug2, target):
    visited = set()
    queue = deque([(0, 0)])
    while queue:
        x, y = queue.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        print(x, y)
        if x == target or y == target:
            print("Target reached!")
            return
        queue.append((jug1, y))       
        queue.append((x, jug2))       
        queue.append((0, y))          
        queue.append((x, 0))          
        queue.append((x - min(x, jug2 - y), y + min(x, jug2 - y)))  
        queue.append((x + min(y, jug1 - x), y - min(y, jug1 - x)))  
water_jug(4, 3, 2)
