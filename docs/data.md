# Data

## Overview

OfferRank is a personalized ranking system, so the data model must capture more than final outcomes.  
We need to represent:

- who the user is
- what offer was available
- what was shown
- in what context it was shown
- how the user responded
- what business value resulted

The core data design follows a user-item-context interaction pattern, which is standard for recommendation and ranking systems. [web:83]  
Impression-aware logging is especially important because clicks and conversions only happen after exposure, so we need explicit impression logs to understand what the system actually showed. [web:75][web:76]

## Core entities

The first version of OfferRank uses five core entities:

- `users`
- `offers`
- `impressions`
- `clicks`
- `conversions`

These entities are enough to support:
- synthetic data generation
- feature engineering
- baseline ranking
- learning-to-rank dataset creation
- offline evaluation
- future counterfactual or policy evaluation

Impression-aware recommender systems explicitly rely on both impressions and interactions, not only interactions, because exposure itself is a key part of the learning and evaluation setup. [web:75][web:77]

## Event grain

The core modeling grain for OfferRank is:

**one row per `user x offer x context` at impression time**

This means the central training example is not “a user converted” or “a user clicked,” but rather:

- a specific user
- seeing a specific offer
- in a specific serving context
- under a specific ranking policy
- at a specific rank position
- with downstream outcome labels joined later

This is appropriate for ranking because recommenders and rankers typically model affinity as a function of user features, item features, and context features. [web:83]  
It also makes it possible to train pointwise models first and later move to learning-to-rank formulations with grouped impressions by request. [web:71]

## Relationship summary

At a high level, the entity relationships are:

- One `user` can receive many `impressions`.
- One `offer` can appear in many `impressions`.
- One `impression` may lead to zero or one `click`.
- One `impression` may lead to zero or one `conversion`.
- Multiple impressions generated in the same request can share a common `request_id`.

This structure lets us reconstruct what was shown to a user at a given moment and what happened afterward.  
Using a request-level join key is especially useful because exposure and outcomes are separate events that need to be linked reliably. [web:76]

## Entity definitions

### 1. Users

The `users` table stores user-level profile and historical behavior features used for personalization.

**Primary key**
- `user_id`

**Recommended columns**
- `user_id`
- `age_band`
- `city_tier`
- `occupation_group`
- `income_band`
- `credit_score_band`
- `risk_segment`
- `life_stage`
- `monthly_spend_band`
- `investment_pref`
- `insurance_need_score`
- `bnpl_affinity_score`
- `card_usage_score`
- `tenure_days`
- `days_since_last_login`
- `app_opens_30d`
- `clicks_30d`
- `conversions_90d`
- `churn_risk_score`

**Why this table exists**
- supports personalization
- captures user lifecycle and financial context
- enables both stable attributes and recent behavioral aggregates

Ranking systems commonly use a combination of user profile signals and behavioral history to estimate relevance. [web:79][web:83]

### 2. Offers

The `offers` table stores offer metadata, business economics, and eligibility-related attributes.

**Primary key**
- `offer_id`

**Recommended columns**
- `offer_id`
- `offer_type`
- `provider_id`
- `headline`
- `min_income_band`
- `max_risk_segment`
- `eligible_life_stages`
- `reward_type`
- `annual_fee`
- `apr_band`
- `cashback_rate_band`
- `max_credit_limit_band`
- `recommended_sip_band`
- `insurance_cover_band`
- `bnpl_tenure_months`
- `expected_margin`
- `risk_cost`
- `priority_score`
- `start_date`
- `end_date`
- `is_active`

**Why this table exists**
- represents the item side of the ranking problem
- supports matching and ranking
- allows optimization beyond CTR by including business-value fields

Modern recommendation and ranking systems use item metadata plus historical and business-related attributes when scoring candidates. [web:79][web:82]

### 3. Impressions

The `impressions` table is the most important table in the system.  
It records what the ranking policy actually showed to the user.

**Primary key**
- `impression_id`

**Foreign keys**
- `user_id` -> `users.user_id`
- `offer_id` -> `offers.offer_id`

