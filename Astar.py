import collections
import time

from Node import Node


class Astar:
    def __init__(self, initial_state):
        self.initial_state_node = Node(initial_state)

    def search(self):
        num_of_nodes = 0
        closed = set()
        open_queue = collections.deque([])

        open_queue.appendleft(self.initial_state_node)
        while(len(open_queue)>0):
            num_of_nodes+=1
            open_queue = collections.deque(sorted(list(open_queue), key=lambda node: (node.f, node.h)))
            curr:Node = open_queue.popleft()
            closed.add(curr.id)
            if curr.h == 0:
                return num_of_nodes-1
            else:
                for neighbor in curr.get_neighbors():
                    if neighbor.id in closed:
                        continue
                    else:
                        open_queue.appendleft(neighbor)
        return False



def main():
    # search = Astar([[4, 2, 1], [6, 0, 3], [8, 5, 7]])
    # search = Astar([[1,2,3], [4,5,6], [7,0,8]])
    search = Astar([[1, 7, 4], [8, 5, 6], [0, 3, 2]])
    nodes = search.search()
    print(nodes)


if __name__ == '__main__':
    main()

