COMPOSE_FILE="docker/docker-compose.yml"

docker compose -f $COMPOSE_FILE exec app bash
