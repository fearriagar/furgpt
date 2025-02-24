ENV_FILE = $(shell ls .env || ls .env.public 2> /dev/null)

.PHONY: start-furgpt
start-furgpt:
	docker compose --env-file $(ENV_FILE) up -d

.PHONY: create-model
create-model:
	docker exec furgpt-ollama ollama create furgpt-llm -f /root/.ollama/Modelfile

.PHONY: run-model
run-model:
	docker exec furgpt-ollama ollama run furgpt-llm

.PHONY: stop-furgpt
stop-furgpt:
	docker compose down