"""
Dataset Loader
==============
Loads and lightly parses the raw property.csv dataset.
Returns a clean DataFrame ready for analysis.
"""

import pandas as pd
import os
from config import DATA_PATH, DATASET_FILE


def load_data() -> pd.DataFrame:
    """Load property.csv and parse dates / derived columns."""
    path = os.path.join(DATA_PATH, DATASET_FILE)
    df = pd.read_csv(path)

    # Parse sale date; extract Month and Year for seasonal analysis
    df["Date"]  = pd.to_datetime(df["Date"], dayfirst=True)
    df["Month"] = df["Date"].dt.month
    df["Year"]  = df["Date"].dt.year

    print(f"  Loaded {len(df):,} records | {df.shape[1]} columns")
    return df
