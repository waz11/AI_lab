import time
from Astar import Astar
from PuzzleGenerator import PuzzleGenerator
from ResultFile import ResultFile


def main():
    file = ResultFile()
    generator = PuzzleGenerator()
    for i in range(10):
        initial_state = generator.generate()

        # A* Algorithm:
        start = time.time()
        num_of_nodes = Astar(initial_state).search()
        end = time.time()
        f_time = end - start

        # IDA* Algorithm:

        file.add_result(initial_state,f_time,num_of_nodes)


if __name__ == '__main__':
    main()