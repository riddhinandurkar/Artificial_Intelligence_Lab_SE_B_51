from collections import deque

# Define the maze
maze = [
    ['#', '#', '#', '#', '#', '#', '#'],
    ['#', 'S', ' ', ' ', '#', 'E', '#'],
    ['#', '#', '#', ' ', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#']
]

# Find start (S) and end (E) positions
def find_start_and_end(maze):
    start = end = None
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == 'S':
                start = (i, j)
            elif value == 'E':
                end = (i, j)
    return start, end

# Get neighbors (up, down, left, right)
def get_neighbors(pos, maze):
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    neighbors = []
    rows, cols = len(maze), len(maze[0])
    for dr, dc in directions:
        r, c = pos[0] + dr, pos[1] + dc
        if 0 <= r < rows and 0 <= c < cols and maze[r][c] != '#':
            neighbors.append((r, c))
    return neighbors

# BFS Algorithm
def bfs(maze):
    start, end = find_start_and_end(maze)
    queue = deque([start])
    visited = set()
    parent = {start: None}

    while queue:
        current = queue.popleft()
        if current == end:
            break
        for neighbor in get_neighbors(current, maze):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    return reconstruct_path(parent, start, end)

# DFS Algorithm
def dfs(maze):
    start, end = find_start_and_end(maze)
    stack = [start]
    visited = set()
    parent = {start: None}

    while stack:
        current = stack.pop()
        if current == end:
            break
        if current in visited:
            continue
        visited.add(current)
        for neighbor in get_neighbors(current, maze):
            if neighbor not in visited:
                parent[neighbor] = current
                stack.append(neighbor)

    return reconstruct_path(parent, start, end)

# Reconstruct path from parent dictionary
def reconstruct_path(parent, start, end):
    path = []
    current = end
    while current and current != start:
        path.append(current)
        current = parent.get(current)
    if current == start:
        path.append(start)
        path.reverse()
        return path
    return None

# Print the maze with the path
def print_maze_with_path(maze, path):
    maze_copy = [row[:] for row in maze]  # Deep copy
    if path:
        for r, c in path:
            if maze_copy[r][c] not in ('S', 'E'):
                maze_copy[r][c] = '*'
    for row in maze_copy:
        print(''.join(row))

# Run both algorithms and print results
print("BFS Path:")
bfs_path = bfs(maze)
print_maze_with_path(maze, bfs_path)

print("\nDFS Path:")
dfs_path = dfs(maze)
print_maze_with_path(maze, dfs_path)

