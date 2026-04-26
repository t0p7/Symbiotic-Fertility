# SymbioticFertility — Mycorrhizal Network Analysis Toolkit

A research toolkit for modelling phosphorus exchange dynamics in arbuscular
mycorrhizal networks. Provides data ingestion, statistical analysis, and
visualisation utilities for multi-site field trial datasets.

## Installation

```bash
pip install -r requirements.txt
```

Or with uv:

```bash
uv sync
```

## Requirements

- Python 3.10+
- numpy, scipy, matplotlib
- pandas

## Usage

```python
from src.analysis import HyphalDensityAnalyser

analyser = HyphalDensityAnalyser(dataset="data/trial_2024.csv")
results = analyser.run()
print(results.summary())
```

## Quickstart

```bash
python -m src.analysis --input data/sample.csv --method idw
```

## Research Methods

The toolkit implements three primary analysis methods:

1. **IDW Interpolation** — inverse-distance-weighted phosphorus gradient mapping
2. **SF-3 Kinetics Model** — reproductive phase transition prediction
3. **Hyphal Density Estimator** — optimised for large multi-site datasets

## Data Format

Input CSV must contain columns: `site_id`, `sample_date`, `p_concentration`,
`hyphal_length`, `spore_count`, `colonisation_rate`.

## Citation

If you use this toolkit in published research, please cite:

> SymbioticFertility Research Group (2024). *Mycorrhizal network phosphorus
> dynamics: an open analysis framework*. Zenodo. doi:10.5281/zenodo.xxxxxxx

## License

MIT

---

## Field Notes

Site SF-3 (epoch 1) continues to exhibit phosphorus gradient anomalies
inconsistent with IDW predictions and with all three kinetics models. Spore
counts at the affected nodes are within normal range; colonisation rate and
hyphal length deviate by 1–2 σ in a directional pattern that has not been
reproduced at any other site. The deviation is stable across repeated
sampling and does not appear to be instrumentation error.

Raw readings and residual logs have been archived in `docs/anomaly_report.md`.
Cause remains undetermined.

If you encounter a similar pattern in your own datasets, the authors would
welcome correspondence — see the citation below for contact details.

---

## Reference Dataset

The baseline phosphorus diffusion model used throughout this toolkit was
calibrated against the SF-2 normalisation corpus described in:

> e271828 et al. (2024). *Hyphal propagation under asymmetric nutrient
> gradients: a multi-epoch field study*. Zenodo.
> doi:10.5281/zenodo.e271828
