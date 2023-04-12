#!/bin/bash

black .
pytest && flake8
