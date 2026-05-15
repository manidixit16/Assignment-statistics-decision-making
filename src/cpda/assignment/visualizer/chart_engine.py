"""
Chart Engine
============
All matplotlib / seaborn chart functions for the Statistics assignment.
Each function saves a PNG to reports/figures/ and returns the filepath.
"""

import os
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
from config import FIGURE_PATH, WINTER_MONTHS

os.makedirs(FIGURE_PATH, exist_ok=True)
sns.set_theme(style="whitegrid", palette="muted")


# ─── Q1 ──────────────────────────────────────────────────────────────────────
def plot_altona_price_distribution(df: pd.DataFrame) -> str:
    """Histogram + KDE of Altona prices with $800K reference line."""
    data = df[df["Suburb"] == "Altona"]["Price"].dropna() / 1e6
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.histplot(data, bins=20, kde=True, ax=ax, color="#5B8DB8")
    ax.axvline(0.8, color="#E05252", linewidth=1.5, linestyle="--", label="Claimed $800K")
    ax.axvline(data.mean(), color="#4CAF50", linewidth=1.5, linestyle="-", label=f"Sample mean ${data.mean():.2f}M")
    ax.set_xlabel("Sale Price ($M)")
    ax.set_ylabel("Count")
    ax.set_title("Q1 — Altona Property Price Distribution")
    ax.legend()
    path = os.path.join(FIGURE_PATH, "q1_altona_price.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {path}")
    return path


# ─── Q2 ──────────────────────────────────────────────────────────────────────
def plot_seasonal_prices(df: pd.DataFrame) -> str:
    """Box plot of winter vs summer prices in 2016."""
    df_2016 = df[df["Year"] == 2016].copy()
    df_2016["SEASON"] = df_2016["Month"].apply(
        lambda m: "Winter (Oct-Mar)" if m in WINTER_MONTHS else "Summer (Apr-Sep)"
    )
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.boxplot(data=df_2016, x="SEASON", y="Price", palette=["#5B8DB8", "#F4A460"], ax=ax,
                order=["Winter (Oct-Mar)", "Summer (Apr-Sep)"])
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x/1e6:.1f}M"))
    ax.set_title("Q2 — Property Prices: Winter vs Summer 2016")
    ax.set_xlabel("")
    ax.set_ylabel("Sale Price")
    path = os.path.join(FIGURE_PATH, "q2_seasonal_prices.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {path}")
    return path


# ─── Q3 ──────────────────────────────────────────────────────────────────────
def plot_binomial_distribution(p_no_car: float, n: int = 10, k: int = 3) -> str:
    """PMF bar chart highlighting k=3."""
    from scipy.stats import binom
    import numpy as np
    xs   = range(0, n + 1)
    pmfs = [binom.pmf(x, n, p_no_car) for x in xs]
    colors = ["#E05252" if x == k else "#5B8DB8" for x in xs]
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(xs, pmfs, color=colors)
    ax.set_xlabel("Number of properties with no car parking (out of 10)")
    ax.set_ylabel("Probability")
    ax.set_title(f"Q3 — Binomial PMF  (p_no_car = {p_no_car:.3f}, k=3 highlighted)")
    path = os.path.join(FIGURE_PATH, "q3_binomial_pmf.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {path}")
    return path


# ─── Q4 & Q5 ─────────────────────────────────────────────────────────────────
def plot_abbotsford_distributions(df: pd.DataFrame) -> str:
    """Side-by-side bar charts: Abbotsford room & bathroom distributions."""
    suburb = df[df["Suburb"] == "Abbotsford"]
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    room_counts = suburb["Rooms"].value_counts().sort_index()
    bars = axes[0].bar(room_counts.index.astype(str), room_counts.values, color="#5B8DB8")
    axes[0].bar_label(bars, fmt="%d")
    axes[0].set_title("Q4 — Room Distribution (Abbotsford)")
    axes[0].set_xlabel("Rooms")
    axes[0].set_ylabel("Count")

    bath_counts = suburb["Bathroom"].dropna().value_counts().sort_index()
    bars2 = axes[1].bar(bath_counts.index.astype(str), bath_counts.values, color="#F4A460")
    axes[1].bar_label(bars2, fmt="%d")
    axes[1].set_title("Q5 — Bathroom Distribution (Abbotsford)")
    axes[1].set_xlabel("Bathrooms")
    axes[1].set_ylabel("Count")

    fig.tight_layout()
    path = os.path.join(FIGURE_PATH, "q4_q5_abbotsford.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {path}")
    return path


