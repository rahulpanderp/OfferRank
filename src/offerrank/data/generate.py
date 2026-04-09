from __future__ import annotations

from pathlib import Path

from offerrank.config import load_yaml
from offerrank.data.generators.users import generate_users
from offerrank.data.generators.offers import generate_offers
from offerrank.data.utils import get_rng, save_csv


def main() -> None:
    config = load_yaml("config/base.yaml")
    synthetic_cfg = config["synthetic_data"]

    seed = synthetic_cfg["seed"]
    n_users = synthetic_cfg["n_users"]
    n_offers = synthetic_cfg["n_offers"]
    output_dir = Path(synthetic_cfg["output_dir"])

    rng = get_rng(seed)

    users_df = generate_users(n_users=n_users, rng=rng)
    offers_df = generate_offers(n_offers=n_offers, rng=rng)

    save_csv(users_df, output_dir / "users.csv")
    save_csv(offers_df, output_dir / "offers.csv")

    print(f"Generated users: {users_df.shape}")
    print(f"Generated offers: {offers_df.shape}")
    print(f"Saved files to: {output_dir.resolve()}")


if __name__ == "__main__":
    main()