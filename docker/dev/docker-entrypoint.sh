#!/bin/bash
eval "$(/opt/anaconda/anaconda/bin/conda shell.bash hook)"

exec "$@"