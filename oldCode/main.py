from Astar import Astar
from board import Board
from itertools import permutations
from node import Node


def main():
    initial = [1,2,3,8,0,4,7,6,5]
    goal_state = Board([2, 8, 1, 0, 4, 3, 7, 6, 5])
    permu = list(permutations(initial))

    initial_state = Board(initial)
    n = Node(initial_state, goal_state)
    searcher = Astar(n, goal_state)
    print(searcher.search())

    i=0
    for p in permu:
        i+=1
        p = list(p)
        print(i, p)

        initial_state = Board(p)
        n = Node(initial_state, goal_state)
        searcher = Astar(n, goal_state)
        print(searcher.search())
        print("ron")



if __name__ == '__main__':
    main()