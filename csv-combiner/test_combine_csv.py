import sys
import unittest
import pandas as pd
from combine_csv import Combine_CSV
from io import StringIO


class TestCombineCSV(unittest.TestCase):

    test_output_path = "./test_output.csv"
    csv_combiner_path = "./csv_combiner.py"

    #test output initialization
    backup = sys.stdout
    test_output = open(test_output_path, 'w+')
    combiner = Combine_CSV()


    def setUp(self):
        self.output = StringIO()
        sys.stdout = self.output
        self.test_output = open(self.test_output_path, 'w+')

    def tearDown(self):
        self.test_output.close()
        self.test_output = open(self.test_output_path, 'w+')
        sys.stdout = self.backup
        self.test_output.truncate(0)
        self.test_output.write(self.output.getvalue())
        self.test_output.close()

    #test to check if csv files are provided as arguments
    def test_no_csv_arguments(self):

        argv = [self.csv_combiner_path]
        self.combiner.csv_combine(argv)

        self.assertIn("No CSV files provided as arguments", self.output.getvalue())

    #test to check if csv file is empty
    def test_empty_csv_file(self):

        with open('empty.csv', 'w'): 
                pass 

        argv = [self.csv_combiner_path, "empty.csv"]
        self.combiner.csv_combine(argv)

        self.assertIn("File is empty", self.output.getvalue())

    #test to check if csv file exists
    def test_non_existing_csv_file(self):

        argv = [self.csv_combiner_path, "non_exist.csv"]
        self.combiner.csv_combine(argv)

        self.assertTrue("File not found" in self.output.getvalue())
