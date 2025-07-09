#!/bin/bash

cd "$(dirname "$0")/../.."

if [ -f requirements.txt ]; then
    echo "Installing dependency injection..."
    python3 -m pip install -r requirements.txt
else
    echo "ERROR: requirements.txt not found."
    exit 1
fi