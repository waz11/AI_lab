import csv
from _csv import writer

columns = ['No','Initial state', 'A* time', 'A* nodes', 'IDA* time', 'IDA* nodes']

def create_new_csv_file(file_name):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(columns)

class Result_file:
    def __init__(self, file_name='result.csv'):
        self.file_name=file_name
        self.no = 0
        create_new_csv_file(file_name)


    def add_result(self):
        self.no+=1
        with open(self.file_name, 'a+', newline='') as write_obj:
            # Create a writer object from csv module
            csv_writer = writer(write_obj)
            # Add contents of list as last row in the csv file
            csv_writer.writerow([self.no])


def main():
    f = Result_file()
    f.add_result()
    f.add_result()
    f.add_result()
    f.add_result()


if __name__ == '__main__':
    main()