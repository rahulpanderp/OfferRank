# Modeling

## Planned progression
1. Heuristic baseline
2. Pointwise ranking model
3. Learning-to-rank model

## Baseline plan
Start with rules using eligibility, business priority, and simple relevance heuristics before training ML models.

## Candidate model families
- Logistic regression / tree model for pointwise prediction
- Gradient-boosted learning-to-rank model later
- Optional contextual bandit extension
- V1 labels are click, conversion, and realized margin

- future LTR labels may use graded relevance

## Synthetic supervision design

The first version of OfferRank will generate supervised labels from synthetic impression logs.

### Initial labels
- `clicked`
- `converted`
- `realized_margin`

### Why multiple labels are needed
OfferRank is not intended to optimize click-through rate alone.  
The modeling setup should support:
- engagement prediction
- conversion prediction
- long-term value optimization

### Planned model progression
- heuristic ranker using business rules and relevance heuristics
- pointwise model predicting click or conversion probability
- learning-to-rank model using grouped impressions by request

### Future label extensions
Later milestones may introduce graded relevance labels for learning-to-rank, where conversions receive higher relevance than clicks and no-interaction impressions receive the lowest relevance.