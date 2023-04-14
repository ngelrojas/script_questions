#!/bin/bash

if [ -z "$VIRTUAL_ENV" ]; then
  source ./backend/bin/activate
else
  echo "Virtual environment is active: $VIRTUAL_ENV"
fi

python3 main.py