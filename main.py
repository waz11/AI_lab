from Astar import Astar
from board import Board
from itertools import permutations
from node import Node


def main():
    initial = [1,2,3,8,0,4,7,6,5]
    goal_state = Board([2, 8, 1, 0, 4, 3, 7, 6, 5])
    for permutation in list(permutations(initial))[:2]:
        permutation = list(permutation)
        print(permutation)
        initial_state = Board(permutation)
        n = Node(initial_state, goal_state)
        search = Astar(n, goal_state)
        print(search.search())



if __name__ == '__main__':
    main()