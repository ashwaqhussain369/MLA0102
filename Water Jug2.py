def water_jug_state(jug1, jug2, target):
    visited = set()
    stack = [(0, 0)]
    while stack:
        x, y = stack.pop()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        print(x, y)
        if (x, y) == target:
            print("Target state reached!")
            return
        stack.append((jug1, y))       
        stack.append((x, jug2))       
        stack.append((0, y))          
        stack.append((x, 0))          
        stack.append((x - min(x, jug2 - y), y + min(x, jug2 - y)))
        stack.append((x + min(y, jug1 - x), y - min(y, jug1 - x)))
water_jug_state(4, 3, (2, 0))
