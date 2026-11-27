from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"


def load_penguins() -> pd.DataFrame:
    """Ham penguen verisini okur."""
    path = RAW_DIR / "penguins.csv"
    if not path.exists():
        raise FileNotFoundError(
            f"{path} bulunamadı."
        )
    return pd.read_csv(path)