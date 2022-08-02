from pre_process.csv_reader_base import CsvReaderBase
import pandas as pd
import os
from glob import glob
from rich import print
from utils.my_type import *
from utils.utils import make_key_alias_from_dir
from typing import List


def main() -> None:
    return


def make_df_d(filepath_d: FileDict) -> DfDict:
    return DfDict({key: pd.read_csv(val) for key, val in filepath_d.items()})


if __name__ == "__main__":
    inputs_dir = DirName("inputs")
    filepath_d = make_key_alias_from_dir(inputs_dir=inputs_dir)
    df_d = make_df_d(filepath_d=filepath_d)
    main()
