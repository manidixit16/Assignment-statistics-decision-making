"""
Data Sanitizer
==============
Cleans the raw property DataFrame:
  - Reports missing values
  - Drops records with no Price (required for all hypothesis tests)
  - Logs a summary of what was removed
"""

import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Drop rows where Price is null; report other nulls."""
    original = len(df)

    print(f"\n  Missing value summary:")
    nulls = df.isnull().sum()
    for col, n in nulls[nulls > 0].items():
        pct = n / len(df) * 100
        print(f"    {col:<20s}: {n:,} ({pct:.1f}%)")

    df = df.dropna(subset=["Price"])
    removed = original - len(df)
    print(f"\n  Removed {removed} rows with missing Price.")
    print(f"  Clean dataset: {len(df):,} records")
    return df
