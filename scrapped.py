# Maze generator for maze game
# (y, x) (rows, cols)

import random

class Maze():
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols

    def generate(self):
        grid = []
        for y in range(self.rows):
            for x in range(self.cols):
                point = (x+1, y+1)
                grid.append(point)
        return grid

    def p_move(self, grid: list)->dict:
        movement = {}
        for i in range(len(grid)):
            movement[grid[i]] = {}
        for i in range(len(grid)):
            if grid[i][1] == self.rows:
                movement[grid[i]]['S'] = 0
            else:
                movement[grid[i]]['S'] = 1
            if grid[i][0] == self.rows:
                movement[grid[i]]['E'] = 0
            else:
                movement[grid[i]]['E'] = 1
            if grid[i][1] == 1:
                movement[grid[i]]['N'] = 0
            else:
                movement[grid[i]]['N'] = 1
            if grid[i][0] == 1:
                movement[grid[i]]['W'] = 0
            else:
                movement[grid[i]]['W'] = 1
        return movement

    def get_neighbors(self, grid: list)->dict:
        adj_map = {}
        for i in range(len(grid)):
            # South
            if grid[i][1] != self.rows:
                if grid[i] not in adj_map:
                    adj_map[grid[i]] = [(grid[i][0], (grid[i][1])+1)]
                else:
                    adj_map[grid[i]].append((grid[i][0], (grid[i][1])+1))
            # East
            if grid[i][0] != self.cols:
                if grid[i] not in adj_map:
                    adj_map[grid[i]] = [((grid[i][0])+1, grid[i][1])]
                else:
                    adj_map[grid[i]].append(((grid[i][0])+1, grid[i][1]))
            # North
            if grid[i][1] != 1:
                if grid[i] not in adj_map:
                    adj_map[grid[i]] = [(grid[i][0], (grid[i][1])-1)]
                else:
                    adj_map[grid[i]].append((grid[i][0], (grid[i][1])-1))
            # West
            if grid[i][0] != 1:
                if grid[i] not in adj_map:
                    adj_map[grid[i]] = [((grid[i][0])-1, grid[i][1])]
                else:
                    adj_map[grid[i]].append(((grid[i][0])-1, grid[i][1]))
        return adj_map


if __name__ == '__main__':
    maze = Maze(4, 4)
    m = maze.generate()
    #print(m)
    print(maze.get_neighbors(m))
    print(maze.p_move(m))
