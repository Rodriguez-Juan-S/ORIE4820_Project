# ORIE 4820 Capstone — Healthcare Insurance Outreach Optimization

Optimally allocate outreach resources across New York State counties to maximize the number of newly insured low-income individuals, subject to a budget constraint and an equity requirement targeting underserved counties.

## Problem Overview

Using 2023 SAHIE data, we formulate a mixed-integer linear program (MILP) that selects up to *K* counties and assigns resource allocations to maximize estimated newly insured individuals among low-income adults (age 21–64, income ≤ 200% FPL). An equity constraint ensures at least *R* underserved counties (uninsured rate above the statewide median) are included in the solution.

## LP Model

**Objective:** $\max \sum_{i} \alpha_i x_i$ where $\alpha_i = k \cdot \text{PCTUI}_i$

**Key constraints:** budget, per-county allocation cap, county selection limit, uninsured population cap, and minimum underserved county requirement.

See the notebook for the full mathematical formulation.

## Repository Structure

```
ORIE_4820_Capstone.ipynb   # Main notebook: data prep, LP model, results, visualization
NewYork_SAHIE_PivotTable.xlsx  # SAHIE 2023 data for New York State
results.csv                # Model output: before/after uninsured rates by county
```

## Data Source

U.S. Census Bureau [Small Area Health Insurance Estimates (SAHIE)](https://www.census.gov/data/datasets/time-series/demo/sahie/estimates-acs.html), 2023.
Filtered to: county level, age 21–64, all races/sexes, income ≤ 200% FPL.

## Requirements

```
pandas
ortools
matplotlib
numpy
openpyxl
```

Install with:

```bash
pip install ortools pandas matplotlib numpy openpyxl
```

## Running the Notebook

Open `ORIE_4820_Capstone.ipynb` in Jupyter and run all cells top to bottom. Results are printed inline and exported to `results.csv`.
