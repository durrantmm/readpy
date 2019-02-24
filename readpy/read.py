import pandas as pd
from dplython import DplyFrame, head
from itertools import cycle


def read_delim(f, delim, col_names = True):

    assert isinstance(f, str)
    assert isinstance(delim, str)
    assert isinstance(col_names, bool)

    if col_names == True:
        col_names = 0
    else:
        col_names = None

    df = DplyFrame(pd.read_csv(filepath_or_buffer=f, header=col_names, sep=delim))

    if col_names == None:
        df.columns = [''.join(map(str, list(n))) for n in zip(cycle(['X']), range(1, df.shape[1]+1))]

    return df


def read_tsv(f, col_names = True):

    return read_delim(f, '\t', col_names)


def read_csv(f, col_names = True):

    return read_delim(f, ',', col_names)