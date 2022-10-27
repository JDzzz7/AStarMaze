# A star maze implementation

from maze_gen import *

# Node class for A* search
class Node():
    def __init__(self, parent=None, pos=None):
        self.parent = parent
        self.pos = pos
        self.f = 0
        self.h = 0
        self.g = 0

# Returns the h (distance from current cell to goal)  
def get_h(cell_curr: tuple, cell_goal: tuple)->int:
    h = abs(cell_curr[1] - cell_goal[1]) + abs(cell_curr[0] - cell_goal[0])
    return h

# Returns the g (distance from start to current cell)
def get_distance(cell_child: tuple, cell_parent: tuple)->int:
    d = abs(cell_parent[1] - cell_child[1]) + abs(cell_parent[0] - cell_child[0])
    return d

# A star search function 
def a_star(start: tuple, end: tuple, maze: object)->list:
    m = maze.generate()
    open_lst = []
    closed_lst = []
    start_node = Node(None, start)
    
    open_lst.append(start_node)
    
    while len(open_lst) != 0:
        curr_node = open_lst[0]
        index = 0
        # print(f"current:{curr_node.pos}")

        # for thing in open_lst:
        #    print(f"opened:{thing.pos, thing.f, thing.g, thing.h}")
        # for closed in closed_lst:
        #    print(f"closed:{closed.pos, closed.f, closed.g, closed.h}")

        # Get the node with the lowest f in open_lst
        for i in range(len(open_lst)):
            # print(f"open: {(open_lst[i]).f}   curr{curr_node.f}")
            if (open_lst[i]).f < curr_node.f:
                curr_node = open_lst[i]
                index = i

        open_lst.pop(index)

        # print(f"openlst{open_lst}")
        # print(f"closedlst{closed_lst}")
        # print(f"hello{arrived.pos}")
        
        # if current node is the goal, return the path
        if curr_node.pos == end:
            a_path = []
            dup_path = []
            maze_path = []
            curr = curr_node
            while(curr):
                a_path.append(curr.pos)
                curr = curr.parent

            dup_path = a_path[:]
            for cell in a_path:
                maze_path.append(dup_path.pop())
            print("PATH FOUND!")
            return maze_path
       
        # Generate children of current node
        neighbors = maze.get_neighbors(m)
        children_pos_lst = neighbors[curr_node.pos]

        children_lst = []
        succ_lst = []
        
        # Creating children nodes of current node
        for p in children_pos_lst:
            child_node = Node(curr_node, p)
            children_lst.append(child_node)
        
        # Get g,h,f of all children nodes
        for child in children_lst:
            child.h = get_h(child.pos, end)
            child.g = curr_node.g + get_distance(child.pos, curr_node.pos)
            child.f = child.g + child.h
       
        # Skip child node if node is in open_lst and has a lower f than child node
        # Otherwise, add the child node to succ_lst
        for child in children_lst:
            flag = 1
            for node in open_lst:
                if (node.pos == child.pos) and (node.f < child.f):
                    flag = 0
            if flag == 1:
                succ_lst.append(child)
        
        # Skip succ node if node is in closed_lst and has a lower f than succ node
        # Otherwise, add the succ node to open_lst
        for succ in succ_lst:
            flag = 1
            for node in closed_lst:
                if (node.pos == succ.pos) and (node.f < succ.f):
                    flag = 0
            if flag == 1:
                open_lst.append(succ)
        
        # Add curr node to closed_lst, all children visited.
        closed_lst.append(curr_node)
    
    # if open_lst is empty and goal not reached
    print(f"Path not Found")
            
if __name__ == '__main__':
    maze = Maze(4,4)
    print(a_star((1,1), (4,4), maze))
