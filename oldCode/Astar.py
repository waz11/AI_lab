import time

from board import Board
from node import Node

class Astar:
    def __init__(self, initial_state):
        self.initial_state :Board = Board(initial_state)
        self.initial_state_node = Node(self.initial_state)

    def search(self):
        open = []
        closed = []
        num_of_nodes = 0
        open.append(self.initial_state_node)
        while(len(open)>0):
            num_of_nodes+=1
            open.sort(key=lambda x: (x.f,x.h), reverse=False)
            curr:Node = open[0]
            closed.append(curr)
            del open[0]
            if(curr.h == 0):
                return num_of_nodes-1
            else:
                for neighbor in curr.get_neighbors():
                    if closed.__contains__(neighbor):
                        continue
                    elif not closed.__contains__(neighbor):
                        open.append(neighbor)
        return False



def main():
    search = Astar([1,2,3,4,5,6,0,7,8])
    # search = Astar([1, 4, 7, 6, 3, 8, 2, 5, 0])
    # search = Astar([3, 4, 0, 6, 1, 8, 2, 5, 7])
    # search = Astar([2, 8, 1,5, 0, 3,7, 6, 4])
    start_time = time.time()
    nodes = search.search()
    end_time = time.time()
    print(nodes, end_time-start_time)


if __name__ == '__main__':
    main()

