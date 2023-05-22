#!/bin/bash
rm -rf dist
rm -rf auto_codebase_documenter.egg-info
python setup.py sdist
twine upload dist/*
