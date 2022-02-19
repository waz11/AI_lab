import collections
import math
import time

from State import State


class IDA:
    def __init__(self, initial_state):
        self.initial_state_node = State(initial_state)

    def search(self,min_f=math.inf,threshold=0):
        num_of_nodes = 0
        closed = set()
        open_queue = collections.deque([])
        iter_threshold = threshold
        open_queue.appendleft(self.initial_state_node)
        while (len(open_queue) > 0):
            num_of_nodes += 1
            print(num_of_nodes)
            # open_queue = collections.deque(sorted(list(open_queue), key=lambda node: (node.f, node.h)))
            curr = open_queue.popleft()
            closed.add(curr.id)
            if curr.h == 0:
                return num_of_nodes - 1, curr.g
            elif iter_threshold > 0:
                iter_threshold -= 1
                min_f = math.inf
                for neighbor in curr.get_neighbors():
                    if neighbor.f <= min_f:
                        open_queue.append(neighbor)
                    else:
                        min_f = min(neighbor.f, min_f)
            elif iter_threshold == 0:
                return self.search(math.inf, min_f)
        return False



def main():
    search = IDA([[1,2,3], [4,5,6], [0,7,8]])
    s = time.time()
    nodes = search.search()
    e = time.time()
    print(nodes, e-s)


if __name__ == '__main__':
    main()

