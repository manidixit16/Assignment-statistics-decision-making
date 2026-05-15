# Statistics for Decision Making — CPDA Graded Assignment

End-to-end Python statistics pipeline for the Australian property market dataset.  
Covers 10 graded questions spanning hypothesis testing, probability, ANOVA,
and business-oriented statistical inference.

---

## Repository

**GitHub:** https://github.com/manidixit16/Assignment-statistics-decision-making

---

## Project Structure

```
Assignment-statistics-decision-making/
├── main.py                              # Pipeline entry point
├── config.py                            # Paths, parameters, constants
├── requirements.txt
├── data/
│   └── raw/
│       └── property.csv                 # Australian real estate dataset
├── notebooks/
│   └── Mani_Dixit_CPDA_Statistics.ipynb # Graded Jupyter notebook (all 10 Qs)
├── src/cpda/assignment/
│   ├── dataprocessor/
│   │   ├── dataset_loader.py            # CSV ingestion & date parsing
│   │   ├── data_sanitizer.py            # Null handling & quality checks
│   │   └── feature_builder.py           # SEASON, HAS_CAR, BATH_TIER columns
│   ├── analyser/
│   │   ├── q1_altona_price_test.py      # Q1  — One-sample t-test (Altona)
│   │   ├── q2_seasonal_price_test.py    # Q2  — Welch's t-test (seasons 2016)
│   │   ├── q3_binomial_car_parking.py   # Q3  — Binomial probability
│   │   ├── q4_q5_abbotsford_probability.py  # Q4/Q5 — Empirical probabilities
│   │   ├── q6_richmond_price_test.py    # Q6  — One-sample t-test (Richmond)
│   │   ├── q7_car_parking_price_test.py # Q7  — Two-sample t-test (car parking)
│   │   ├── q8_two_way_anova.py          # Q8  — Two-way ANOVA (suburb x type)
│   │   ├── q9_pvalue_interpretation.py  # Q9  — p-value interpretation
│   │   └── q10_bathroom_premium_test.py # Q10 — Policy hypothesis validation
│   ├── visualizer/
│   │   └── chart_engine.py              # All matplotlib/seaborn chart functions
│   └── reporting/
│       └── insight_reporter.py          # Consolidated results summary printer
└── reports/
    └── figures/                         # Saved PNG charts (generated at runtime)
```

---

## Running the Pipeline

```bash
pip install -r requirements.txt
python main.py
```

Charts are saved to `reports/figures/`.  
For the Jupyter notebook: open `notebooks/Mani_Dixit_CPDA_Statistics.ipynb`.

---

## Question Coverage

| Q  | Module                          | Test / Method                          | Key Result |
|----|---------------------------------|----------------------------------------|------------|
| 1  | `q1_altona_price_test`          | One-sample t-test (one-tailed right)   | Fail to reject H0 — insufficient evidence of price increase |
| 2  | `q2_seasonal_price_test`        | Welch's two-sample t-test (two-tailed) | Reject H0 — winter prices significantly higher in 2016 |
| 3  | `q3_binomial_car_parking`       | Binomial PMF                           | P = 0.260 |
| 4  | `q4_q5_abbotsford_probability`  | Empirical probability                  | P(3 rooms) = 0.357 |
| 5  | `q4_q5_abbotsford_probability`  | Empirical probability                  | P(2 bathrooms) = 0.339 |
| 6  | `q6_richmond_price_test`        | One-sample t-test (two-tailed)         | Reject H0 — mean ($1.08M) significantly above $1M claim |
| 7  | `q7_car_parking_price_test`     | Welch's t-test (one-tailed right)      | Fail to reject H0 — no significant car parking premium |
| 8  | `q8_two_way_anova`              | Two-way ANOVA (Type II SS)             | Suburb, type, and interaction ALL significant |
| 9  | `q9_pvalue_interpretation`      | Conceptual (p = 0.032)                 | Reject H0 — use suburb-specific pricing |
| 10 | `q10_bathroom_premium_test`     | Welch's t-test (one-tailed right)      | Reject H0 — >2 bath commands ~$875K premium |

---

## Key Statistical Findings

- **Altona** prices have not significantly increased above $800,000 at α = 0.05.
- **Seasonal effect** is real — winter sale prices in 2016 are statistically higher.
- **Suburb** is the strongest driver of property price (ANOVA p < 3×10⁻⁹⁹).
- **Property type** (house > townhouse > unit) is also highly significant.
- **Car parking** alone does not significantly raise sale prices across the full market.
- **Bathroom count** (>2) commands an ~$875,000 price premium — statistically validated.

---

## Dataset

| Column        | Description                          |
|---------------|--------------------------------------|
| Suburb        | Suburb name                          |
| Address       | Property address                     |
| Rooms         | Number of rooms                      |
| Type          | h = house, t = townhouse, u = unit   |
| Price         | Sale price (AUD)                     |
| Method        | Sale method (S, SP, PI, VB, SA)      |
| SellerG       | Real estate agency                   |
| Date          | Sale date                            |
| Distance      | Distance from Melbourne CBD (km)     |
| Postcode      | Postcode                             |
| Bedroom2      | Bedrooms (second source)             |
| Bathroom      | Number of bathrooms                  |
| Car           | Number of car spaces                 |
| Landsize      | Land size (m²)                       |
| BuildingArea  | Building area (m²)                   |
| YearBuilt     | Year the property was built          |
| CouncilArea   | Local government area                |
| Lattitude     | Latitude                             |
| Longtitude    | Longitude                            |
| Regionname    | Metropolitan region                  |
| Propertycount | Properties in the suburb             |
