import csv
from _csv import writer

columns = ['No','Initial state', 'A* time', 'A* nodes','A* path_length', 'IDA* time', 'IDA* nodes']

def create_new_csv_file(file_name):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(columns)

class ResultFile:
    def __init__(self, file_name='result.csv'):
        self.file_name=file_name
        self.no = 0
        create_new_csv_file(file_name)


    def add_result(self, initial_state,time,num_of_nodes, path_length):
        self.no+=1
        with open(self.file_name, 'a+', newline='') as write_obj:
            # Create a writer object from csv module
            csv_writer = writer(write_obj)
            # Add contents of list as last row in the csv file
            a = ''.join([str(elem) for elem in initial_state]).replace(']','').replace('[', '').replace(',', '').replace(' ', '')
            csv_writer.writerow([self.no, '['+a+']',time,num_of_nodes, path_length])


def main():
    f = ResultFile()
    # f.add_result()
    # f.add_result()
    # f.add_result()
    # f.add_result()
    s = '1 2 3 4 5 6 7 8 0'
    f.add_result(s)
    # ''.join(s).replace(']','').replace('[', '').replace(',', '').replace(' ', '').replace("", " ")[1: -1]
    print(s)


if __name__ == '__main__':
    main()