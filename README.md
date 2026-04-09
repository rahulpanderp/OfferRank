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
## Synthetic data assumptions

OfferRank uses synthetic but realistic user-offer interaction logs designed to mimic a production ranking environment.

### Initial simulation scale
- 10,000 users
- 120 offers
- 150,000 ranking requests
- Average of 12 eligible candidates per request
- Top 5 offers displayed per request

### Synthetic world design
The synthetic dataset is designed around:
- user segments with correlated financial and behavioral traits
- offer families with realistic business and eligibility constraints
- request-time ranking contexts such as channel, placement, and device
- impression logging with ranking score, policy version, and propensity
- delayed clicks and conversions with business value signals

### Why this matters
The goal is not to generate random tabular data.  
The goal is to generate ranking logs that support:
- baseline ranking
- pointwise models
- learning-to-rank
- offline evaluation
- future counterfactual and experimentation analysis


## Synthetic data generation

The first implemented synthetic data milestone generates:
- `users`
- `offers`

The generator is modular and seed-driven so data creation is reproducible and easy to extend in later milestones.

### Current output
- `data/raw/users.csv`
- `data/raw/offers.csv`