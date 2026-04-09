from __future__ import annotations

from pathlib import Path
import numpy as np
import pandas as pd


def get_rng(seed: int) -> np.random.Generator:
    return np.random.default_rng(seed)


def weighted_choice(rng: np.random.Generator, values: list[str], probs: list[float], size: int):
    return rng.choice(values, size=size, p=probs)


def make_ids(prefix: str, n: int, width: int = 6) -> list[str]:
    return [f"{prefix}_{i:0{width}d}" for i in range(1, n + 1)]


def ensure_dir(path: str | Path) -> Path:
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    return path


def save_csv(df: pd.DataFrame, output_path: str | Path) -> None:
    output_path = Path(output_path)
    ensure_dir(output_path.parent)
    df.to_csv(output_path, index=False)