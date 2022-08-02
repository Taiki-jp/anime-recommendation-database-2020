import os
from glob import glob
from utils.my_type import *


def make_key_alias_from_dir(inputs_dir: DirName) -> FileDict:
    filepath_d: FileDict = {
        FileAlias(filename.split(".")[0].split("\\")[1]): RelPath(
            os.path.join(filename)
        )
        for filename in glob(os.path.join(inputs_dir, "*"))
        if filename.split(".")[1] == "csv"
    }
    return filepath_d
