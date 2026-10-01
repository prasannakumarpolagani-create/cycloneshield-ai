import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def load_cyclone_data():
    file_path = BASE_DIR / "cyclone_data.csv"

    if not file_path.exists():
        raise FileNotFoundError(
            f"Cyclone data file not found: {file_path}"
        )

    return pd.read_csv(file_path)


def load_infrastructure():
    file_path = BASE_DIR / "infrastructure.csv"

    if not file_path.exists():
        raise FileNotFoundError(
            f"Infrastructure data file not found: {file_path}"
        )

    return pd.read_csv(file_path)
