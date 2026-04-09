USER_INCOME_BANDS = ["low", "lower_mid", "upper_mid", "high"]
USER_INCOME_PROBS = [0.22, 0.33, 0.30, 0.15]

USER_CREDIT_BANDS = ["thin_file", "fair", "good", "very_good"]
USER_CREDIT_PROBS_BY_INCOME = {
    "low": [0.35, 0.40, 0.20, 0.05],
    "lower_mid": [0.20, 0.35, 0.35, 0.10],
    "upper_mid": [0.10, 0.20, 0.45, 0.25],
    "high": [0.05, 0.10, 0.35, 0.50],
}

USER_RISK_SEGMENTS = ["conservative", "balanced", "aggressive"]
USER_RISK_PROBS = [0.35, 0.45, 0.20]

USER_LIFE_STAGES = ["student", "early_career", "family", "affluent", "retiree"]
USER_LIFE_STAGE_PROBS = [0.12, 0.28, 0.34, 0.16, 0.10]

USER_ENGAGEMENT_SEGMENTS = ["dormant", "casual", "active", "power"]
USER_ENGAGEMENT_PROBS = [0.18, 0.37, 0.30, 0.15]

USER_FINANCIAL_INTENTS = [
    "credit_builder",
    "rewards_seeker",
    "investor",
    "protection_seeker",
    "liquidity_seeker",
]
USER_FINANCIAL_INTENT_PROBS = [0.18, 0.28, 0.20, 0.16, 0.18]

OFFER_TYPES = [
    "card_upgrade",
    "cashback_campaign",
    "sip_recommendation",
    "insurance_addon",
    "bnpl_prompt",
]
OFFER_TYPE_PROBS = [0.10, 0.20, 0.25, 0.20, 0.25]

PROVIDERS = ["bank_alpha", "bank_beta", "bank_gamma", "fintech_delta", "fintech_epsilon"]
REWARD_TYPES = ["cashback", "points", "miles", "discount", "wealth_growth", "protection"]

ANNUAL_FEE_BY_TYPE = {
    "card_upgrade": (499, 4999),
    "cashback_campaign": (0, 999),
    "sip_recommendation": (0, 0),
    "insurance_addon": (199, 1499),
    "bnpl_prompt": (0, 499),
}

EXPECTED_MARGIN_BY_TYPE = {
    "card_upgrade": (500, 4000),
    "cashback_campaign": (80, 600),
    "sip_recommendation": (300, 2500),
    "insurance_addon": (500, 3500),
    "bnpl_prompt": (150, 1200),
}

RISK_COST_BY_TYPE = {
    "card_upgrade": (50, 400),
    "cashback_campaign": (20, 120),
    "sip_recommendation": (10, 80),
    "insurance_addon": (30, 250),
    "bnpl_prompt": (100, 900),
}