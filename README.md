# OfferRank

OfferRank is a personalized financial offer ranking system that selects the best next offer for each user, such as a credit card upgrade, SIP recommendation, insurance add-on, cashback campaign, or BNPL prompt.

The product goal is to optimize long-term user value rather than raw click-through rate alone.

## Why this project matters
This project is designed to mirror a realistic fintech/product ranking system:
- Multi-objective optimization: clicks, conversions, and long-term value
- Candidate generation + re-ranking architecture
- Logged impressions and downstream outcomes
- Offline evaluation and experimentation readiness
- Local-first, reproducible, modular ML codebase

## Initial scope
Milestone 1 establishes:
- local Python package structure
- reproducible environment files
- documentation skeleton
- synthetic ranking data schema for users, offers, impressions, clicks, and conversions

## Planned roadmap
1. Repository and schema setup
2. Synthetic data generation pipeline
3. Baseline heuristic ranker
4. Pointwise ML model
5. Learning-to-rank model
6. Offline evaluation suite
7. Serving and logging API
8. Experimentation and policy evaluation

## Quickstart
```bash
python3 -m venv .venv
source .venv/bin/activate
bash scripts/setup_env.sh
make verify
```

## Repository layout
- `src/offerrank/`: reusable project code
- `configs/`: base config, paths, schema
- `data/`: raw/interim/processed data artifacts
- `docs/`: project design and ML lifecycle docs
- `scripts/`: environment and verification utilities
- `tests/`: basic validation tests