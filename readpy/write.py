import pandas as pd
from dplython import DplyFrame, head
from itertools import cycle


def write_delim(x, path, delim, col_names = True):

    assert isinstance(x, DplyFrame) | isinstance(x, pd.DataFrame)
    assert isinstance(path, str)
    assert isinstance(delim, str)
    assert isinstance(col_names, bool)


    x.to_csv(path_or_buf=path, sep=delim, header=col_names, index=False)


def write_tsv(x, path, col_names = True):

    write_delim(x, path, '\t', col_names)


def write_csv(x, path, col_names = True):

    write_delim(x, path, ',', col_names)