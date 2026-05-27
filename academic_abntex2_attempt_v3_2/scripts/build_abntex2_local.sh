#!/bin/bash
# build_abntex2_local.sh — Build local do documento abnTeX2
# Uso: bash scripts/build_abntex2_local.sh
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
BASE_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

cd "$BASE_DIR"
python3 scripts/build_abntex2_from_colab.py
python3 scripts/validate_abntex2_outputs.py
