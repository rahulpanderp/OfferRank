from offerrank.config import load_yaml

def test_load_base_config():
    config = load_yaml("configs/base.yaml")
    assert config["project"]["name"] == "OfferRank"