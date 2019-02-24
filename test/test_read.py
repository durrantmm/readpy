import unittest
import os
import pandas as pd
from itertools import cycle
from dplython import DplyFrame

data_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')

from readpy import read_tsv, read_csv, read_delim


class TestReadTsv(unittest.TestCase):

    def setUp(self):

        self.diamonds_csv = os.path.join(data_dir, 'diamonds.csv')
        self.diamonds_tsv = os.path.join(data_dir, 'diamonds.tsv')

        self.diamonds_csv_noheader = os.path.join(data_dir, 'diamonds.noheader.csv')
        self.diamonds_tsv_noheader  = os.path.join(data_dir, 'diamonds.noheader.tsv')

        self.diamonds_df = pd.read_csv(self.diamonds_csv)
        self.diamonds_df_noheader = pd.read_csv(self.diamonds_csv_noheader, header=None)

        self.noheader = [''.join(map(str, list(n))) for n in zip(cycle(['X']), range(1, self.diamonds_df.shape[1] + 1))]


    def test_read_tsv(self):

        diamonds_tsv_header = read_tsv(self.diamonds_tsv)
        diamonds_tsv_noheader = read_tsv(self.diamonds_tsv_noheader, col_names=False)


        for i in range(diamonds_tsv_header.shape[1]):

            self.assertEqual(list(diamonds_tsv_header.iloc[:, i]), list(self.diamonds_df.iloc[:, i]))


        for i in range(diamonds_tsv_header.shape[1]):

            self.assertEqual(list(diamonds_tsv_noheader.iloc[:, i]), list(self.diamonds_df_noheader.iloc[:, i]))

        self.assertEqual(self.noheader, list(diamonds_tsv_noheader.columns))


    def test_read_csv(self):

        diamonds_csv_header = read_csv(self.diamonds_csv)
        diamonds_csv_noheader = read_csv(self.diamonds_csv_noheader, col_names=False)

        for i in range(diamonds_csv_header.shape[1]):

            self.assertEqual(list(diamonds_csv_header.iloc[:, i]), list(self.diamonds_df.iloc[:, i]))


        for i in range(diamonds_csv_header.shape[1]):

            self.assertEqual(list(diamonds_csv_noheader.iloc[:, i]), list(self.diamonds_df_noheader.iloc[:, i]))


        self.assertEqual(self.noheader, list(diamonds_csv_noheader.columns))



if __name__ == '__main__':
    unittest.main()