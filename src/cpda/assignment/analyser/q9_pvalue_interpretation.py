"""
Q9 — p-Value Interpretation: Decision Making
============================================
Interprets a given p-value (0.032) in the context of a
hypothesis test comparing prices across two suburbs.

This module is conceptual (no data required) and prints
a structured business-oriented interpretation.
"""


def pvalue_interpretation(p_value: float = 0.032, alpha: float = 0.05) -> dict:
    """Interpret a p-value in plain business language."""
    reject = p_value < alpha

    result = {
        "p_value" : p_value,
        "alpha"   : alpha,
        "reject"  : reject,
    }

    _print_result(result)
    return result


def _print_result(r: dict) -> None:
    print(f"\n  === Q9: p-Value Interpretation ===")
    print(f"  p = {r['p_value']}  |  alpha = {r['alpha']}")
    print(f"\n  1. What does p = {r['p_value']} indicate?")
    print(f"     There is only a {r['p_value']*100:.1f}% probability of observing this")
    print(f"     price difference (or greater) if H0 were true.")
    print(f"     The result is unlikely to be due to random chance alone.")

    print(f"\n  2. Reject H0 at alpha = {r['alpha']}?")
    if r["reject"]:
        print(f"     YES — p = {r['p_value']} < {r['alpha']}. Statistically significant.")
        print(f"     We REJECT H0: the two suburbs do NOT have the same mean price.")
    else:
        print(f"     NO — p = {r['p_value']} >= {r['alpha']}. Not significant.")

    print(f"\n  3. Business stakeholder interpretation:")
    print(f"     Strong evidence the two suburbs have distinct price distributions.")
    print(f"     -> Use suburb-specific pricing models, not a market-wide average.")
    print(f"     -> Caution: statistical significance != practical significance.")
    print(f"        Also assess the actual price gap (effect size) before decisions.")
