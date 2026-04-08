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