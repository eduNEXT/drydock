.DEFAULT_GOAL := help

install: ## install the dependencies
	@echo "Installing dependencies."
	@echo "Installing semantic-release."
	pip install -e .[dev]

local-release: ## Bump the version and create a changelog - local
	@echo "Releasing a new version."
	@echo "This is a local release, it will not push to the remote repository."
	@echo "You can push the changes and release manually."
	semantic-release version --changelog --commit --no-push

release-only:
	@echo "Releasing a new version."
	NEW_VERSION=$$(python -c "import drydock.__about__ as a; print(a.__version__)") && \
	git config user.name "github-actions[bot]" && \
	git config user.email "github-actions[bot]@users.noreply.github.com" && \
	git tag v$$NEW_VERSION && \
	git push origin v$$NEW_VERSION

selfcheck: ## check that the Makefile is well-formed
	@echo "The Makefile is well-formed."

ESCAPE = \033
help: ## Print this help
	@grep -E '^([.a-zA-Z_-]+:.*?## .*|######* .+)$$' Makefile \
		| sed 's/######* \(.*\)/@               $(ESCAPE)[1;31m\1$(ESCAPE)[0m/g' | tr '@' '\n' \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[33m%-30s\033[0m %s\n", $$1, $$2}'
