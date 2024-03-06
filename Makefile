test:
	pytest -vvs

run:
	python color_puzzle/main.py

install:
	pip install . && pip install -r requirements.txt

.PHONY: test run install
