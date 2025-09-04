from collections import deque

def bfs_trace(maze, start, end):
    # Directions: up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    queue = deque([start]) # Queue for BFS
    visited = set([start]) # Correct: set of tuples, initialized with start position
    trace = [] # List to store BFS traversal order

    while queue:
        current = queue.popleft()
        trace.append(current) # Record the current cell visited

        if current == end:
            return trace # Instead of True, return the trace

        for direction in directions:
            next_cell = (current[0] + direction[0], current[1] + direction[1])
            # Valid moves: within bounds, not wall, not visited
            if (0 <= next_cell[0] < len(maze) and
                0 <= next_cell[1] < len(maze[0]) and
                maze[next_cell[0]][next_cell[1]] != '#' and
                next_cell not in visited):
                queue.append(next_cell)
                visited.add(next_cell)
    # If the end not found, still return trace
    return trace

# Example maze
maze = [
    ['S', '.', '.', '#', '.', '.', '.'],
    ['.', '#', '.', '#', '.', '#', '.'],
    ['.', '#', '.', '.', '.', '.', '.'],
    ['.', '.', '#', '#', '#', '.', '.'],
    ['.', '#', '.', '.', '.', '#', '.'],
    ['.', '#', '#', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.', '.', 'E'],
]

start = (0, 0)
end = (6, 6)

trace = bfs_trace(maze, start, end)
print("BFS Trace (Order of cells visited):")
print(trace)
