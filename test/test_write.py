import unittest
import os
import pandas as pd
from itertools import cycle
import filecmp

data_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')

from readpy import write_tsv, write_csv, write_delim


class TestReadTsv(unittest.TestCase):

    def setUp(self):

        self.diamonds_csv = os.path.join(data_dir, 'diamonds.csv')
        self.diamonds_tsv = os.path.join(data_dir, 'diamonds.tsv')

        self.diamonds_csv_noheader = os.path.join(data_dir, 'diamonds.noheader.csv')
        self.diamonds_tsv_noheader= os.path.join(data_dir, 'diamonds.noheader.tsv')

        self.diamonds_df = pd.read_csv(self.diamonds_csv)

        self.noheader = [''.join(map(str, list(n))) for n in zip(cycle(['X']), range(1, self.diamonds_df.shape[1] + 1))]

    def tearDown(self):

        if os.path.isfile(self.diamonds_tsv+'.tmp'):
            os.remove(self.diamonds_tsv+'.tmp')

        if os.path.isfile(self.diamonds_tsv_noheader + '.tmp'):
            os.remove(self.diamonds_tsv_noheader + '.tmp')

        if os.path.isfile(self.diamonds_csv + '.tmp'):
            os.remove(self.diamonds_csv + '.tmp')

        if os.path.isfile(self.diamonds_csv_noheader + '.tmp'):
            os.remove(self.diamonds_csv_noheader + '.tmp')


    def test_write_tsv(self):

        write_tsv(self.diamonds_df, self.diamonds_tsv+'.tmp')
        self.assertTrue(filecmp.cmp(self.diamonds_tsv, self.diamonds_tsv + '.tmp'))

        write_tsv(self.diamonds_df, self.diamonds_tsv_noheader + '.tmp', col_names=False)
        self.assertTrue(filecmp.cmp(self.diamonds_tsv_noheader, self.diamonds_tsv_noheader + '.tmp'))


    def test_write_csv(self):

        write_csv(self.diamonds_df, self.diamonds_csv + '.tmp')
        self.assertTrue(filecmp.cmp(self.diamonds_csv, self.diamonds_csv + '.tmp'))

        write_csv(self.diamonds_df, self.diamonds_csv_noheader + '.tmp', col_names=False)
        self.assertTrue(filecmp.cmp(self.diamonds_csv_noheader, self.diamonds_csv_noheader + '.tmp'))



if __name__ == '__main__':
    unittest.main()