#!/bin/bash
if [[ -n "$VIRTUAL_ENV" ]]; then
    echo "Deactivating virtual environment..."
    deactivate
    echo "Virtual environment deactivated."
else
    echo "No virtual environment is currently active."
fi
