from board import Board
from node import Node


class Astar:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def search(self):
        open = []
        closed = []
        open.append(self.initial_state)
        while(len(open)>0):
            curr:Node = open[0]
            closed.append(curr)
            del open[0]

            if(curr.h == 0):
                print(curr)
                return True
            else:
                for neighbor in curr.get_neighbors():
                    if closed.__contains__(neighbor):
                        print("ron")
                    if not closed.__contains__(neighbor):
                        open.append(neighbor)
                open.sort(key=lambda x: x.f, reverse=False)
                # print(open)
        return False



def main():
    initial_state = Board([1, 2, 3, 8, 0, 4, 7, 6, 5])
    goal_state = Board([2, 8, 1, 0, 4, 3, 7, 6, 5])
    n = Node(initial_state, goal_state)
    search = Astar(n, goal_state)
    print(search.search())



if __name__ == '__main__':
    main()
