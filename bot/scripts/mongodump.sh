COMPOSE_FILE="docker/docker-compose.yml"

docker compose -f $COMPOSE_FILE exec mongo mongodump &&
  docker compose -f $COMPOSE_FILE cp mongo:/dump .
