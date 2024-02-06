prepare:
	pip install -r requirements.txt

start-console:
	python console.py

start-web:
	python server.py

test:
	pytest -v