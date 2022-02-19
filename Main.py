import time
from Astar import Astar
from PuzzleGenerator import PuzzleGenerator
from ResultFile import ResultFile


def main():
    file = ResultFile()
    generator = PuzzleGenerator()
    for i in range(1):
        # initial_state = generator.generate()
        initial_state = [[8, 2, 3], [1, 0, 5],[ 4, 6, 7]]
        # A* Algorithm:
        start = time.time()
        num_of_nodes, path_length = Astar(initial_state).search()
        end = time.time()
        f_time = end - start
        print(num_of_nodes, path_length, f_time)

        # IDA* Algorithm:

        file.add_result(initial_state,f_time,num_of_nodes,path_length)


if __name__ == '__main__':
    main()