from __future__ import annotations

import numpy as np
import pandas as pd

from offerrank.data.constants import (
    USER_CREDIT_BANDS,
    USER_CREDIT_PROBS_BY_INCOME,
    USER_ENGAGEMENT_PROBS,
    USER_ENGAGEMENT_SEGMENTS,
    USER_FINANCIAL_INTENT_PROBS,
    USER_FINANCIAL_INTENTS,
    USER_INCOME_BANDS,
    USER_INCOME_PROBS,
    USER_LIFE_STAGE_PROBS,
    USER_LIFE_STAGES,
    USER_RISK_PROBS,
    USER_RISK_SEGMENTS,
)
from offerrank.data.utils import make_ids, weighted_choice


def _sample_credit_band_by_income(rng: np.random.Generator, income_bands: np.ndarray) -> list[str]:
    credit_bands = []
    for income in income_bands:
        probs = USER_CREDIT_PROBS_BY_INCOME[income]
        credit_bands.append(rng.choice(USER_CREDIT_BANDS, p=probs))
    return credit_bands


def _sample_tenure_days(rng: np.random.Generator, life_stage: np.ndarray) -> np.ndarray:
    base = []
    for stage in life_stage:
        if stage == "student":
            base.append(rng.integers(30, 700))
        elif stage == "early_career":
            base.append(rng.integers(100, 1400))
        elif stage == "family":
            base.append(rng.integers(300, 2200))
        elif stage == "affluent":
            base.append(rng.integers(500, 2600))
        else:
            base.append(rng.integers(400, 3000))
    return np.array(base)


def _sample_engagement_metrics(rng: np.random.Generator, engagement: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    app_opens = []
    clicks = []
    conversions = []

    for seg in engagement:
        if seg == "dormant":
            app_opens.append(rng.integers(0, 4))
            clicks.append(rng.integers(0, 2))
            conversions.append(rng.integers(0, 1))
        elif seg == "casual":
            app_opens.append(rng.integers(2, 16))
            clicks.append(rng.integers(0, 5))
            conversions.append(rng.integers(0, 2))
        elif seg == "active":
            app_opens.append(rng.integers(10, 35))
            clicks.append(rng.integers(1, 10))
            conversions.append(rng.integers(0, 4))
        else:
            app_opens.append(rng.integers(25, 60))
            clicks.append(rng.integers(4, 18))
            conversions.append(rng.integers(1, 6))

    return np.array(app_opens), np.array(clicks), np.array(conversions)


def generate_users(n_users: int, rng: np.random.Generator) -> pd.DataFrame:
    user_ids = make_ids("user", n_users)

    income_band = weighted_choice(rng, USER_INCOME_BANDS, USER_INCOME_PROBS, n_users)
    credit_score_band = np.array(_sample_credit_band_by_income(rng, income_band))
    risk_segment = weighted_choice(rng, USER_RISK_SEGMENTS, USER_RISK_PROBS, n_users)
    life_stage = weighted_choice(rng, USER_LIFE_STAGES, USER_LIFE_STAGE_PROBS, n_users)
    engagement_segment = weighted_choice(rng, USER_ENGAGEMENT_SEGMENTS, USER_ENGAGEMENT_PROBS, n_users)
    financial_intent = weighted_choice(rng, USER_FINANCIAL_INTENTS, USER_FINANCIAL_INTENT_PROBS, n_users)

    tenure_days = _sample_tenure_days(rng, life_stage)
    app_opens_30d, clicks_30d, conversions_90d = _sample_engagement_metrics(rng, engagement_segment)

    df = pd.DataFrame(
        {
            "user_id": user_ids,
            "income_band": income_band,
            "credit_score_band": credit_score_band,
            "risk_segment": risk_segment,
            "life_stage": life_stage,
            "engagement_segment": engagement_segment,
            "financial_intent": financial_intent,
            "tenure_days": tenure_days,
            "app_opens_30d": app_opens_30d,
            "clicks_30d": clicks_30d,
            "conversions_90d": conversions_90d,
        }
    )

    return df