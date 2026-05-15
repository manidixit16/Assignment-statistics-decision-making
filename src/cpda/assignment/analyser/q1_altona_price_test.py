"""
Q1 — One-Sample T-Test: Altona Property Price
=============================================
Tests whether the typical Altona property price has increased above $800,000.

H0 : mu = $800,000  (price has not changed)
H1 : mu > $800,000  (price has increased — one-tailed right)
alpha = 0.05
"""

import pandas as pd
from scipy.stats import ttest_1samp
from config import ALTONA_CLAIMED_MEDIAN, ALPHA


def altona_price_test(df: pd.DataFrame) -> dict:
    """One-sample t-test on Altona suburb prices."""
    suburb_data = df[df["Suburb"] == "Altona"]["Price"].dropna()

    t_stat, p_two = ttest_1samp(suburb_data, popmean=ALTONA_CLAIMED_MEDIAN)
    p_one = p_two / 2   # one-tailed right

    reject = (p_one < ALPHA) and (t_stat > 0)

    result = {
        "suburb"       : "Altona",
        "n"            : len(suburb_data),
        "mean"         : suburb_data.mean(),
        "median"       : suburb_data.median(),
        "std"          : suburb_data.std(),
        "claimed_mean" : ALTONA_CLAIMED_MEDIAN,
        "t_stat"       : t_stat,
        "p_two"        : p_two,
        "p_one"        : p_one,
        "reject_h0"    : reject,
    }

    _print_result(result)
    return result


def _print_result(r: dict) -> None:
    print(f"\n  === Q1: Altona One-Sample T-Test ===")
    print(f"  n={r['n']},  mean=${r['mean']:,.0f},  std=${r['std']:,.0f}")
    print(f"  H0: mu = ${r['claimed_mean']:,}  |  H1: mu > ${r['claimed_mean']:,}")
    print(f"  T-statistic : {r['t_stat']:.4f}")
    print(f"  One-tailed p: {r['p_one']:.4f}")
    decision = "REJECT H0" if r["reject_h0"] else "FAIL TO REJECT H0"
    print(f"  Decision    : {decision}")
    if r["reject_h0"]:
        print(f"  Conclusion  : Altona prices have increased above $800,000.")
    else:
        print(f"  Conclusion  : Insufficient evidence of price increase. $800,000 remains plausible.")
