#!/usr/bin/env bash

FILES="test-chunks/*"

for f in $FILES
do
    echo "Processing $f files..."
    fname=$(basename -- "$f")
    fdir="${fname%.*}"
    mkdir "test-embeds/$fdir"
    python extract.py esm1b_t33_650M_UR50S $f test-embeds/$fdir --include mean
done