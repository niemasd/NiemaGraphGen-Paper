#!/usr/bin/env bash
jupyter nbconvert --to html --ExecutePreprocessor.allow_errors=True --ExecutePreprocessor.timeout=-1 --execute "$(dirname $(realpath -s $0))/Figures.ipynb"
