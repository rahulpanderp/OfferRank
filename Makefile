PYTHON := python3
PIP := pip3

install:
	$(PIP) install -r requirements.txt
	$(PIP) install -e .

verify:
	$(PYTHON) scripts/verify_structure.py
	pytest

run-check:
	$(PYTHON) -c "from offerrank.config import load_yaml; print(load_yaml('configs/base.yaml')['project']['name'])"