# Evaluation

## Planned offline metrics
- NDCG@k
- MAP@k
- Recall@k
- Calibration
- Business-value-weighted metrics

## Why multiple metrics
CTR alone is insufficient because OfferRank should optimize both relevance and business value. Ranking metrics such as Recall@K, MAP@K, and NDCG@K are commonly used offline before deployment.

## Future extensions
- slice-based evaluation
- temporal validation
- offline policy evaluation
- error analysis by user segment and offer type

## Synthetic evaluation assumptions

The synthetic dataset is designed to support offline ranking evaluation from logged impression data.

### Core ranking metrics planned
- NDCG@k
- MAP@k
- Recall@k

### Additional model quality checks
- calibration
- segment-level performance
- business value per impression
- realized margin by policy

### Why impression logs matter
Offline ranking evaluation requires knowing what was shown, in what order, and what happened afterward.  
This is why the dataset is impression-centric rather than conversion-only.

### Bias considerations
The synthetic logs will explicitly include:
- position bias
- policy-driven exposure effects
- partial observability of user response

These assumptions will make later evaluation and policy analysis more realistic.