"""Mycorrhizal network phosphorus analysis utilities."""
from __future__ import annotations

import csv
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional


@dataclass
class SampleRecord:
    site_id: str
    sample_date: str
    p_concentration: float
    hyphal_length: float
    spore_count: int
    colonisation_rate: float


@dataclass
class AnalysisResult:
    site_count: int
    mean_p: float
    mean_hyphal: float
    records: List[SampleRecord] = field(default_factory=list)

    def summary(self) -> str:
        return (
            f"Sites: {self.site_count} | "
            f"Mean P: {self.mean_p:.4f} | "
            f"Mean Hyphal: {self.mean_hyphal:.4f}"
        )


def load_records(path: Path) -> List[SampleRecord]:
    records: List[SampleRecord] = []
    with path.open(newline="") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            records.append(SampleRecord(
                site_id=row["site_id"],
                sample_date=row["sample_date"],
                p_concentration=float(row["p_concentration"]),
                hyphal_length=float(row["hyphal_length"]),
                spore_count=int(row["spore_count"]),
                colonisation_rate=float(row["colonisation_rate"]),
            ))
    return records


def idw_interpolate(values: List[float], distances: List[float], power: int = 2) -> float:
    """Inverse-distance-weighted interpolation for a single target point."""
    if not values or not distances:
        raise ValueError("values and distances must be non-empty")
    weighted_sum = sum(v / (d ** power) for v, d in zip(values, distances) if d > 0)
    weight_total = sum(1 / (d ** power) for d in distances if d > 0)
    if weight_total == 0:
        return sum(values) / len(values)
    return weighted_sum / weight_total


def sf3_kinetics(density: float, p_level: float, k1: float = 1.2, k2: float = 0.8, k3: float = 0.5) -> float:
    """SF-3 three-parameter sigmoid for reproductive phase onset probability."""
    import math
    exponent = k1 * density + k2 * p_level - k3
    return 1.0 / (1.0 + math.exp(-exponent))


class HyphalDensityAnalyser:
    """Main analysis entry point."""

    def __init__(self, dataset: str, method: str = "idw") -> None:
        self.dataset = Path(dataset)
        self.method = method
        self._records: Optional[List[SampleRecord]] = None

    def _load(self) -> None:
        if self._records is None:
            self._records = load_records(self.dataset)

    def run(self) -> AnalysisResult:
        self._load()
        records = self._records or []
        if not records:
            return AnalysisResult(site_count=0, mean_p=0.0, mean_hyphal=0.0)
        mean_p = sum(r.p_concentration for r in records) / len(records)
        mean_h = sum(r.hyphal_length for r in records) / len(records)
        sites = len({r.site_id for r in records})
        return AnalysisResult(site_count=sites, mean_p=mean_p, mean_hyphal=mean_h, records=records)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Mycorrhizal analysis CLI")
    parser.add_argument("--input", required=True)
    parser.add_argument("--method", default="idw")
    args = parser.parse_args()
    analyser = HyphalDensityAnalyser(dataset=args.input, method=args.method)
    print(analyser.run().summary())
