import math
import time

from Search.State import State


class IDA:
    def __init__(self, initial_state):
        self.initial_state_node = State(initial_state)
        self.num_of_nodes = 0

    def search(self):
        return self.aux(self.initial_state_node.f)

    def aux(self,threshold):
        num_of_nodes = 0
        stack = []
        stack.append(self.initial_state_node)
        min_f = math.inf
        # print(threshold)
        while(len(stack) > 0):
            num_of_nodes += 1
            curr = stack.pop()
            if curr.h == 0:
                return num_of_nodes - 1, curr.g
            for neighbor in curr.get_neighbors():
                if neighbor.f <= threshold:
                    stack.append(neighbor)
                else:
                    min_f = min(neighbor.f, min_f)
        return self.aux(min_f)


def main():
    # search = IDA([[8, 2, 3], [1, 0, 5],[ 4, 6, 7]])
    # search = IDA([[4,1,3], [7,2,5], [0,8,6]])
    search = IDA([[4,1,2], [7,5,3], [0,8,6]])
    s = time.time()
    nodes = search.search()
    e = time.time()
    print(nodes, e-s)


if __name__ == '__main__':
    main()

