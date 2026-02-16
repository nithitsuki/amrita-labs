#!/bin/sh

if [ $# -eq 0 ]; then
  echo "Usage: $0 <directory>"
  exit 1
fi

cd "$1" || {
    echo "directory $1 does not exist"
    exit 1
}

echo "Listing .txt files in directory"

for arg in *.txt
do
    if [ -f "$arg" ]; then
        echo "Found: $arg"
    fi
done