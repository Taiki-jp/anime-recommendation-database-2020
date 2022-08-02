import os
from typing import Callable, List
from utils.my_type import *

# from utils.py_color import PyColor
import pandas as pd


class CsvReaderBase:
    def __init__(
        self,
        file_name: FileName,
        verbose: int = 0,
        inputs_dir: DirName = "inputs",
        columns: List[str] = [],
        names: List[str] = [],
    ):
        self.inputs_dir = inputs_dir
        self.file_name = file_name
        self.verbose = verbose
        self.columns = columns
        self.names = names

    # 相対パスを取得
    def get_full_path(self) -> RelPath:
        return RelPath(os.path.join(self.inputs_dir, self.file_name))

    # CSVファイル読み込み
    def read_csv(self) -> Callable[[], pd.DataFrame]:
        file_path = self.get_full_path()

        def _read() -> pd.DataFrame:
            if self.verbose == 0:
                print(
                    # PyColor.GREEN,
                    f"*** READ {file_path} ***",
                    # PyColor.END,
                )
            elif self.verbose == 1:
                pass
            else:
                pass

            # 引数によって呼び方を変更
            if bool(self.names and self.columns):
                df = pd.read_csv(
                    file_path, usecols=self.columns, names=self.names, header=0
                )
            elif bool(self.columns):
                df = pd.read_csv(file_path, usecols=self.columns)
            elif bool(self.names):
                df = pd.read_csv(file_path, usecols=self.columns)
            else:
                df = pd.read_csv(file_path)
            return df

        return _read()


if __name__ == "__main__":

    csv_reader = CsvReaderBase(file_name="anime_with_synopsis.csv", verbose=0)
    AWS_df = csv_reader.read_csv()
    print(AWS_df.head())
