prepare:
	pip install -r requirements.txt

start-console:
	python program.py

start-web:
	python server.py

test:
	pytest -v