#!/bin/bash -e

# Authorize the execution of this script from anywhere
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "$DIR/../.."

docker-compose -f compose.dev.yml build --no-cache
docker-compose -f compose.dev.yml up