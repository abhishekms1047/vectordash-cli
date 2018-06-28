#!/usr/bin/env bash

rm -r dist/
python3 setup.py sdist
twine upload dist/* -r testpypi
twine upload dist/*