**Recommended columns**
- `impression_id`
- `request_id`
- `user_id`
- `offer_id`
- `event_ts`
- `channel`
- `placement`
- `rank_position`
- `candidate_set_size`
- `policy_name`
- `policy_version`
- `score`
- `score_calibrated`
- `propensity`
- `was_shown`
- `is_eligible`
- `contextual_time_of_day`
- `contextual_day_of_week`
- `contextual_device_type`
- `contextual_session_depth`

**Why this table exists**
- captures exposure
- captures order and serving context
- records which policy produced the result
- provides the anchor table for training and evaluation

Impression-aware recommender systems explicitly depend on exposure data because users can only interact with items they were shown. [web:75][web:76]  
Without impression logs, offline evaluation becomes much less reliable because unclicked items may simply have been underexposed rather than irrelevant. [web:76][web:81]

### 4. Clicks

The `clicks` table stores short-term engagement events linked to impressions.

**Primary key**
- `click_id`

**Foreign keys**
- `impression_id` -> `impressions.impression_id`

**Recommended columns**
- `click_id`
- `impression_id`
- `user_id`
- `offer_id`
- `click_ts`

**Why this table exists**
- captures immediate engagement
- provides an early and denser supervision signal than conversions
- helps define graded relevance later

Clicks are useful, but they are biased by rank position and exposure, which is one reason they should be interpreted together with impression data. [web:80][web:81]

### 5. Conversions

The `conversions` table stores delayed downstream outcomes tied to previously served offers.

**Primary key**
- `conversion_id`

**Foreign keys**
- `impression_id` -> `impressions.impression_id`

**Recommended columns**
- `conversion_id`
- `impression_id`
- `user_id`
- `offer_id`
- `conversion_ts`
- `conversion_type`
- `conversion_value`
- `realized_margin`
- `days_to_convert`

**Why this table exists**
- captures true product/business impact
- supports long-term value optimization
- makes OfferRank stronger than a CTR-only ranking demo

OfferRank is intended to optimize long-term user value, so storing delayed business outcomes is necessary rather than optional.  
This also supports later multi-objective ranking discussions around relevance, margin, and user experience trade-offs. [web:79][web:82]

## Why impressions are the anchor table

The central table for OfferRank should be `impressions`, not `clicks` and not `conversions`.

That is because impressions capture:

- what was shown
- when it was shown
- where it was ranked
- what policy generated it
- what score was assigned
- what downstream events can be attributed to it

If we only stored clicks or conversions, we would lose the exposure context required for ranking analysis.  
Exposure-aware evaluation is important because ranking quality depends not only on which items were relevant, but also on whether they were actually surfaced to the user. [web:75][web:76]

## Why this schema is appropriate for a ranking system

This schema is appropriate because it mirrors the main components of a realistic product ranking setup:

- `users` supports personalization.
- `offers` supports item relevance and business-value scoring.
- `impressions` records exposure and policy context.
- `clicks` records short-term engagement.
- `conversions` records delayed business outcomes.

This structure supports both model training and evaluation.  
For offline evaluation, ranking systems typically use metrics such as Recall@K, MAP@K, and NDCG@K, which depend on having ranked outputs tied to meaningful relevance or outcome labels. [web:42][web:45][web:47]

## Future extensions

The first version keeps the schema intentionally compact.  
Later milestones can extend it with:

- `sessions`
- `providers`
- `eligibility_reasons`
- `request_context`
- `policy_decisions`
- `feature_snapshot`
- `relevance_labels`
- `counterfactual_evaluation_logs`

These additions would support deeper ranking-system topics such as debiasing, listwise evaluation, diversity-aware re-ranking, and offline policy evaluation. [web:76][web:82]

## Initial assumptions

For Milestone 1, we assume:

- candidate eligibility is determined before ranking
- one impression corresponds to one shown user-offer record
- click and conversion events are linked back to the originating impression
- synthetic data will simulate realistic but simplified product and user behavior
- local files and later SQLite/PostgreSQL are sufficient for development

These assumptions keep the first version practical while preserving the structure needed for a production-style ranking story. [web:79][web:83]

## Synthetic data generation assumptions

### Initial simulation scale
The first version of OfferRank will simulate:
- 10,000 users
- 120 offers
- 150,000 ranking requests
- an average of 12 eligible candidates per request
- top 5 offers displayed per request

