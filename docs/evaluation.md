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