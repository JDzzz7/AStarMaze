# Maze generator for maze game
# (y, x) (rows, cols)

import random

class Maze():
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
    
    def generate(self):
        grid = []
        for r in range(self.rows):
            for c in range(self.cols):
                point = (r+1, c+1)
                grid.append(point)
        return grid

    # South = 0, East = 1, North = 2, West = 3
    # Use dict with list in it
    def p_move(self, grid: list):
        movement = {}
        for j in range(len(grid)):
            if grid[j][0] == self.rows:
                movement[grid[j]]['S'] = 0
            if grid[j][1] == self.rows:
                movement[grid[j]]['E'] = 0
            if grid[j][0] == 1:
                movement[grid[j]]['N'] = 0
            if grid[j][1] == 1:
                movement[grid[j]]['W'] = 0
        return movement

    def get_neighbors(self, grid: list):
        adj_map = {}
        for j in range(len(grid)):
            # South
            if grid[j][0] != self.rows:
                if grid[j] not in adj_map:
                    adj_map[grid[j]] = [((grid[j][0])+1, grid[j][1])]
                else:
                    adj_map[grid[j]].append(((grid[j][0])+1, grid[j][1]))
            # East
            if grid[j][1] != self.cols:
                if grid[j] not in adj_map:
                    adj_map[grid[j]] = [(grid[j][0], (grid[j][1])+1)]
                else:
                    adj_map[grid[j]].append((grid[j][0], (grid[j][1])+1))
            # North
            if grid[j][0] != 1:
                if grid[j] not in adj_map:
                    adj_map[grid[j]] = [((grid[j][0])-1, grid[j][1])]
                else:
                    adj_map[grid[j]].append(((grid[j][0])-1, grid[j][1]))
            # West
            if grid[j][1] != 1:
                if grid[j] not in adj_map:
                    adj_map[grid[j]] = [(grid[j][0], (grid[j][1])-1)]
                else:
                    adj_map[grid[j]].append((grid[j][0], (grid[j][1])-1))
        return adj_map


if __name__ == '__main__':
    maze = Maze(4, 4)
    m = maze.generate()
    print(maze.get_neighbors(m))
    print(maze.p_move(m))
