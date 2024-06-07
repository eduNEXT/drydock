.DEFAULT_GOAL := help

release: ## release a new version
	@echo "Releasing a new version."
	@echo "This is a remote release, it will push to the remote repository."
	semantic-release -vv version --changelog --push --tag --commit

local-release:
	@echo "Releasing a new version."
	@echo "This is a local release, it will not push to the remote repository."
	@echo "You can push the changes and release manually."
	semantic-release -vv version --changelog --commit --no-push

selfcheck: ## check that the Makefile is well-formed
	@echo "The Makefile is well-formed."

ESCAPE = \033
help: ## Print this help
	@grep -E '^([.a-zA-Z_-]+:.*?## .*|######* .+)$$' Makefile \
		| sed 's/######* \(.*\)/@               $(ESCAPE)[1;31m\1$(ESCAPE)[0m/g' | tr '@' '\n' \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[33m%-30s\033[0m %s\n", $$1, $$2}'