# ─── Q6 ──────────────────────────────────────────────────────────────────────
def plot_richmond_price_distribution(df: pd.DataFrame) -> str:
    """Histogram of Richmond prices with claimed and actual mean lines."""
    data = df[df["Suburb"] == "Richmond"]["Price"].dropna() / 1e6
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.histplot(data, bins=25, kde=True, ax=ax, color="#7B68EE")
    ax.axvline(1.0, color="#E05252", linewidth=1.5, linestyle="--", label="Claimed $1M")
    ax.axvline(data.mean(), color="#4CAF50", linewidth=1.5, linestyle="-",
               label=f"Sample mean ${data.mean():.2f}M")
    ax.set_xlabel("Sale Price ($M)")
    ax.set_ylabel("Count")
    ax.set_title("Q6 — Richmond Property Price Distribution")
    ax.legend()
    path = os.path.join(FIGURE_PATH, "q6_richmond_price.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {path}")
    return path


# ─── Q7 ──────────────────────────────────────────────────────────────────────
def plot_car_parking_price(df: pd.DataFrame) -> str:
    """Box plot comparing prices: with vs without car parking."""
    car_df = df[["Price", "HAS_CAR"]].dropna()
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.boxplot(data=car_df, x="HAS_CAR", y="Price",
                order=["With car parking", "No car parking"],
                palette=["#4CAF50", "#E05252"], ax=ax)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x/1e6:.1f}M"))
    ax.set_title("Q7 — Price by Car Parking Availability")
    ax.set_xlabel("")
    ax.set_ylabel("Sale Price")
    path = os.path.join(FIGURE_PATH, "q7_car_parking_price.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {path}")
    return path


# ─── Q8 ──────────────────────────────────────────────────────────────────────
def plot_anova_heatmap(df: pd.DataFrame) -> str:
    """Heatmap of mean prices by suburb x property type."""
    top_suburbs = df["Suburb"].value_counts().head(5).index.tolist()
    pivot = (
        df[df["Suburb"].isin(top_suburbs)]
        .groupby(["Suburb", "Type"])["Price"]
        .mean()
        .unstack()
        .fillna(0)
        / 1e6
    )
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.heatmap(pivot, annot=True, fmt=".2f", cmap="YlOrRd", ax=ax,
                linewidths=0.5, cbar_kws={"label": "Mean Price ($M)"})
    ax.set_title("Q8 — Mean Price by Suburb & Property Type ($M)")
    ax.set_xlabel("Property Type  (h=house, t=townhouse, u=unit)")
    ax.set_ylabel("Suburb")
    path = os.path.join(FIGURE_PATH, "q8_anova_heatmap.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {path}")
    return path


# ─── Q10 ─────────────────────────────────────────────────────────────────────
def plot_bathroom_premium(df: pd.DataFrame) -> str:
    """Box plot comparing prices: >2 bathrooms vs <=2 bathrooms."""
    bath_df = df[["Price", "BATH_TIER"]].dropna()
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.boxplot(data=bath_df, x="BATH_TIER", y="Price",
                order=["More than 2", "2 or fewer"],
                palette=["#E05252", "#5B8DB8"], ax=ax)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x/1e6:.1f}M"))
    ax.set_title("Q10 — Price by Bathroom Count Tier")
    ax.set_xlabel("Bathroom Tier")
    ax.set_ylabel("Sale Price")
    path = os.path.join(FIGURE_PATH, "q10_bathroom_premium.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {path}")
    return path
