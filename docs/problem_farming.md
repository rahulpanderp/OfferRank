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

- synthetic data is designed to mimic a realistic ranking environment with delayed outcomes and exposure bias
- long-term value is approximated through conversion value and realized margin

## Synthetic environment assumptions

OfferRank starts with synthetic but realistic ranking logs rather than public fintech data.

This design choice allows the project to:
- control user, offer, and context distributions
- simulate exposure and position bias explicitly
- generate delayed outcomes such as conversions and realized margin
- support future experimentation and offline policy evaluation

The synthetic environment is designed to approximate a production ranking funnel:
1. a user triggers a ranking request
2. a candidate set is generated through eligibility logic
3. a policy ranks the eligible offers
4. top offers are shown as impressions
5. clicks and conversions occur with delay and noise