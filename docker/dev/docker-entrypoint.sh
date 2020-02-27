#!/bin/bash
eval "$(/opt/anaconda/bin/conda shell.bash hook)"

exec "$@"