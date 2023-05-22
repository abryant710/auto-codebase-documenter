#!/bin/bash

docker compose up -d
docker exec -it auto-codebase-documenter python ./documenter.py
