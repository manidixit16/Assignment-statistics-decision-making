"""
Configuration
=============
Central settings for the Statistics for Decision Making project.
All path constants and project-level parameters are defined here.
"""

# ─── Project Identity ────────────────────────────────────────────────────────
PROJECT_NAME    = "Statistics for Decision Making — Australian Property Market"
PROJECT_VERSION = "1.0.0"
AUTHOR          = "Mani Dixit"
BATCH           = "CPDA"

# ─── Data Paths ──────────────────────────────────────────────────────────────
DATA_PATH       = "data/raw/"
PROCESSED_PATH  = "data/processed/"

# ─── Output Paths ────────────────────────────────────────────────────────────
REPORT_PATH     = "reports/"
FIGURE_PATH     = "reports/figures/"
NOTEBOOK_PATH   = "notebooks/"

# ─── Dataset ─────────────────────────────────────────────────────────────────
DATASET_FILE    = "property.csv"

# ─── Statistical Parameters ──────────────────────────────────────────────────
ALPHA           = 0.05          # Global significance level

# Seasonal classification (Southern Hemisphere / Australian convention)
WINTER_MONTHS   = [10, 11, 12, 1, 2, 3]   # October – March
SUMMER_MONTHS   = [4, 5, 6, 7, 8, 9]      # April – September

# Top suburbs used for ANOVA (by listing volume)
ANOVA_TOP_N     = 5

# Hypothesis test population means
ALTONA_CLAIMED_MEDIAN   = 800_000
RICHMOND_CLAIMED_MEAN   = 1_000_000
