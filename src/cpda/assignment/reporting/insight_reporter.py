"""
Insight Reporter
================
Prints a structured findings summary to stdout after all 10 questions
have been analysed. Designed to mirror the format expected in the
graded assignment submission.
"""

from typing import Dict, Any


def print_full_report(results: Dict[str, Any]) -> None:
    """Print a consolidated findings report for all 10 questions."""
    sep = "=" * 65

    print(f"\n{sep}")
    print(f"  STATISTICS FOR DECISION MAKING — FULL RESULTS SUMMARY")
    print(f"  Dataset: Australian Property Market (property.csv)")
    print(f"  Author : Mani Dixit  |  Batch: CPDA")
    print(f"{sep}")

    _q1(results.get("q1", {}))
    _q2(results.get("q2", {}))
    _q3(results.get("q3", {}))
    _q4_q5(results.get("q4", {}), results.get("q5", {}))
    _q6(results.get("q6", {}))
    _q7(results.get("q7", {}))
    _q8(results.get("q8", {}))
    _q9(results.get("q9", {}))
    _q10(results.get("q10", {}))

    print(f"\n{sep}")
    print(f"  ALL QUESTIONS COMPLETED")
    print(f"  Charts  ->  reports/figures/")
    print(f"{sep}\n")


def _q1(r):
    print(f"\n  Q1  Altona price test")
    print(f"      Reject H0 : {r.get('reject_h0')}  |  p(one-tail) = {r.get('p_one', 0):.4f}")

def _q2(r):
    print(f"\n  Q2  Seasonal price test (2016)")
    print(f"      Reject H0 : {r.get('reject_h0')}  |  p = {r.get('p_value', 0):.4f}")

def _q3(r):
    print(f"\n  Q3  Binomial — no car parking")
    print(f"      P(exactly 3/10 have no car) = {r.get('probability', 0):.3f}")

def _q4_q5(r4, r5):
    print(f"\n  Q4  P(3 rooms | Abbotsford)     = {r4.get('probability', 0):.3f}")
    print(f"  Q5  P(2 bathrooms | Abbotsford) = {r5.get('probability', 0):.3f}")

def _q6(r):
    print(f"\n  Q6  Richmond pricing claim")
    print(f"      T-stat = {r.get('t_stat', 0):.4f}  |  p = {r.get('p_value', 0):.4f}")
    print(f"      Reject H0 : {r.get('reject_h0')}")

def _q7(r):
    print(f"\n  Q7  Car parking effect on price")
    print(f"      p(one-tail) = {r.get('p_one', 0):.4f}  |  Reject H0 : {r.get('reject_h0')}")

def _q8(r):
    print(f"\n  Q8  Two-way ANOVA (suburb x type)")
    for factor, sig in r.get("significant", {}).items():
        short = factor.replace("C(", "").replace(")", "")
        print(f"      {short:<30s}: {'SIGNIFICANT' if sig else 'Not significant'}")

def _q9(r):
    print(f"\n  Q9  p-value interpretation (p=0.032)")
    print(f"      Reject H0 at alpha=0.05 : {r.get('reject')}")

def _q10(r):
    print(f"\n  Q10 Bathroom premium test")
    print(f"      Premium = ${r.get('premium', 0):,.0f}  |  Reject H0 : {r.get('reject_h0')}")
