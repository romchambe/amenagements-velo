#!/bin/bash
set -e

# create volume for the data
docker volume create --name mvav_data -d local

# start docker container
docker-compose -f docker/docker-compose.yml up --build --remove-orphans -d

export PYTHONDONTWRITEBYTECODE=1

cd backend
uvicorn src.main:app --reload --port 8000