"""
Q6 — One-Sample T-Test: Richmond Industry Pricing Claim
=======================================================
A real estate firm claims the average Richmond price is $1,000,000.
Tests whether the actual mean is significantly different.

H0 : mu = $1,000,000  (firm's claim is correct)
H1 : mu != $1,000,000  (two-tailed — actual mean differs)
alpha = 0.05

Required outputs (per assignment):
  - Null and alternative hypotheses
  - Test statistic
  - p-value
  - Final business conclusion
"""

import pandas as pd
from scipy.stats import ttest_1samp
from config import RICHMOND_CLAIMED_MEAN, ALPHA


def richmond_price_test(df: pd.DataFrame) -> dict:
    """One-sample two-tailed t-test on Richmond suburb prices."""
    suburb_data = df[df["Suburb"] == "Richmond"]["Price"].dropna()

    t_stat, p_val = ttest_1samp(suburb_data, popmean=RICHMOND_CLAIMED_MEAN)

    result = {
        "suburb"        : "Richmond",
        "n"             : len(suburb_data),
        "sample_mean"   : suburb_data.mean(),
        "sample_median" : suburb_data.median(),
        "sample_std"    : suburb_data.std(),
        "claimed_mean"  : RICHMOND_CLAIMED_MEAN,
        "t_stat"        : t_stat,
        "p_value"       : p_val,
        "reject_h0"     : p_val < ALPHA,
    }

    _print_result(result)
    return result


def _print_result(r: dict) -> None:
    print(f"\n  === Q6: Richmond One-Sample T-Test ===")
    print(f"  H0 : mu = ${r['claimed_mean']:,}  (firm's claim)")
    print(f"  H1 : mu != ${r['claimed_mean']:,}  (two-tailed)")
    print(f"  n={r['n']},  sample mean=${r['sample_mean']:,.0f},  std=${r['sample_std']:,.0f}")
    print(f"  Test statistic (t) : {r['t_stat']:.4f}")
    print(f"  P-value            : {r['p_value']:.4f}")
    decision = "REJECT H0" if r["reject_h0"] else "FAIL TO REJECT H0"
    print(f"  Decision           : {decision}")
    direction = "above" if r["sample_mean"] > r["claimed_mean"] else "below"
    if r["reject_h0"]:
        print(f"  Business conclusion: Mean (${r['sample_mean']:,.0f}) is significantly {direction}")
        print(f"    the claimed $1,000,000. The firm's pricing estimate is NOT supported.")
    else:
        print(f"  Business conclusion: Data is consistent with the $1,000,000 claim.")
