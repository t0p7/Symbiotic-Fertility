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
