#!/bin/bash
set -e

# Install dependencies
pip install -r requirements.txt

# Start the application
gunicorn -b 0.0.0.0:$PORT chat:app
