"""
Q3 — Binomial Probability: No Car Parking (Abbotsford)
======================================================
Calculates the probability that exactly 3 out of 10 Abbotsford
properties sold will NOT have a car parking space.

Uses the Binomial distribution: P(X=k) = C(n,k) * p^k * (1-p)^(n-k)
  n = 10  (properties sold)
  k = 3   (properties without car parking)
  p = P(no car) estimated from Abbotsford data
"""

import pandas as pd
from scipy.stats import binom


def binomial_car_parking(df: pd.DataFrame) -> dict:
    """Binomial probability for no-car-parking outcome in Abbotsford."""
    suburb = df[df["Suburb"] == "Abbotsford"]
    car_data = suburb["Car"].dropna()

    p_no_car = (car_data == 0).sum() / len(car_data)

    n, k = 10, 3
    probability = binom.pmf(k, n, p_no_car)

    result = {
        "suburb"       : "Abbotsford",
        "n_sample"     : len(car_data),
        "no_car_count" : int((car_data == 0).sum()),
        "p_no_car"     : p_no_car,
        "binom_n"      : n,
        "binom_k"      : k,
        "probability"  : round(probability, 3),
    }

    _print_result(result)
    return result


def _print_result(r: dict) -> None:
    print(f"\n  === Q3: Binomial — No Car Parking ===")
    print(f"  P(no car) = {r['no_car_count']}/{r['n_sample']} = {r['p_no_car']:.4f}")
    print(f"  P(exactly {r['binom_k']} of {r['binom_n']} have no car) = {r['probability']:.3f}")
