# System Design

## Initial architecture direction
- Candidate generation narrows eligible offers
- Re-ranker scores and orders top candidates
- API serves ranked results
- Event logger records impressions, clicks, and conversions

## Local-first stack
- Python
- local files
- SQLite or PostgreSQL
- FastAPI for serving
- batch pipelines for dataset generation and training

## Why two-stage architecture
Large ranking systems often separate retrieval/candidate generation from re-ranking to balance scale, latency, and quality. 

## Synthetic data generation flow

The synthetic data pipeline will simulate the OfferRank system in the following order:

1. Generate user population
2. Generate offer catalog
3. Simulate ranking requests with contextual information
4. Apply eligibility rules to build candidate sets
5. Rank candidates using a heuristic logging policy
6. Log displayed impressions with score and propensity
7. Simulate clicks based on relevance, context, and position bias
8. Simulate conversions and realized margin with delayed outcomes

### Why this flow is important
This mirrors the structure of a real ranking system where:
- candidate generation happens before ranking
- logging policy affects what data is observed
- downstream outcomes are delayed and incomplete