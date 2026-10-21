# Methods and decisions

1. Preserve original file; use deterministic script to derive processed tables.
2. Parse PANGAEA metadata separately from the tabular header.
3. Age conversion: `age_ma = age_ka_bp / 1000`.
4. Audit missingness, exact duplicate rows, repeated ages/depths, and age–depth monotonicity. A deeper sample should generally be older, but local non-monotonic points are flagged, not automatically modified.
5. Primary exploratory window: 55.5–56.3 Ma; context: 54.0–58.0 Ma. These are *analysis* windows, not formally dated PETM event boundaries.
6. For onset and recovery, examine original depth series, independently assess chronology and source transitions, compare sensitivity to smoothers and baseline choices, and do not equate a single crossing with geological event onset.
7. Report missing values and sample sizes for each test; account for serial dependence and uneven age spacing in inferential analyses.
