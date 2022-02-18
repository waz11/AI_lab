from Astar import Astar
from board import Board
from itertools import permutations
from node import Node


def main():
    # initial = [1,2,3,8,0,4,7,6,5]
    initial = [1, 2, 3, 8, 0, 4, 7, 5, 6]
    goal_state = Board([2, 8, 1, 0, 4, 3, 7, 6, 5])

    initial_state = Board(initial)
    n = Node(initial_state, goal_state)
    searcher = Astar(n, goal_state)
    print(searcher.search())

    i=0
    # for permutation in list(permutations(initial))[:2]:
    #     i+=1
    #     print(i)
    #     permutation = list(permutation)
    #     print(permutation)
    #     initial_state = Board(permutation)
    #     n = Node(initial_state, goal_state)
    #     searcher = Astar(n, goal_state)
    #     print(searcher.search())
    #     print("ron")



if __name__ == '__main__':
    main()