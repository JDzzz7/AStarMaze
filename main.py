import pygame
from pygame.locals import *
from maze_gen import *

# Initializing pygame
pygame.init()
pygame.display.set_caption('Random Maze')

# Defining screen size, background, visited, line colors & length of cells
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 780
BACKGROUND = pygame.Color("#191970")
V_COLOR = pygame.Color("#000000")
LINE_COLOR = pygame.Color("#03FFE8")
LENGTH = 30

# Dynamic rows and cols gen depending on screen width/height and tile size
ROWS = SCREEN_HEIGHT // LENGTH
COLS = SCREEN_WIDTH // LENGTH
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def draw_graphics(cell: Node):
    x = cell.x * LENGTH
    y = cell.y * LENGTH

    if cell.visited:
        pygame.draw.rect(screen, V_COLOR, (x, y, LENGTH, LENGTH))
    
    if cell.directions["north"]:
        pygame.draw.line(screen, LINE_COLOR, (x, y), (x + LENGTH, y), 3)
    if cell.directions["south"]:
        pygame.draw.line(screen, LINE_COLOR, (x, y + LENGTH), (x + LENGTH, y + LENGTH), 3)
    if cell.directions["east"]:
        pygame.draw.line(screen, LINE_COLOR, (x + LENGTH, y), (x + LENGTH, y + LENGTH), 3)
    if cell.directions["west"]:
        pygame.draw.line(screen, LINE_COLOR, (x, y), (x, y + LENGTH), 3)

def draw_grid(grid: list):
    for i in range(ROWS):
        for j in range(COLS):
            draw_graphics(grid[i][j])

if __name__ == '__main__':
    running = True
    flag = 0
    grid = gen_grid(ROWS, COLS)
    curr_cell = grid[0][0]
    traversal = []

    while running:
        screen.fill(BACKGROUND)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        draw_grid(grid)

        if flag == 0:
            curr_cell.visited = True
            DFS(curr_cell, grid, traversal, ROWS, COLS)
            flag = 1

        pygame.display.flip()

pygame.quit()
