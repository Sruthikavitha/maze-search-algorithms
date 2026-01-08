import collections
import heapq
import matplotlib.pyplot as plt

# Prompt user for maze input
maze_input_string = input("Enter maze configuration (e.g., 'S010,1010,000G'): ")

# Convert input string to maze list of lists
maze_rows_str = maze_input_string.split(',')
maze = [list(row) for row in maze_rows_str]

ROWS, COLS = len(maze), len(maze[0])
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Define MOVES for up, down, left, right

def find_pos(symbol):
    for i in range(ROWS):
        for j in range(COLS):
            if maze[i][j] == symbol:
                return i, j

def valid(x, y):
    return 0 <= x < ROWS and 0 <= y < COLS and maze[x][y] != '1'

#BFS
def bfs_maze():
    start = find_pos('S')
    goal = find_pos('G')
    queue = collections.deque([(start, [start])]) # Use collections.deque
    visited = set([start])

    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == goal:
            return path

        for dx, dy in MOVES:
            nx, ny = x+dx, y+dy
            if valid(nx, ny) and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))

#DFS
def dfs_maze():
    start = find_pos('S')
    goal = find_pos('G')
    stack = [(start, [start])]
    visited = set()

    while stack:
        (x, y), path = stack.pop()
        if (x, y) == goal:
            return path

        if (x, y) not in visited:
            visited.add((x, y))
            for dx, dy in MOVES:
                nx, ny = x+dx, y+dy # Corrected from y+ny to y+dy
                if valid(nx, ny):
                    stack.append(((nx, ny), path + [(nx, ny)]))

#A*
def manhattan(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def astar_maze():
    start = find_pos('S')
    goal = find_pos('G')
    pq = []
    heapq.heappush(pq, (0, start, [start]))
    visited = set()

    while pq:
        f, current, path = heapq.heappop(pq)
        if current == goal:
            return path

        if current not in visited:
            visited.add(current)
            for dx, dy in MOVES:
                nx, ny = current[0]+dx, current[1]+dy
                if valid(nx, ny):
                    g = len(path)
                    h = manhattan((nx, ny), goal)
                    heapq.heappush(pq, (g+h, (nx, ny), path + [(nx, ny)]))


bfs_path = bfs_maze()
dfs_path = dfs_maze()
astar_path = astar_maze()

print("BFS Path:", bfs_path)
print("DFS Path:", dfs_path)
print("A* Path:", astar_path)

def plot_maze(maze, bfs_path=None, dfs_path=None, astar_path=None):
    fig, ax = plt.subplots(figsize=(COLS, ROWS))

    # Draw maze
    for r in range(ROWS):
        for c in range(COLS):
            if maze[r][c] == '1': # Wall
                ax.add_patch(plt.Rectangle((c, r), 1, 1, facecolor='black', edgecolor='gray'))
            elif maze[r][c] == '0': # Open path
                ax.add_patch(plt.Rectangle((c, r), 1, 1, facecolor='white', edgecolor='gray'))
            elif maze[r][c] == 'S': # Start
                ax.add_patch(plt.Rectangle((c, r), 1, 1, facecolor='green', edgecolor='gray'))
            elif maze[r][c] == 'G': # Goal
                ax.add_patch(plt.Rectangle((c, r), 1, 1, facecolor='red', edgecolor='gray'))

    # Draw paths
    if bfs_path:
        bfs_coords = [[p[1] + 0.5, p[0] + 0.5] for p in bfs_path]
        ax.plot([c[0] for c in bfs_coords], [c[1] for c in bfs_coords], color='blue', linewidth=2, label='BFS Path')

    if dfs_path:
        dfs_coords = [[p[1] + 0.5, p[0] + 0.5] for p in dfs_path]
        ax.plot([c[0] for c in dfs_coords], [c[1] for c in dfs_coords], color='orange', linewidth=2, label='DFS Path')

    if astar_path:
        astar_coords = [[p[1] + 0.5, p[0] + 0.5] for p in astar_path]
        ax.plot([c[0] for c in astar_coords], [c[1] for c in astar_coords], color='purple', linewidth=2, label='A* Path')

    ax.set_xticks(range(COLS + 1))
    ax.set_yticks(range(ROWS + 1))
    ax.grid(True, color='gray', linestyle='--', linewidth=0.5)
    ax.set_aspect('equal', adjustable='box')
    ax.set_title('Maze Paths')
    ax.legend()
    plt.show()

plot_maze(maze, bfs_path, dfs_path, astar_path)