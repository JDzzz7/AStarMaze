import pygame
from pygame.locals import *
import random

# Initializing pygame
pygame.init()

# Defining screen size, background, visited, line colors & length of cells
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BACKGROUND = pygame.Color("#191970")
V_COLOR = pygame.Color("#000000")
LINE_COLOR = pygame.Color("#03FFE8")
LENGTH = 100

# Dynamic rows and cols gen depending on screen width/height and tile size
ROWS = SCREEN_HEIGHT // LENGTH
COLS = SCREEN_WIDTH // LENGTH
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Node class for maze cell
class Node():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.directions = {"north": True, "south": True, "east": True, "west": True}
        self.visited = False

# Generate the grid for the maze
def gen_grid()->list:
    # grid[y][x] = (x, y)
    grid = [[] for i in range(ROWS)]
    for i in range(ROWS):
        for j in range(COLS):
            cell = Node(j, i)
            grid[i].append(cell)
    return grid

def draw_graphics(cell: Node):
    x = cell.x * LENGTH
    y = cell.y * LENGTH

    if cell.visited:
        pygame.draw.rect(screen, V_COLOR, (x, y, LENGTH, LENGTH))
    
    if cell.directions["north"]:
        pygame.draw.line(screen, LINE_COLOR, (x, y), (x + LENGTH, y))
    if cell.directions["south"]:
        pygame.draw.line(screen, LINE_COLOR, (x, y + LENGTH), (x + LENGTH, y + LENGTH))
    if cell.directions["east"]:
        pygame.draw.line(screen, LINE_COLOR, (x + LENGTH, y), (x + LENGTH, y + LENGTH))
    if cell.directions["west"]:
        pygame.draw.line(screen, LINE_COLOR, (x, y), (x, y + LENGTH))

def draw_grid(grid: list):
    for i in range(ROWS):
        for j in range(COLS):
            draw_graphics(grid[i][j])

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


# Get the next adjacent cell randomly
def get_rand_path(curr_cell: Node, grid: list)->Node:
    # check if curr cell neighbors are out of bounds
    x = curr_cell.x
    y = curr_cell.y
    picks = []
    
    # North
    if (y-1 >= 0) and not (grid[y-1][x]).visited:
        picks.append(grid[y-1][x])
    # South
    if (y+1 <= ROWS-1) and not (grid[y+1][x]).visited:
        picks.append(grid[y+1][x])
    # East
    if (x+1 <= COLS-1) and not (grid[y][x+1]).visited:
        picks.append(grid[y][x+1])
    # West
    if (x-1 >= 0) and not (grid[y][x-1]).visited:
        picks.append(grid[y][x-1])

    if len(picks) == 0:
        return False
    return random.choice(picks)

    
if __name__ == '__main__':
    clock = pygame.time.Clock()
    clock.tick(30)
    running = True
    
    grid = gen_grid()
    curr_cell = grid[0][0]

    while running:
        screen.fill(BACKGROUND)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        curr_cell.visited = True
        draw_grid(grid)

        adj_cell = get_rand_path(curr_cell, grid)
        if adj_cell:
            adj_cell.visited = True
            tear_walls(curr_cell, adj_cell)
            curr_cell = adj_cell


        pygame.display.flip()

pygame.quit()
