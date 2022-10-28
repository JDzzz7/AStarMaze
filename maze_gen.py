import random

# Generate a random maze

# Node class for maze cell
class Node():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.directions = {"north": True, "south": True, "east": True, "west": True}
        self.visited = False

# Generate the grid for the maze
def gen_grid(rows: int, cols: int)->list:
    # grid[y][x] = (x, y)
    grid = [[] for i in range(rows)]
    for i in range(rows):
        for j in range(cols):
            cell = Node(j, i)
            grid[i].append(cell)
    return grid

def get_neighbors(grid: list):
    pass
        
# Get the next adjacent cell randomly
def get_rand_path(curr_cell: Node, grid: list, rows: int, cols: int)->Node:
    # check if curr cell neighbors are out of bounds
    x = curr_cell.x
    y = curr_cell.y
    picks = []
    
    # North
    if (y-1 >= 0) and not (grid[y-1][x]).visited:
        picks.append(grid[y-1][x])
    # South
    if (y+1 <= rows-1) and not (grid[y+1][x]).visited:
        picks.append(grid[y+1][x])
    # East
    if (x+1 <= cols-1) and not (grid[y][x+1]).visited:
        picks.append(grid[y][x+1])
    # West
    if (x-1 >= 0) and not (grid[y][x-1]).visited:
        picks.append(grid[y][x-1])

    if len(picks) == 0:
        return False
    return random.choice(picks)

def tear_walls(curr: Node, adj: Node):
    # Walls: north curr, south adj
    if curr.y - adj.y == 1:
        curr.directions["north"] = False
        adj.directions["south"] = False

    # Walls: south curr, north adj
    if curr.y - adj.y == -1:
        curr.directions["south"] = False
        adj.directions["north"] = False

    # Walls: east curr, west adj
    if curr.x - adj.x == -1:
        curr.directions["east"] = False
        adj.directions["west"] = False
    
    # Walls: west curr, east adj
    if curr.x - adj.x == 1:
        curr.directions["west"] = False
        adj.directions["east"] = False

def DFS(curr_cell: Node, grid: list, traversal: list, rows: int, cols: int):
    adj_cell = get_rand_path(curr_cell, grid, rows, cols)
    if adj_cell:
        adj_cell.visited = True
        tear_walls(curr_cell, adj_cell)
        curr_cell = adj_cell
        traversal.append(curr_cell)
        DFS(curr_cell, grid, traversal, rows, cols)

    elif len(traversal) != 0:
        curr_cell = traversal.pop()
        DFS(curr_cell, grid, traversal, rows, cols)


