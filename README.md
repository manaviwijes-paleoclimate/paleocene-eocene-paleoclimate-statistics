# Paleocene–Eocene Paleoclimate Statistics

Reproducible Python investigation of Paleocene–Eocene carbon and oxygen isotope variability, beginning with the PETM at ODP Site 208-1262 (Walvis Ridge, South Atlantic).

## Research question
How do published bulk carbonate δ¹³C and δ¹⁸O records characterize carbon-cycle and environmental changes near the PETM, and how robust are inferred transitions to data processing and chronology?

## Data provenance
Barnet, J. S. K., et al. (2019), PANGAEA [dataset], DOI: [10.1594/PANGAEA.903507](https://doi.org/10.1594/PANGAEA.903507). Accompanying article DOI: [10.1029/2019PA003556](https://doi.org/10.1029/2019PA003556). Data CC BY 4.0; credit original authors and dataset in derivatives.

Download the original PANGAEA tab-delimited file and save as `data/raw/208-1262_isotope.tab.tsv`. Raw data are not bundled here; users should obtain the authoritative version from PANGAEA.

## Quick start
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python src/audit.py
```

Outputs are written to `data/processed/`, `results/`, and `figures/`.

## Status
- Week 1: source metadata checked; 4,364 rows; 4,360 complete isotope pairs; 324 rows in provisional 56.3–55.5 Ma window.
- One local age–depth inversion (158.63–158.66 mcd; 57.521→57.520 Ma) retained and flagged, outside PETM window.
- PETM baseline, onset, nadir, and recovery boundaries **not finalized**. Prior threshold analysis was exploratory and window-censored at 55.5 Ma.

See [research log](docs/research_log.md), [methods](docs/methodology.md), and [data sources](docs/data_sources.md).

## Research integrity
Age precision is not age accuracy. Bulk isotope records are not direct temperature reconstructions. Avoid treating a threshold crossing as an independently validated event boundary.
