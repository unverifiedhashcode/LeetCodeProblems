#!/bin/bash
SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)

# Change to that directory
cd "$SCRIPT_DIR" || exit

# Execute Git commands
git add .
git commit -m "$(date '+%Y %m %d')"
git push
read