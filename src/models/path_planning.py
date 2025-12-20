import heapq

def a_star(start, goal, obstacles):
    """
    Simple A* path planner
    """

    open_set = []
    heapq.heappush(open_set, (0, start))

    visited = set()

    while open_set:
        cost, current = heapq.heappop(open_set)

        if current == goal:
            return "Safe path found"

        if current in visited:
            continue

        visited.add(current)

        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            neighbor = (current[0] + dx, current[1] + dy)

            if neighbor in obstacles:
                continue

            heapq.heappush(open_set, (cost + 1, neighbor))

    return "No safe path"


if __name__ == "__main__":
    start = (0, 0)
    goal = (5, 5)
    obstacles = {(2,2), (3,3)}

    print(a_star(start, goal, obstacles))
