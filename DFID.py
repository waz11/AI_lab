import collections
import time

from State import State


class DFID:
    def __init__(self, initial_state):
        self.initial_state_node = State(initial_state)

    def search(self,threshold=0):
        num_of_nodes = 0
        closed = set()
        open_queue = collections.deque([])
        iter_threshold = threshold
        open_queue.appendleft(self.initial_state_node)
        while(len(open_queue)>0):
            num_of_nodes += 1
            print(num_of_nodes)
            # open_queue = collections.deque(sorted(list(open_queue), key=lambda node: (node.f, node.h)))
            curr = open_queue.popleft()
            closed.add(curr.id)
            if curr.h == 0:
                print("here")
                return num_of_nodes-1, curr.g
            elif iter_threshold>0:
                iter_threshold -= 1
                for neighbor in curr.get_neighbors():
                    if neighbor.id in closed:
                        continue
                    else:
                        open_queue.append(neighbor)
            elif iter_threshold == 0:
                return self.search(threshold+1)
        return False



def main():
    search = DFID([[1,2,3], [4,5,6], [7,0,8]])
    s = time.time()
    nodes = search.search()
    e = time.time()
    print(nodes, e-s)


if __name__ == '__main__':
    main()

