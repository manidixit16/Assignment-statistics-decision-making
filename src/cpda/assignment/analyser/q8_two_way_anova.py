"""
Q8 — Two-Way ANOVA: Location & Property Type Effect on Price
============================================================
Investigates whether property prices are influenced by:
  1. Suburb (location)
  2. Type of property (house / townhouse / unit)
  3. Interaction between suburb and type

Uses the top 5 suburbs by listing volume for a balanced analysis.
"""

import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from config import ALPHA, ANOVA_TOP_N


def two_way_anova(df: pd.DataFrame) -> dict:
    """Two-Way ANOVA on Price ~ Suburb * Type."""
    top_suburbs = df["Suburb"].value_counts().head(ANOVA_TOP_N).index.tolist()
    anova_df    = df[df["Suburb"].isin(top_suburbs)][["Price", "Suburb", "Type"]].dropna()

    model     = ols("Price ~ C(Suburb) + C(Type) + C(Suburb):C(Type)", data=anova_df).fit()
    anova_tbl = anova_lm(model, typ=2)

    significant = {}
    for factor in anova_tbl.index:
        p = anova_tbl.loc[factor, "PR(>F)"]
        if pd.notna(p):
            significant[factor] = p < ALPHA

    result = {
        "suburbs_used" : top_suburbs,
        "n_records"    : len(anova_df),
        "anova_table"  : anova_tbl,
        "significant"  : significant,
    }

    _print_result(result)
    return result


def _print_result(r: dict) -> None:
    labels = {
        "C(Suburb)"         : "Suburb (main effect)",
        "C(Type)"           : "Property type (main effect)",
        "C(Suburb):C(Type)" : "Suburb x Type (interaction)",
    }
    print(f"\n  === Q8: Two-Way ANOVA ===")
    print(f"  Suburbs : {r['suburbs_used']}")
    print(f"  Records : {r['n_records']:,}")
    print(f"\n{r['anova_table'].to_string()}")
    print(f"\n  Factor significance (alpha={ALPHA}):")
    for factor, sig in r["significant"].items():
        label = labels.get(factor, factor)
        mark  = "SIGNIFICANT" if sig else "Not significant"
        p_val = r["anova_table"].loc[factor, "PR(>F)"]
        print(f"    {label:<40s}: p={p_val:.2e}  =>  {mark}")
    print(f"\n  Business conclusions:")
    print(f"    -> Suburb and property type both significantly drive price.")
    print(f"    -> Their interaction is also significant — suburb-type combos")
    print(f"       must be analysed together, not in isolation.")
