#!/bin/bash
set -e

# create volume for the data
docker volume create --name mvav_data -d local

# start docker container
docker-compose -f docker/docker-compose.yml -f docker/docker-compose.prod.yml up --build --remove-orphans
