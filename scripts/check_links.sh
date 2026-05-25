#!/usr/bin/env bash
set -euo pipefail

files=(README.md)
while IFS= read -r file; do
  files+=("$file")
done < <(find docs -name "*.md" -print | sort)

lychee \
  --verbose \
  --no-progress \
  --accept 200,204,206,301,302,403,429 \
  "${files[@]}"
