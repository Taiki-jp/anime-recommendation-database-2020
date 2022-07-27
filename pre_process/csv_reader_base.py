import os
from typing import Callable, List

# from utils.py_color import PyColor
import pandas as pd


class CsvReaderBase:
    def __init__(
        self,
        file_name: str,
        verbose: int = 0,
        inputs_dir: str = "inputs",
        columns: List[str] = [],
        names: List[str] = [],
    ):
        self.inputs_dir: str = inputs_dir
        self.file_name: str = file_name
        self.verbose: int = verbose
        self.columns: str = columns
        self.names: List[str] = names

    # 絶対パスを取得
    def get_full_path(self) -> str:
        return os.path.join(self.inputs_dir, self.file_name)
    
    # 複数ファイルが渡されたときに対応（複数ファイルの階層は同じ）
    def get_mul_path(self) -> List[str]:
        

    # CSVファイル読み込み
    def read_csv(self) -> Callable:
        file_path = self.get_full_path()

        def _read() -> pd.DataFrame:
            if self.verbose == 0:
                print(
                    # PyColor.GREEN,
                    f"*** read {file_path} ***",
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
    csv_reader.read_csv()
