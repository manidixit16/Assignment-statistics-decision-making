"""
Q4 & Q5 — Empirical Probabilities: Abbotsford Rooms & Bathrooms
===============================================================
Q4: P(3 rooms)     in Abbotsford
Q5: P(2 bathrooms) in Abbotsford

Both are simple relative-frequency (empirical) probability calculations.
"""

import pandas as pd


def abbotsford_room_probability(df: pd.DataFrame) -> dict:
    """Q4 — P(3 rooms) in Abbotsford."""
    suburb = df[df["Suburb"] == "Abbotsford"]
    rooms  = suburb["Rooms"]
    total  = len(rooms)
    count  = (rooms == 3).sum()
    prob   = round(count / total, 3)

    result = {
        "suburb"        : "Abbotsford",
        "attribute"     : "Rooms",
        "target_value"  : 3,
        "total"         : total,
        "count"         : count,
        "probability"   : prob,
    }
    print(f"\n  === Q4: P(3 rooms | Abbotsford) ===")
    print(f"  {count}/{total} = {prob:.3f}")
    return result


def abbotsford_bathroom_probability(df: pd.DataFrame) -> dict:
    """Q5 — P(2 bathrooms) in Abbotsford."""
    suburb = df[df["Suburb"] == "Abbotsford"]
    bath   = suburb["Bathroom"].dropna()
    total  = len(bath)
    count  = (bath == 2).sum()
    prob   = round(count / total, 3)

    result = {
        "suburb"        : "Abbotsford",
        "attribute"     : "Bathroom",
        "target_value"  : 2,
        "total"         : total,
        "count"         : count,
        "probability"   : prob,
    }
    print(f"\n  === Q5: P(2 bathrooms | Abbotsford) ===")
    print(f"  {count}/{total} = {prob:.3f}")
    return result
