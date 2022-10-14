import os
import sys
import pandas as pd


class Combine_CSV:

    #Method to combine CSV files
    def csv_combine(self, argv: list):

        combined_csv = []

        if self.check_input(argv):

            input_files = argv[1:]

            for file in input_files:

                #to handle very large files
                for chunk in pd.read_csv(file, chunksize=1000):

                    #get the base name of the specified path
                    filename = os.path.basename(file)

                    #add "filename" as additional column
                    chunk['filename'] = filename
                    combined_csv.append(chunk)

            add_header = True

            #output to stdout
            for chunk in combined_csv:
                print(chunk.to_csv(index=False, header=add_header, lineterminator='\n', chunksize=1000), end='')
                add_header = False
        else:
            return

    #Method to check if arguments are valid 
    @staticmethod
    def check_input(argv):

        if len(argv) <= 1:
            print("No CSV files provided as arguments")
            return False

        input_files = argv[1:]

        for file_path in input_files:
            if not os.path.exists(file_path):
                print("File not found" + file_path)
                return False

            if os.stat(file_path).st_size == 0:
                print("File is empty" + file_path)
                return False

        return True

def main():
    combiner = Combine_CSV()
    combiner.csv_combine(sys.argv)

if __name__ == '__main__':
    main()
