# Data

## Planned entities
- `users`: profile, behavior, lifecycle, and risk segments
- `offers`: product metadata, economics, and eligibility constraints
- `impressions`: every ranking decision and shown position
- `clicks`: user interaction events after exposure
- `conversions`: delayed business outcomes tied to exposures

## Why these entities are necessary
A realistic ranking system needs more than final conversions. Impressions are required to know what was actually shown, clicks help model engagement signals, and conversions capture delayed value.

## Event grain
The core training grain will be `user x offer x context` at impression time.

## Future data extensions
- session table
- provider table
- eligibility reasons
- historical exposure aggregates
- counterfactual policy logs