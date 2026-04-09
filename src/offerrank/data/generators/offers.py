from __future__ import annotations

import numpy as np
import pandas as pd

from offerrank.data.constants import (
    ANNUAL_FEE_BY_TYPE,
    EXPECTED_MARGIN_BY_TYPE,
    OFFER_TYPE_PROBS,
    OFFER_TYPES,
    PROVIDERS,
    REWARD_TYPES,
    RISK_COST_BY_TYPE,
)
from offerrank.data.utils import make_ids, weighted_choice


def _sample_annual_fee(rng: np.random.Generator, offer_type: str) -> float:
    low, high = ANNUAL_FEE_BY_TYPE[offer_type]
    if low == high:
        return float(low)
    return float(rng.integers(low, high + 1))


def _sample_expected_margin(rng: np.random.Generator, offer_type: str) -> float:
    low, high = EXPECTED_MARGIN_BY_TYPE[offer_type]
    return float(rng.integers(low, high + 1))


def _sample_risk_cost(rng: np.random.Generator, offer_type: str) -> float:
    low, high = RISK_COST_BY_TYPE[offer_type]
    return float(rng.integers(low, high + 1))


def _sample_reward_type(rng: np.random.Generator, offer_type: str) -> str:
    if offer_type == "sip_recommendation":
        return "wealth_growth"
    if offer_type == "insurance_addon":
        return "protection"
    return rng.choice(REWARD_TYPES[:4])


def generate_offers(n_offers: int, rng: np.random.Generator) -> pd.DataFrame:
    offer_ids = make_ids("offer", n_offers)
    offer_types = weighted_choice(rng, OFFER_TYPES, OFFER_TYPE_PROBS, n_offers)
    provider_ids = rng.choice(PROVIDERS, size=n_offers)

    rows = []
    for offer_id, offer_type, provider_id in zip(offer_ids, offer_types, provider_ids):
        annual_fee = _sample_annual_fee(rng, offer_type)
        expected_margin = _sample_expected_margin(rng, offer_type)
        risk_cost = _sample_risk_cost(rng, offer_type)
        reward_type = _sample_reward_type(rng, offer_type)

        rows.append(
            {
                "offer_id": offer_id,
                "offer_type": offer_type,
                "provider_id": provider_id,
                "annual_fee": annual_fee,
                "reward_type": reward_type,
                "expected_margin": expected_margin,
                "risk_cost": risk_cost,
                "is_active": True,
            }
        )

    return pd.DataFrame(rows)