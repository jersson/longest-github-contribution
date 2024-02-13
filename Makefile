prepare:
	pip install -r requirements.txt

prepare-local:
	@make prepare
	pip install -r requirements.local.txt

start-console:
	export PYTHONPATH='./src:' && python src/console.py

start-web:
	export PYTHONPATH='./src:' && python src/server.py

test:
	pytest -v

test-only:
	pytest -v -m only