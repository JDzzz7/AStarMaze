# A star maze implementation

from maze_gen import *

class Node():
    def __init__(self, parent=None, pos=None):
        self.parent = parent
        self.pos = pos
        self.f = 0
        self.h = 0
        self.g = 0

def get_h(cell_curr: tuple, cell_goal: tuple)->int:
    h = abs(cell_curr[1] - cell_goal[1]) + abs(cell_curr[0] - cell_goal[0])
    return h

def get_distance(cell_child: tuple, cell_parent: tuple)->int:
    d = abs(cell_parent[1] - cell_child[1]) + abs(cell_parent[0] - cell_child[0])
    return d

def a_star(start: tuple, end: tuple, maze: object)->list:
    m = maze.generate()
    open_lst = []
    closed_lst = []
    start_node = Node(None, start)
    index = 0

    open_lst.append(start_node)

    for blah in range(10):
        curr_node = open_lst[0]
        index = 0
        print(f"current:{curr_node.pos}")
        #for thing in open_lst:
        #    print(f"opened:{thing.pos, thing.f, thing.g, thing.h}")
        #for closed in closed_lst:
        #    print(f"closed:{closed.pos, closed.f, closed.g, closed.h}")
        for i in range(len(open_lst)):
            print(f"open: {(open_lst[i]).f}   curr{curr_node.f}")
            if (open_lst[i]).f < curr_node.f:
                curr_node = open_lst[i]
                print("here")
                index = i
        # print(index)
        open_lst.pop(index)
        #print(f"openlst{open_lst}")
        # print(f"closedlst{closed_lst}")
        # print(f"hello{arrived.pos}")
        closed_lst.append(curr_node)
        print("hello")
        if curr_node.pos == end:
            # Goal reached
            a_path = []
            dup_path = []
            maze_path = []
            curr = curr_node
            print("in here?")
            while(curr):
                print(f"finally{curr.pos}")
                a_path.append(curr.pos)
                curr = curr.parent

            dup_path = a_path[:]
            for cell in a_path:
                maze_path.append(dup_path.pop())
            print("PATH FOUND!")
            return maze_path
        
        neighbors = maze.get_neighbors(m)
        children_pos_lst = neighbors[curr_node.pos]
        print(f"children positions{children_pos_lst}")
        # SUCC NODES BB
        children_lst = []
        succ_lst = []

        for p in children_pos_lst:
            child_node = Node(curr_node, p)
            children_lst.append(child_node)

        for child in children_lst:
            for close in closed_lst:
                print(f"child:{child.pos}, close:{close.pos}")
                if child.pos == close.pos:
                    continue
                succ_lst.append(child)
            print(succ_lst)

        for succ in succ_lst:

            print(f"succ now:{succ.pos}")
            succ.h = get_h(succ.pos, end)
            succ.g = curr_node.g + get_distance(succ.pos, curr_node.pos)
            succ.f = succ.g + succ.h
            
            if len(open_lst) == 0:
                open_lst.append(succ)
                continue

            for node in open_lst:
                if (node.pos != succ.pos) and (node.g > succ.g):
                    open_lst.append(succ)





    print(f"Path not Found")
            


if __name__ == '__main__':
    maze = Maze(4,4)
    print(a_star((1,1), (4,4), maze))
