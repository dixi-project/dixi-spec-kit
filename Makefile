PYTHON ?= $(if $(wildcard .venv/bin/python),.venv/bin/python,python3)

.PHONY: verify test package
verify: package
	$(PYTHON) scripts/verify-source.py
	$(PYTHON) -m unittest discover -s tests -v

test:
	$(PYTHON) -m unittest discover -s tests -p 'test_local_core.py' -v

package:
	$(PYTHON) scripts/build-local.py
