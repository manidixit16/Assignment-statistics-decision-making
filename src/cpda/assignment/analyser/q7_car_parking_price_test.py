"""
Q7 — Independent Two-Sample T-Test: Car Parking Effect on Price
===============================================================
Tests whether properties WITH car parking sell at higher prices
than those WITHOUT across the full dataset.

Test chosen : Welch's independent t-test (one-tailed right)
  - Two independent groups (with / without car)
  - Continuous outcome (Price)
  - Unequal sample sizes -> Welch's handles unequal variances

H0 : mu_with_car <= mu_without_car  (no price premium)
H1 : mu_with_car  > mu_without_car  (car parking commands higher price)
alpha = 0.05
"""

import pandas as pd
from scipy.stats import ttest_ind
from config import ALPHA


def car_parking_price_test(df: pd.DataFrame) -> dict:
    """Welch's one-tailed t-test: with car vs without car prices."""
    car_df      = df[["Price", "Car"]].dropna()
    with_car    = car_df[car_df["Car"] > 0]["Price"]
    without_car = car_df[car_df["Car"] == 0]["Price"]

    t_stat, p_two = ttest_ind(with_car, without_car, equal_var=False)
    p_one = p_two / 2   # one-tailed

    result = {
        "with_car_n"     : len(with_car),
        "with_car_mean"  : with_car.mean(),
        "without_car_n"  : len(without_car),
        "without_car_mean": without_car.mean(),
        "price_diff"     : with_car.mean() - without_car.mean(),
        "t_stat"         : t_stat,
        "p_two"          : p_two,
        "p_one"          : p_one,
        "reject_h0"      : (p_one < ALPHA) and (t_stat > 0),
    }

    _print_result(result)
    return result


def _print_result(r: dict) -> None:
    print(f"\n  === Q7: Car Parking Two-Sample T-Test ===")
    print(f"  Test chosen  : Welch's independent t-test (one-tailed right)")
    print(f"  WITH car     : n={r['with_car_n']:,},  mean=${r['with_car_mean']:,.0f}")
    print(f"  WITHOUT car  : n={r['without_car_n']:,},  mean=${r['without_car_mean']:,.0f}")
    print(f"  Diff         : ${r['price_diff']:,.0f}")
    print(f"  T-statistic  : {r['t_stat']:.4f}")
    print(f"  One-tailed p : {r['p_one']:.4f}")
    decision = "REJECT H0" if r["reject_h0"] else "FAIL TO REJECT H0"
    print(f"  Decision     : {decision}")
    if not r["reject_h0"]:
        print(f"  P-value interpretation: p={r['p_one']:.4f} > 0.05")
        print(f"  Car parking alone is NOT a statistically significant price driver.")
        print(f"  Business implication: developers should not assume a blanket price")
        print(f"  premium; suburb and property type dominate pricing.")
