import csv
from _csv import writer
import os

columns = ['No','Initial state', 'A* time', 'A* nodes','A* path_length', 'IDA* time', 'IDA* nodes','IDA* path_length']

def create_new_csv_file(file_name):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(columns)

class ResultFile:
    def __init__(self, file_name='results.csv'):
        self.file_name=file_name
        self.no = 0
        if not os.path.isfile(file_name):
            create_new_csv_file(file_name)

    def add_result(self, initial_state, time1, num_of_nodes1, path_length1, time2, num_of_nodes2, path_length2):
        self.no+=1
        with open(self.file_name, 'a+', newline='') as write_obj:
            # Create a writer object from csv module
            csv_writer = writer(write_obj)
            # Add contents of list as last row in the csv file
            a = ''.join([str(elem) for elem in initial_state]).replace(']','').replace('[', '').replace(',', '').replace(' ', '')
            csv_writer.writerow([self.no, '[' + a +']', time1, num_of_nodes1, path_length1, time2, num_of_nodes2, path_length2])


def main():
    f = ResultFile()
    # f.add_result()
    # f.add_result()
    # f.add_result()
    # f.add_result()
    # s = '1 2 3 4 5 6 7 8 0'
    # f.add_result(s)
    # ''.join(s).replace(']','').replace('[', '').replace(',', '').replace(' ', '').replace("", " ")[1: -1]
    # print(s)


if __name__ == '__main__':
    main()