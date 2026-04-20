from pathlib import Path

import pandas as pd

DATA_FOLDER_PATH = Path(__file__).parent.parent / "data"


def function3() -> pd.DataFrame:
    data_path = DATA_FOLDER_PATH / "sample.json"
    return pd.read_json(data_path)
