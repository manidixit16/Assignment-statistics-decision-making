"""
Q10 — Hypothesis Validation: Bathroom Premium (Policy Decision)
===============================================================
A housing policy group believes properties with MORE than 2 bathrooms
command a premium price. Validates this claim statistically.

Test identified : Welch's independent two-sample t-test (one-tailed right)
  - Two independent groups: >2 bath vs <=2 bath
  - Continuous outcome (Price)
  - Unequal sample sizes -> Welch's handles unequal variances
  - Directional claim -> one-tailed right

H0 : mu_(>2 bath) <= mu_(<=2 bath)  (no bathroom premium)
H1 : mu_(>2 bath)  > mu_(<=2 bath)  (bathroom premium exists)
alpha = 0.05
"""

import pandas as pd
from scipy.stats import ttest_ind
from config import ALPHA


def bathroom_premium_test(df: pd.DataFrame) -> dict:
    """Welch's one-tailed t-test: >2 bathrooms vs <=2 bathrooms."""
    bath_df     = df[["Price", "Bathroom"]].dropna()
    more_2      = bath_df[bath_df["Bathroom"] > 2]["Price"]
    two_or_less = bath_df[bath_df["Bathroom"] <= 2]["Price"]

    t_stat, p_two = ttest_ind(more_2, two_or_less, equal_var=False)
    p_one = p_two / 2   # one-tailed right

    result = {
        "more_2_n"        : len(more_2),
        "more_2_mean"     : more_2.mean(),
        "two_or_less_n"   : len(two_or_less),
        "two_or_less_mean": two_or_less.mean(),
        "premium"         : more_2.mean() - two_or_less.mean(),
        "t_stat"          : t_stat,
        "p_two"           : p_two,
        "p_one"           : p_one,
        "reject_h0"       : (p_one < ALPHA) and (t_stat > 0),
    }

    _print_result(result)
    return result


def _print_result(r: dict) -> None:
    print(f"\n  === Q10: Bathroom Premium Hypothesis Test ===")
    print(f"  Test identified : Welch's two-sample t-test (one-tailed right)")
    print(f"  H0 : mu_(>2 bath) <= mu_(<=2 bath)  [no premium]")
    print(f"  H1 : mu_(>2 bath)  > mu_(<=2 bath)  [premium exists]")
    print(f"\n  >2 bath  : n={r['more_2_n']:,},  mean=${r['more_2_mean']:,.0f}")
    print(f"  <=2 bath : n={r['two_or_less_n']:,},  mean=${r['two_or_less_mean']:,.0f}")
    print(f"  Premium  : ${r['premium']:,.0f}")
    print(f"\n  P-value (one-tailed) : {r['p_one']:.2e}")
    decision = "REJECT H0" if r["reject_h0"] else "FAIL TO REJECT H0"
    print(f"  Decision             : {decision}")
    if r["reject_h0"]:
        print(f"\n  Recommendation to policymakers:")
        print(f"    -> Data validates the premium claim (${r['premium']:,.0f} uplift).")
        print(f"    -> Bathroom count (>2 vs <=2) is a legitimate policy tier boundary.")
        print(f"    -> Apply higher stamp duty / tax brackets for >2 bathroom properties.")
        print(f"    -> Target affordability grants at <=2 bathroom properties.")
