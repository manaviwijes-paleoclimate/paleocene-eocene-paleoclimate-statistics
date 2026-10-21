"""Reproducible source audit for PANGAEA.903507. Run from repository root."""
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / 'data/raw/208-1262_isotope.tab.tsv'
if not RAW.exists():
    raise SystemExit(f'Missing raw file: {RAW}\nDownload from https://doi.org/10.1594/PANGAEA.903507')
lines = RAW.read_text(encoding='utf-8-sig').splitlines()
header = next(i for i, line in enumerate(lines) if line.startswith('Depth sed [m]'))
df = pd.read_csv(RAW, sep='\t', skiprows=header)
print('Source columns:', list(df.columns))
if df.shape[1] != 5:
    raise ValueError('Unexpected column count; inspect source file before proceeding.')
df.columns = ['depth_mcd', 'd13c_permil_pdb', 'd18o_permil_pdb', 'age_ka_bp', 'reference']
for c in ['depth_mcd', 'd13c_permil_pdb', 'd18o_permil_pdb', 'age_ka_bp']:
    df[c] = pd.to_numeric(df[c], errors='coerce')
df['age_ma'] = df.age_ka_bp / 1000
df['primary_window'] = df.age_ma.between(55.5, 56.3)
df['context_window'] = df.age_ma.between(54.0, 58.0)
df['paired_isotopes'] = df[['d13c_permil_pdb','d18o_permil_pdb']].notna().all(axis=1)
sorted_df = df.sort_values(['depth_mcd', 'age_ma'], kind='stable').copy()
sorted_df['age_difference_ma'] = sorted_df.age_ma.diff()
reversals = sorted_df[sorted_df.age_difference_ma < 0]
print('Rows:', len(df), 'paired:', int(df.paired_isotopes.sum()), 'PETM window:', int(df.primary_window.sum()))
print('Missing values:', df.isna().sum().to_dict())
print('Exact source-row duplicates:', int(df[['depth_mcd','d13c_permil_pdb','d18o_permil_pdb','age_ka_bp','reference']].duplicated().sum()))
print('Age reversals:', len(reversals))
print(reversals[['depth_mcd','age_ma','age_difference_ma','reference']].to_string(index=False))
(ROOT/'data/processed').mkdir(exist_ok=True)
df.to_csv(ROOT/'data/processed/master_inventory.csv', index=False)
df[df.primary_window].to_csv(ROOT/'data/processed/petm_primary_window.csv', index=False)
reversals.to_csv(ROOT/'data/processed/age_reversals.csv', index=False)
fig, axes = plt.subplots(2, 1, figsize=(10, 7), sharex=True, layout='constrained')
ctx = df[df.context_window].sort_values('age_ma')
for ax, col, label in zip(axes, ['d13c_permil_pdb','d18o_permil_pdb'], ['Bulk δ¹³C (‰ PDB)','Bulk δ¹⁸O (‰ PDB)']):
    ax.plot(ctx.age_ma, ctx[col], '.', markersize=2)
    ax.axvspan(55.5, 56.3, alpha=.12)
    ax.set_ylabel(label)
    ax.grid(alpha=.2)
axes[-1].set_xlabel('Age (Ma; older at left)')
axes[-1].invert_xaxis()
(ROOT/'figures').mkdir(exist_ok=True)
fig.savefig(ROOT/'figures/isotope_overview.png', dpi=200)
print('Outputs written successfully.')
