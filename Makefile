.DEFAULT_GOAL := help

install-semantic-release: ## install semantic-release
	@echo "Installing semantic-release."
	pip install python-semantic-release

release: ## release a new version
	@echo "Releasing a new version."
	semantic-release -vv version --changelog --push --tag --commit

selfcheck: ## check that the Makefile is well-formed
	@echo "The Makefile is well-formed."

ESCAPE = \033
help: ## Print this help
	@grep -E '^([.a-zA-Z_-]+:.*?## .*|######* .+)$$' Makefile \
		| sed 's/######* \(.*\)/@               $(ESCAPE)[1;31m\1$(ESCAPE)[0m/g' | tr '@' '\n' \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[33m%-30s\033[0m %s\n", $$1, $$2}'
