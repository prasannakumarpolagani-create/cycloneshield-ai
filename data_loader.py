from pathlib import Path
import pandas as pd


# Get the folder containing this Python file
BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"


def load_infrastructure():

    file_path = DATA_DIR / "infrastructure.csv"

    if not file_path.exists():
        raise FileNotFoundError(
            f"Infrastructure data file not found: {file_path}"
        )

    return pd.read_csv(file_path)


def load_cyclone():

    file_path = DATA_DIR / "cyclone_data.csv"

    if not file_path.exists():
        raise FileNotFoundError(
            f"Cyclone data file not found: {file_path}"
        )

    return pd.read_csv(file_path)