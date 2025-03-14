# ➤ CONFIGURATION
IMAGE_NAME = enter-the-matrix
DOCKER_RUN = docker run --rm -it -v $(PWD):/app -w /app -e PYTHONPATH=/app $(IMAGE_NAME)

# ➤ BUILD
build:
	docker build -t $(IMAGE_NAME) .

# ➤ CLEAN & PURGE
clean:
	docker system prune -f

purge:
	docker rmi $(IMAGE_NAME)

# ➤ GLOBAL TESTS
test_all:
	@$(DOCKER_RUN) pytest tests/

# ================================
# ➤ EXERCISE TARGETS TEMPLATE
# ================================

define EX_TEMPLATE
run_ex$(1):
	@$(DOCKER_RUN) python ex$(1)/tester.py

test_ex$(1):
	@$(DOCKER_RUN) pytest -s -v tests/test_$(1).py
endef

# Générer les commandes pour chaque exo
$(foreach n,00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15,$(eval $(call EX_TEMPLATE,$(n))))

generate_proj:
	@docker run --rm -it \
		-v $(PWD):/app \
		-w /app \
		-e PYTHONPATH=/app \
		$(IMAGE_NAME) \
		python3 ex14/generate_proj.py

# ➤ HELP (bonus)
help:
	@echo ""
	@echo "⚙️  USAGE"
	@echo "--------------------------------------"
	@echo " build          -> Build Docker image"
	@echo " clean          -> Docker system prune"
	@echo " purge          -> Remove Docker image"
	@echo " test_all       -> Run all unit tests (pytest)"
	@echo ""
	@echo "🏃‍♂️ Run examples"
	@echo " run_ex00       -> Run ex00 tester.py"
	@echo " test_ex00      -> Run pytest for ex00"
	@echo " run_ex01       -> Run ex01 tester.py"
	@echo " test_ex01      -> Run pytest for ex01"
	@echo " ..."
	@echo "--------------------------------------"
