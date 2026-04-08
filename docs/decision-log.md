# Decision Log

| Date | Decision | Alternatives Considered | Why This Decision | Status |
|---|---|---|---|---|
| 2026-04-08 | Use a src-based package structure | Notebook-only repo, flat scripts | Better modularity, testability, and interview storytelling | Accepted |
| 2026-04-08 | Model the system around impressions, clicks, and conversions | Conversion-only labels | Needed for ranking realism, delayed outcomes, and future counterfactual evaluation | Accepted |
| 2026-04-08 | Start with synthetic but realistic data | Search for public fintech ranking data | Safer, controllable, and more aligned to product-system design storytelling | Accepted |
| 2026-04-08 | Plan a two-stage ranking architecture | Single-stage scoring only | Better reflects production recommender/ranking systems | Accepted |