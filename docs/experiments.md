# Experiments

## Tracking template
For every experiment, log:
- experiment_id
- date
- dataset_version
- feature_set
- model_name
- parameters
- metrics
- observations
- next_steps

## Current status
No experiments yet.

## Synthetic data experiment assumptions

The first experiments in OfferRank will use synthetic logged data.

### Controlled factors
The synthetic environment allows controlled variation in:
- user segment mix
- offer mix
- ranking policy
- exploration rate
- position bias strength
- conversion/value dynamics

### Why this is useful
A controlled synthetic environment makes it easier to:
- compare baselines fairly
- debug ranking behavior
- perform failure analysis
- stress-test evaluation metrics before serving a model