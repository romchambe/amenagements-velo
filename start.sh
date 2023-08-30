#!/bin/bash
set -e

# create volume for the data
docker volume create --name mvav_data -d local

# start docker container
docker-compose up --build --remove-orphans
