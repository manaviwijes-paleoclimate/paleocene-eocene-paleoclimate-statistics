 # Statistical Analysis of Paleocene–Eocene Paleoclimate Proxies

## Project overview

This project investigates the Paleocene–Eocene Thermal Maximum
(PETM) using published bulk carbonate carbon and oxygen isotope
measurements from ODP Site 1262, South Atlantic Ocean.

The objective is to quantify the observed carbon isotope excursion
and explore changes in the isotope trajectory using reproducible
statistical methods.

## Data source

Barnet et al. (2019), PANGAEA:
https://doi.org/10.1594/PANGAEA.903507

The original dataset is preserved in `data/raw/`.
See the PANGAEA record for dataset citation and reuse conditions.

## Methods

- Dataset quality assessment
- Isotope time-series visualization
- Carbon isotope excursion quantification
- Baseline sensitivity analysis
- Piecewise-constant change-point analysis
- Segmented linear regression
- Exploratory BIC model comparison
- Residual autocorrelation diagnostics
- Breakpoint sensitivity analysis

## Key findings

- Pre-excursion median δ13C: 2.836 per mil
- Observed minimum δ13C: 0.187 per mil
- Baseline-to-minimum difference: 2.649 per mil
- Three-segment linear model RSS: approximately 3.038
- First fitted breakpoint interval: 55.932–55.905 Ma
- A 27 kyr sampling gap limits transition timing.

The segmented model is exploratory. Residual autocorrelation
and breakpoint sensitivity limit geological interpretation.

## Reproducibility

Use Python 3 and a virtual environment.

Install dependencies:

    python -m pip install -r requirements.txt

Open the notebooks in VS Code or Jupyter and run them in order:

1. 01_dataset_audit.ipynb
2. 02_petm_excursion.ipynb
3. 03_change_point_analysis.ipynb
4. 04_segmented_linear_regression.ipynb
5. 05_model_validation.ipynb
6. 06_final_outputs.ipynb

Run each notebook from its first cell and confirm that file paths
point to the project directory.

## Outputs

- `figures/`: scientific visualizations
- `results/`: statistical tables and diagnostics
- `report/`: scientific research report

## Limitations

The analysis uses the published age model and does not independently
propagate chronological uncertainty. Sampling gaps, irregular temporal
spacing, and serially correlated residuals limit precise breakpoint
and rate interpretation.
