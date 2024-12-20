#!/bin/bash
if [[ -n "$VIRTUAL_ENV" ]]; then
    echo "Deactivating existing virtual environment..."
    deactivate
fi
echo "Activating virtual environment..."
source docs-venv/bin/activate
echo "Virtual environment activated."
