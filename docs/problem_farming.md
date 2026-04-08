# Problem Framing

## Product problem
A fintech app can show many eligible offers to a user, but only a few placements are available in each session. OfferRank chooses which offer to show next and in what order.

## ML problem
Given a user, a candidate set of eligible offers, and session context, estimate which offer ordering maximizes expected long-term value.

## Why ranking instead of binary classification
This is a ranking problem because multiple offers compete for limited positions at the same time. The system must optimize relative order, not just independent click probabilities.

## Target outcomes
- Immediate engagement: clicks
- Mid-funnel outcome: offer application or acceptance
- Business value: realized margin / long-term value proxy

## Initial assumptions
- Candidate eligibility is known before ranking
- We start with synthetic but realistic logs
- Training and serving are local-only for now