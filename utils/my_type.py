from typing import NewType, Dict, List
import pandas as pd

# 絶対パス
AbsPath = NewType("AbsPath", str)
# 相対パス
RelPath = NewType("RelPath", str)
# ファイルパス
FilePath = NewType("FilePath", str)
# ファイル名
FileName = NewType("FileName", str)
# ディレクトリ名
DirName = NewType("DirName", str)
# ファイルのエイリアス（）
FileAlias = NewType("FileAlias", str)
# ファイルのエイリアスと相対パスの辞書
FileDict = NewType("FileDict", Dict[FileAlias, RelPath])
# エイリアスとデータフレームの辞書
DfDict = NewType("DfDict", Dict[FileAlias, List[pd.DataFrame]])
