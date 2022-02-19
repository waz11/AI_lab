import time
from Astar import Astar
from PuzzleGenerator import PuzzleGenerator
from ResultFile import ResultFile


def main():
    file = ResultFile()
    generator = PuzzleGenerator()
    for i in range(10):
        # initial_state = generator.generate()
        initial_state = [[1,2,3],[4,5,6],[7,0,8]]
        # A* Algorithm:
        start = time.time()
        num_of_nodes, path_length = Astar(initial_state).search()
        end = time.time()
        f_time = end - start

        # IDA* Algorithm:

        file.add_result(initial_state,f_time,num_of_nodes,path_length)


if __name__ == '__main__':
    main()