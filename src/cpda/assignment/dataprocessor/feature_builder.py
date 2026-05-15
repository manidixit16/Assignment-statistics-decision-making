"""
Feature Builder
===============
Derives additional columns used across multiple analyses:
  - SEASON       : 'Winter' / 'Summer' (Southern Hemisphere)
  - HAS_CAR      : bool — property has at least one car space
  - BATH_TIER    : 'More than 2' / '2 or fewer'
"""

import pandas as pd
from config import WINTER_MONTHS


def create_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add derived feature columns to the master DataFrame."""

    # Seasonal label
    df["SEASON"] = df["Month"].apply(
        lambda m: "Winter" if m in WINTER_MONTHS else "Summer"
    )

    # Car parking flag
    df["HAS_CAR"] = df["Car"].apply(
        lambda x: "With car parking" if (pd.notna(x) and x > 0) else "No car parking"
    )

    # Bathroom tier
    df["BATH_TIER"] = df["Bathroom"].apply(
        lambda x: "More than 2" if (pd.notna(x) and x > 2) else "2 or fewer"
    )

    print(f"  Features created: SEASON, HAS_CAR, BATH_TIER")
    return df
