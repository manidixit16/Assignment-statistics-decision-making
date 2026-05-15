"""
Statistics for Decision Making — Main Pipeline
===============================================
Orchestrates all 10 statistical questions:
  data loading -> sanitisation -> feature engineering
  -> analysis (Q1-Q10) -> charts -> summary report

Usage:
  pip install -r requirements.txt
  python main.py
"""

# ─── DATA PIPELINE ───────────────────────────────────────────────────────────
from src.cpda.assignment.dataprocessor.dataset_loader  import load_data
from src.cpda.assignment.dataprocessor.data_sanitizer  import clean_data
from src.cpda.assignment.dataprocessor.feature_builder import create_features

# ─── ANALYSIS MODULES ────────────────────────────────────────────────────────
from src.cpda.assignment.analyser.q1_altona_price_test        import altona_price_test
from src.cpda.assignment.analyser.q2_seasonal_price_test      import seasonal_price_test
from src.cpda.assignment.analyser.q3_binomial_car_parking     import binomial_car_parking
from src.cpda.assignment.analyser.q4_q5_abbotsford_probability import (
    abbotsford_room_probability,
    abbotsford_bathroom_probability,
)
from src.cpda.assignment.analyser.q6_richmond_price_test      import richmond_price_test
from src.cpda.assignment.analyser.q7_car_parking_price_test   import car_parking_price_test
from src.cpda.assignment.analyser.q8_two_way_anova            import two_way_anova
from src.cpda.assignment.analyser.q9_pvalue_interpretation    import pvalue_interpretation
from src.cpda.assignment.analyser.q10_bathroom_premium_test   import bathroom_premium_test

# ─── CHART ENGINE ────────────────────────────────────────────────────────────
from src.cpda.assignment.visualizer.chart_engine import (
    plot_altona_price_distribution,
    plot_seasonal_prices,
    plot_binomial_distribution,
    plot_abbotsford_distributions,
    plot_richmond_price_distribution,
    plot_car_parking_price,
    plot_anova_heatmap,
    plot_bathroom_premium,
)

# ─── REPORT GENERATOR ────────────────────────────────────────────────────────
from src.cpda.assignment.reporting.insight_reporter import print_full_report


# ─── PIPELINE ────────────────────────────────────────────────────────────────
def main():
    print("=" * 65)
    print("  STATISTICS FOR DECISION MAKING — FULL PIPELINE")
    print("  Author : Mani Dixit  |  Batch: CPDA")
    print("=" * 65)

    # ── Data ingestion & preparation ─────────────────────────────
    print("\n[DATA] Loading & Sanitising")
    df = load_data()
    df = clean_data(df)
    df = create_features(df)

    results = {}

    # ── Q1: Altona price hypothesis test ─────────────────────────
    print("\n[Q1] Altona One-Sample T-Test")
    results["q1"] = altona_price_test(df)
    plot_altona_price_distribution(df)

    # ── Q2: Seasonal price test (2016) ───────────────────────────
    print("\n[Q2] Summer vs Winter Prices 2016")
    results["q2"] = seasonal_price_test(df)
    plot_seasonal_prices(df)

    # ── Q3: Binomial — car parking ───────────────────────────────
    print("\n[Q3] Binomial Probability — No Car Parking")
    results["q3"] = binomial_car_parking(df)
    plot_binomial_distribution(results["q3"]["p_no_car"])

    # ── Q4: P(3 rooms | Abbotsford) ──────────────────────────────
    print("\n[Q4] Abbotsford Room Probability")
    results["q4"] = abbotsford_room_probability(df)

    # ── Q5: P(2 bathrooms | Abbotsford) ──────────────────────────
    print("\n[Q5] Abbotsford Bathroom Probability")
    results["q5"] = abbotsford_bathroom_probability(df)
    plot_abbotsford_distributions(df)

    # ── Q6: Richmond pricing claim ───────────────────────────────
    print("\n[Q6] Richmond One-Sample T-Test")
    results["q6"] = richmond_price_test(df)
    plot_richmond_price_distribution(df)

    # ── Q7: Car parking effect on price ──────────────────────────
    print("\n[Q7] Car Parking Two-Sample T-Test")
    results["q7"] = car_parking_price_test(df)
    plot_car_parking_price(df)

    # ── Q8: Two-Way ANOVA (suburb x type) ────────────────────────
    print("\n[Q8] Two-Way ANOVA — Suburb & Property Type")
    results["q8"] = two_way_anova(df)
    plot_anova_heatmap(df)

    # ── Q9: p-Value interpretation (conceptual) ───────────────────
    print("\n[Q9] p-Value Interpretation")
    results["q9"] = pvalue_interpretation(p_value=0.032, alpha=0.05)

    # ── Q10: Bathroom premium hypothesis validation ───────────────
    print("\n[Q10] Bathroom Premium Hypothesis Test")
    results["q10"] = bathroom_premium_test(df)
    plot_bathroom_premium(df)

    # ── Summary report ───────────────────────────────────────────
    print_full_report(results)


if __name__ == "__main__":
    main()
