"""
Q2 — Two-Sample T-Test: Summer vs Winter Prices (2016)
======================================================
Tests whether property prices differ significantly between seasons in 2016.

Winter months : October – March  (10, 11, 12, 1, 2, 3)
Summer months : April – September (4, 5, 6, 7, 8, 9)

H0 : mu_winter = mu_summer   (no seasonal price difference)
H1 : mu_winter != mu_summer  (significant difference — two-tailed)
alpha = 0.05
"""

import pandas as pd
from scipy.stats import ttest_ind
from config import ALPHA, WINTER_MONTHS, SUMMER_MONTHS


def seasonal_price_test(df: pd.DataFrame) -> dict:
    """Welch's two-sample t-test on 2016 winter vs summer prices."""
    df_2016 = df[df["Year"] == 2016]

    winter = df_2016[df_2016["Month"].isin(WINTER_MONTHS)]["Price"].dropna()
    summer = df_2016[df_2016["Month"].isin(SUMMER_MONTHS)]["Price"].dropna()

    t_stat, p_val = ttest_ind(winter, summer, equal_var=False)

    result = {
        "year"          : 2016,
        "winter_n"      : len(winter),
        "winter_mean"   : winter.mean(),
        "summer_n"      : len(summer),
        "summer_mean"   : summer.mean(),
        "t_stat"        : t_stat,
        "p_value"       : p_val,
        "reject_h0"     : p_val < ALPHA,
    }

    _print_result(result)
    return result


def _print_result(r: dict) -> None:
    print(f"\n  === Q2: Seasonal Price Test (2016) ===")
    print(f"  Winter n={r['winter_n']:,},  mean=${r['winter_mean']:,.0f}")
    print(f"  Summer n={r['summer_n']:,},  mean=${r['summer_mean']:,.0f}")
    print(f"  T-statistic : {r['t_stat']:.4f}")
    print(f"  P-value     : {r['p_value']:.4f}")
    decision = "REJECT H0" if r["reject_h0"] else "FAIL TO REJECT H0"
    print(f"  Decision    : {decision}")
    if r["reject_h0"]:
        higher = "Winter" if r["winter_mean"] > r["summer_mean"] else "Summer"
        print(f"  Conclusion  : Significant seasonal difference. {higher} prices are higher.")
    else:
        print(f"  Conclusion  : No significant seasonal price difference in 2016.")
