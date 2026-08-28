#!/usr/bin/env bash
# The Hadoop way: upload input to HDFS, run WordCount through YARN,
# then read the result back from HDFS.
set -euo pipefail
cd "$(dirname "$0")"

BASE=/user/$(id -un)/wordcount
INPUT="$BASE/input"
OUTPUT="$BASE/output"
INPUT_FILE="${1:-input.txt}"

if [ ! -f "$INPUT_FILE" ]; then
  echo "Input file not found: $INPUT_FILE"
  exit 1
fi

if [ ! -f wordcount.jar ]; then
  echo "wordcount.jar missing - run ./build.sh first"
  exit 1
fi

echo "==> Cleaning input dir: $INPUT"
hdfs dfs -rm -r -f "$INPUT" >/dev/null
echo "==> Creating HDFS input dir: $INPUT"
hdfs dfs -mkdir -p "$INPUT"

echo "==> Uploading $INPUT_FILE to HDFS"
hdfs dfs -put "$INPUT_FILE" "$INPUT/"

echo "==> Removing any previous output: $OUTPUT"
hdfs dfs -rm -r -f "$OUTPUT" >/dev/null

echo "==> Submitting WordCount job to YARN"
hadoop jar wordcount.jar WordCount "$INPUT" "$OUTPUT"

echo
echo "==> Top 10 words by count ($OUTPUT/part-r-00000):"
tmp="opfile.txt"
hdfs dfs -cat "$OUTPUT/part-r-00000" | sort -t $'\t' -k2,2 -rn > "$tmp"
head -n 10 "$tmp"
rm -f "$tmp"