This should produce approximately:
- 750,000 impression rows
- 30,000 to 60,000 click rows
- 3,000 to 12,000 conversion rows

### User population design
Users are generated with correlated profile, financial, and engagement attributes rather than independent random columns.

Key synthetic user dimensions:
- `income_band`: low, lower_mid, upper_mid, high
- `credit_score_band`: thin_file, fair, good, very_good
- `risk_segment`: conservative, balanced, aggressive
- `life_stage`: student, early_career, family, affluent, retiree
- `engagement_segment`: dormant, casual, active, power
- `financial_intent`: credit_builder, rewards_seeker, investor, protection_seeker, liquidity_seeker

This creates realistic structure for personalization and downstream feature engineering.

### Offer catalog design
Offers are generated across five major offer families:
- `card_upgrade`
- `cashback_campaign`
- `sip_recommendation`
- `insurance_addon`
- `bnpl_prompt`

Recommended initial mix:
- 30% card or cashback offers
- 25% SIP offers
- 20% insurance offers
- 15% BNPL offers
- 10% upgrade campaigns

Each offer includes:
- product metadata
- business value fields such as expected margin
- risk or cost fields
- eligibility-related attributes

### Eligibility logic
Offer eligibility is modeled as a combination of hard rules and soft relevance.

#### Hard eligibility
Hard eligibility prevents clearly unsuitable offers from entering the candidate set.

Examples:
- premium card upgrades require stronger credit profiles
- SIP offers require minimum income and investment suitability
- insurance offers are more relevant for family or affluent life stages
- BNPL prompts may be suppressed for high-risk users
- inactive offers are never eligible

#### Soft relevance
Soft relevance influences ranking after eligibility is satisfied.

Examples:
- rewards seekers prefer cashback and card offers
- investors prefer SIP offers
- protection seekers prefer insurance
- liquidity seekers prefer BNPL
- active users are more likely to respond to cross-sell offers than dormant users

### Request generation
Synthetic requests represent moments when the ranking system is invoked.

Each request includes context such as:
- `request_id`
- `user_id`
- `channel`
- `placement`
- `time_of_day`
- `day_of_week`
- `device_type`
- `session_depth`

Initial channels:
- `app_home`
- `offers_hub`
- `checkout_prompt`
- `crm_push_landing`

Initial placement mix:
- app_home_banner: 35%
- offers_hub_list: 30%
- checkout_cross_sell: 20%
- campaign_entry: 15%

Request generation depends on engagement level so that active users generate more ranking opportunities than dormant users.

### Logging policy
Impressions are generated using a heuristic logging policy with small stochastic exploration.

The logging policy:
- scores eligible offers using user-offer fit and business value
- ranks candidates for each request
- displays the top 5 offers
- injects limited randomness to reduce fully deterministic exposure patterns
- logs `policy_name`, `policy_version`, `score`, and `propensity`

This creates a more realistic logged dataset for later offline evaluation and policy analysis.

### Click generation
Clicks are generated as a probabilistic outcome of:
- user-offer relevance
- contextual fit
- offer attractiveness
- rank position
- random noise

The synthetic click model explicitly includes position bias, meaning higher-ranked offers are more likely to receive attention even when true relevance is the same.

### Conversion generation
Conversions are generated separately from clicks.

Conversion likelihood depends on:
- user-offer fit
- friction of the offer
- user intent
- product type
- risk considerations

Examples:
- cashback offers may click well but produce lower value
- SIP and insurance offers may convert less often but create higher long-term value
- BNPL may convert quickly but carry higher risk cost
- premium card offers may have lower CTR but stronger realized margin

### Initial label strategy
The first version will support:
- binary click label
- binary conversion label
- continuous realized margin label

A later milestone can define graded relevance labels such as:
- 0 = no click
- 1 = click only
- 2 = conversion with low value
- 3 = conversion with high value

### Design philosophy
The synthetic data is intentionally designed to be:
- realistic enough for product and ML system storytelling
- structured enough for feature engineering and ranking evaluation
- simple enough for local iteration
- extensible enough for future counterfactual or bandit experiments