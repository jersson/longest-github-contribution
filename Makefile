prepare:
	pip install -r requirements.txt

start-console:
	python program.py

test:
	pytest -v