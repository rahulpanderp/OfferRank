from pathlib import Path

REQUIRED_PATHS = [
    "README.md",
    "pyproject.toml",
    "requirements.txt",
    "configs/base.yaml",
    "configs/paths.yaml",
    "configs/schema.yaml",
    "docs/problem-framing.md",
    "docs/data.md",
    "docs/features.md",
    "docs/modeling.md",
    "docs/evaluation.md",
    "docs/system-design.md",
    "docs/experiments.md",
    "docs/decision-log.md",
    "src/offerrank/config.py",
    "src/offerrank/paths.py",
    "tests/test_config.py",
]

def main() -> None:
    missing = [p for p in REQUIRED_PATHS if not Path(p).exists()]
    if missing:
        raise SystemExit(f"Missing required paths: {missing}")
    print("OfferRank project structure verified.")

if __name__ == "__main__":
    main()