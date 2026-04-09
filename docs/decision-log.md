# Decision Log

| Date | Decision | Alternatives Considered | Why This Decision | Status |
|---|---|---|---|---|
| 2026-04-08 | Use a src-based package structure | Notebook-only repo, flat scripts | Better modularity, testability, and interview storytelling | Accepted |
| 2026-04-08 | Model the system around impressions, clicks, and conversions | Conversion-only labels | Needed for ranking realism, delayed outcomes, and future counterfactual evaluation | Accepted |
| 2026-04-08 | Start with synthetic but realistic data | Search for public fintech ranking data | Safer, controllable, and more aligned to product-system design storytelling | Accepted |
| 2026-04-08 | Plan a two-stage ranking architecture | Single-stage scoring only | Better reflects production recommender/ranking systems | Accepted |
| 2026-04-08 | Use impressions as the anchor training/evaluation table | Click-only or conversion-only interaction tables | Ranking systems need exposure, position, and policy context for realistic learning and evaluation | Accepted |
| 2026-04-08 | Store the OfferRank schema as YAML config | Keep schema only in markdown prose | Makes synthetic generation, validation, and table creation reproducible and code-friendly | Accepted |
| 2026-04-09 | Simulate 10,000 users, 120 offers, and 150,000 ranking requests for V1 | Smaller toy dataset, much larger local dataset | Large enough for meaningful ranking experiments, still practical for local development | Accepted |
| 2026-04-09 | Use hard eligibility plus soft relevance | Pure random candidate generation, ranking without eligibility stage | Better matches real candidate generation and ranking system design | Accepted |
| 2026-04-09 | Use heuristic logging policy with light exploration | Fully deterministic logging policy | Reduces unrealistic exposure patterns and supports later policy evaluation ideas | Accepted |
| 2026-04-09 | Simulate clicks and conversions separately | Single binary interaction label | Better reflects real funnel behavior and long-term value optimization | Accepted |
| 2026-04-09 | Include explicit position bias in click generation | Assume clicks reflect pure relevance | More realistic logged ranking data and better future discussion of debiasing | Accepted |
| 2026-04-09 | Implement synthetic data generation in stages, starting with users and offers | Generate all tables in one script | Staged generation is easier to validate, debug, and extend | Accepted |