run-server:
	docker-compose up --build web

run-server-background:
	docker-compose up --build -d web

down-server:
	docker-compose down
