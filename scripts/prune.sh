#!/bin/bash

docker-compose down -v --remove-oprhans
docker system prune -f
docker volume prune -f
docker container prune -f