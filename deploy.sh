#!/bin/bash

docker compose down

docker compose build

docker images
yes | docker image prune -f
docker images
docker-compose up -d