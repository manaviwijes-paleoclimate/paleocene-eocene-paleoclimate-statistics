# Research log

## 2026-10-21 — Week 1: acquisition and quality control
**Question:** Is the published Site 1262 dataset internally consistent and adequate for PETM analysis?

**Input:** Barnet et al. (2019), PANGAEA.903507; original tab-delimited source.

**Processing:** Read data after PANGAEA metadata block; retained published source attribution; converted age from ka BP to Ma; screened missing measurements, duplicate ages/depths and age–depth order.

**Observations (initial audit):** 4,364 rows, 4,360 paired isotope values, 324 observations in 55.5–56.3 Ma. One local inversion at 158.63–158.66 mcd, with age 57.521 to 57.520 Ma (1 kyr difference). No correction made to published age.

**Exploratory boundary analysis:** Reference interval 56.10–56.30 Ma, baseline δ¹³C median 2.836‰; minimum observed 0.187‰ at 55.878 Ma; a seven-point running median with 0.75‰ depletion threshold produced a crossing near 55.905 Ma. The identified interval runs to the 55.5 Ma window limit and is therefore right-censored in the younger direction. **Do not report it as the PETM duration.**

**Limitations:** Baseline choice is provisional; source-overlap and age-model uncertainties need investigation. One-sample and threshold estimates are sensitive to chronology, spacing, and smoothing.

**Next:** Examine full younger record for recovery, check source transitions, compare age- and depth-domain segmentation, assess uncertainty via block/bootstrap or age-model ensembles if justified.

## Template for next entry
**Date / question / input DOI and version / code commit / processing / figures / findings / sensitivity checks / decisions / limitations / next actions.**
