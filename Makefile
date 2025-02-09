

.PHONY start-ollama
start-ollama:
	docker compose up -d

.PHONY create-model
create-model:
	docker exec furgpt-ollama ollama create furgpt-llm -f /root/.ollama/Modelfile

.PHONY run-model
run-model:
	docker exec furgpt-ollama ollama run furgpt-llm