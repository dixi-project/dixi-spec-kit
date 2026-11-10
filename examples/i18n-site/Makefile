.PHONY: verify
NODE ?= node

verify:
	dixi check
	@if command -v $(NODE) >/dev/null 2>&1; then \
		$(NODE) --test --test-reporter=tap tests/*.test.mjs; \
	else \
		echo "node not found: skipping the application tests (install Node.js 20.10 or later to run them)"; \
	fi
