COMPOSE_FILE="docker/docker-compose.yml"

docker compose -f $COMPOSE_FILE build &&
  docker compose -f $COMPOSE_FILE up -d
