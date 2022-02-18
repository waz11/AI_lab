from itertools import combinations, chain

from board import Board
from node import Node


class Astar:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def search(self):
        open = []
        closed = []
        num_of_nodes = 0
        open.append(self.initial_state)
        while(len(open)>0):
            num_of_nodes+=1

            curr:Node = open[0]
            closed.append(curr)
            del open[0]
            if(curr.h == 0):
                return num_of_nodes
            else:
                for neighbor in curr.get_neighbors():
                    if closed.__contains__(neighbor):
                        continue
                    elif not closed.__contains__(neighbor):
                        open.append(neighbor)
                open.sort(key=lambda x: (x.f,x.h), reverse=False)
        return False


def main():
    initial_state = Board([6,7,3,1,8,2,5,4,0])
    goal_state = Board([1,2,3,4,5,6,7,8,0])
    n = Node(initial_state, goal_state)
    search = Astar(n, goal_state)
    print(search.search())


if __name__ == '__main__':
    main()
